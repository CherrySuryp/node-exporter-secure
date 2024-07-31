FROM python:3.11.6
RUN pip install poetry
COPY pyproject.toml .
COPY poetry.lock .
RUN apt-get update -y
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi
COPY . .