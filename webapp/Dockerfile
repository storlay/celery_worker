FROM python:3.10

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./image_downloader ./image_downloader

CMD [ "python3", "image_downloader/manage.py", "runserver", "0.0.0.0:8000" ]