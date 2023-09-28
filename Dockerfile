FROM python:3.7.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /src

COPY ./requirements.txt /src
COPY ./.env /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /src/app

EXPOSE 3978
