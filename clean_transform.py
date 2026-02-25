
import pandas as pd

def format_api_pull_to_dataframe(data):
    """Normalize the API JSON into a DataFrame."""
    df = pd.json_normalize(data["matches"])
    return df

def clean_dataframe(df):
    """Drop unwanted columns and fix column names."""
    df_clean = df.drop(
        columns=[
            "group","season.startDate","score.duration","score.winner",
            "season.winner","season.endDate","stage","score.halfTime.home",
            "score.halfTime.away","referees","area.id","area.name","area.code",
            "area.flag","competition.id","competition.name","competition.code",
            "competition.type","competition.emblem","season.id","homeTeam.id",
            "homeTeam.name","homeTeam.tla","homeTeam.crest","awayTeam.id",
            "awayTeam.name","awayTeam.tla","awayTeam.crest",'odds.msg',
            "score.regularTime.home","score.regularTime.away","score.extraTime.home",
            "score.extraTime.away","score.penalties.home","score.penalties.away"
        ],
        errors="ignore"
    )
    df_clean.columns = df_clean.columns.str.replace(".", "_", regex=False)
    return df_clean