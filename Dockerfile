FROM python:3.9

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

COPY . .
