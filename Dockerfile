FROM python:3.6.13-alpine3.12

RUN mkdir /opt/cv_service_1/
WORKDIR /opt/cv_service_1/

ADD . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python3 cv_service_1.py