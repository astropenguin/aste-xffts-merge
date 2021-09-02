FROM mcr.microsoft.com/vscode/devcontainers/python:3.8
ENV POETRY_VIRTUALENVS_CREATE=false

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry install
