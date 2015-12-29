FROM python:3.5

MAINTAINER Ham Vocke

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . /usr/src/app

CMD [ "gunicorn", "app:app" ]
