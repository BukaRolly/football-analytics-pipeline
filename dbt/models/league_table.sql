-- dbt/models/league_table.sql
with home as (
    select 
        homeTeam_shortName as team,
        case 
            when score_fullTime_home > score_fullTime_away then 3
            when score_fullTime_home = score_fullTime_away then 1
            else 0
        end as Home_points,
        1 as Home_matches
    from {{ ref('PL25_26_Raw') }}
    where score_fullTime_home is not null
),

away as (
    select 
        awayTeam_shortName as team,
        case 
            when score_fullTime_away > score_fullTime_home then 3
            when score_fullTime_away = score_fullTime_home then 1
            else 0
        end as Away_points,
        1 as Away_matches
    from {{ ref('PL25_26_Raw') }}
    where score_fullTime_away is not null
)

select
    team,
    sum(Home_points) as Home_points,
    sum(Away_points) as Away_points,
    sum(Home_points + Away_points) as Total_points,
    sum(Home_matches) as Home_matches,
    sum(Away_matches) as Away_matches,
    sum(Home_matches + Away_matches) as Total_matches
from home
union all
select * from away
group by team
order by Total_points desc