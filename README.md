# cv-service-1

### Description
This project does not do much for now, it just publish 2 endpoints:
- `cv1/helloworld` which will responde with `helloworkd <uuid>` and produce event message `hello-cv1`
- `cv1/healthcheck`

It will be used by the cluster [cv-k8s](https://github.com/s1lv10fr4gn4n1-org/cv-k8s).


### Requirements
- [Python3](https://www.python.org/downloads/)


### How to build
Run local
- `pip3 install -r requirements.txt`
- `python3 cv_service_1.py`

Build container image 
- `docker build -t <image_name> .`