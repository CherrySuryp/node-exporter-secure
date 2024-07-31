FROM python:3.11.6
RUN pip installation poetry
COPY pyproject.toml .
COPY poetry.lock .
RUN apt-get update -y
RUN poetry config virtualenvs.create false && poetry installation --no-dev --no-interaction --no-ansi
COPY . .