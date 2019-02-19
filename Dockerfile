FROM python:2.7
ENV PYTHONUNBUFFERED 1
ADD /config/requirements.txt /
RUN pip install -r /requirements.txt 
ADD ./src /src
WORKDIR /src
