import typer
import subprocess

from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def start(
        type_project: Annotated[
            str,
            typer.Argument(
                help="Who to greet", show_default="Deadpoolio the amazing's name"
            ),
        ]):
    if type_project == '':
        print(f"Type project: {type_project}")
    elif type_project == 'fastapi':
        print(f"Type project: {type_project}")
        print("Starting setup FastApi.....")

        # Create Form with Answers
        # Project name
        proj_name = typer.prompt("What's the project name?")

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

        answers_to_write = ["default_project\n",
                            "default_project\n",
                            "short description\n",
                            "\n", "\n", "\n", "\n",
                            "Default Person\n",
                            "default@email.com\n",
                            "\n", "\n"]

        with open('blueprints/project_template_fastapi/answers1.txt', 'w') as f:
            # for answer in answers_to_write:
            f.writelines(answers_to_write)

        # Start Setup
        cmd = ['make -C', './blueprints/project_template_fastapi', 'init', 'create', 'clean']
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        process.wait()


@app.command()
def hello():
    print("Hello bot")


if __name__ == "__main__":
    app(prog_name="blupipy")
