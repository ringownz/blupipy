import sys
import subprocess
import os

MODULE_NAME = '{{ cookiecutter.project_slug}}'


def is_docker_installed():
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def get_root_dir():
    DIR_FILE = os.path.dirname(os.path.abspath(__file__))
    PROJ_DIR = os.path.join(DIR_FILE, '../' + MODULE_NAME)
    return PROJ_DIR


if __name__ == "__main__":
    if not is_docker_installed():
        print("ERROR: Docker is not installed.")
        sys.exit(1)

    if '{{ cookiecutter.ruff }}' == "true":
        #subprocess.run("/", 'poetry', 'add', 'ruff@latest'])
        print()