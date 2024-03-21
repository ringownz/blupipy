FROM python:3.11

EXPOSE 8000

ENV DEBIAN_FRONTEND=noninteractive

# apt-get dependencies
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install \
    curl

# Python -> python3
RUN ln /usr/bin/python3 /usr/bin/python

# Install poetry
#RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# Install cookiecutter
RUN pip install cookiecutter

# /etc/poetry/bin/poetry -> /usr/bin/poetry
#RUN ln /etc/poetry/bin/poetry /usr/bin/poetry

# Upgrading PIP
RUN pip3 install --upgrade pip

# Install project_template
WORKDIR /project_template_fastapi

COPY . .

# Entrypoint
RUN chmod a+x /project_template_fastapi/entrypoint.sh

ENTRYPOINT [ "/project_template_fastapi/entrypoint.sh" ]