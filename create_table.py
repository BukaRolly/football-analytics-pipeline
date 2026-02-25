import subprocess
import os

def run_dbt():
    """Run dbt models in the dbt folder."""
    # Path to your dbt project
    dbt_dir = os.path.join(os.getcwd(), "dbt")

    # Full path to dbt.exe in your Python Scripts folder
    # Replace this path with where your dbt.exe is actually installed
    dbt_executable = r"C:\Users\bulcs\AppData\Local\Python\pythoncore-3.14-64\Scripts\dbt.exe"

    # Run 'dbt run' using the full path
    result = subprocess.run(
        [dbt_executable, "run", "--profiles-dir", os.path.expanduser("~/.dbt")],
        cwd=dbt_dir,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("DBT run failed:")
        print(result.stderr)
    else:
        print("DBT run succeeded:")
        print(result.stdout)

run_dbt()