import typer
import subprocess
import os

from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def start(type_project: str = typer.Argument()
        # type_project: Annotated[
        #      str,
        #      typer.Argument(
        #          help="Type of project", show_default="Type of project you want to start"
        #      )]
        ):
    #type_project = 'fastapi'
    if type_project == 'django':
        print(f"Type project: {type_project}")
    elif type_project == 'fastapi':
        print(f"Type project: {type_project}")
        print("Starting setup FastApi.....")

        # Create Form with Answers
        # Project name
        proj_name = typer.prompt("What's the project name?")
        proj_slug = proj_name.lower().replace(' ', '-')
        proj_description = typer.prompt("What's the description of the project?")
        proj_full_name = typer.prompt("What's your name?")
        proj_email = typer.prompt("What's your email?")

        # Where to save
        proj_save = typer.prompt("Git or Local?").lower().strip()
        if proj_save == 'git':
            path = typer.prompt("What's the repository?")
        elif proj_save == 'local':
            path = typer.prompt("What's the abs path?")

        # Destined to deploy

        # Any of this tools will be used? :[X1, X2, X3]
        proj_tools = typer.prompt("Which tools will be used ")

        # Run command to initialize project with settings
        # https://github.com/arthurhenrique/cookiecutter-fastapi/tree/main

        answers_to_write = [
                            proj_name + "\n",               # name
                            proj_slug + "\n",               # slug
                            proj_description + "\n",        # description
                            proj_full_name + "\n",          # full name
                            proj_email + "\n",              # email
                            "\n",                           # release date local
                            "\n",                           # version
                            "1" + "\n",                     # ruff
                            "2" + "\n"                      # black
                            ]

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        TEMPLATE_PATH = os.path.join(ROOT_DIR, '../blueprints/project_template_fastapi')
        FILE_ANSWERS_PATH = os.path.join(TEMPLATE_PATH, 'answers.txt')

        with open(FILE_ANSWERS_PATH, 'w') as f:
            # for answer in answers_to_write:
            f.writelines(answers_to_write)

        # Start Setup
        cmd = ['make', '-C', TEMPLATE_PATH, 'init', 'create', 'clean']
        subprocess.run(cmd, stdout=subprocess.PIPE)


@app.command()
def hello():
    print("Hello bot")


if __name__ == "__main__":
    app()
    #app(prog_name="blupipy")
