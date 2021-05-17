from flask import Flask
from flask import request
import uuid
import logging
from message_queue.mq_sender import MessageQueueSender

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
mq = MessageQueueSender("hello-cv1")
server_uuid = str(uuid.uuid1())


@app.route('/cv1/healthcheck', methods = ['GET'])
def healthcheck():
  logging.info(request.headers)
  mq.send_message("healthcheck " + str(uuid.uuid1()))
  return "ok " + server_uuid


@app.route('/cv1/helloworld', methods = ['GET'])
def hello_world():
  logging.info(request.headers)
  mq.send_message("helloworld " + str(uuid.uuid1()))
  return "helloworld " + server_uuid


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)