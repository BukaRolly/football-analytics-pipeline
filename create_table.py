import subprocess
import os

def run_dbt():
    """Run dbt models in the dbt folder."""
    dbt_dir = os.path.join(os.getcwd(), "dbt")  # path to your dbt project

    result = subprocess.run(
        ["dbt", "run", "--profiles-dir", "./"],  # just "dbt", no .exe
        cwd=dbt_dir,  # run inside the dbt folder
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("DBT run failed:")
        print(result.stderr)
        raise RuntimeError("dbt run failed")
    else:
        print("DBT run succeeded:")
        print(result.stdout)