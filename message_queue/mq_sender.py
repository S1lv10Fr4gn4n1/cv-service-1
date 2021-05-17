import pika
import os
import threading
import logging

class MessageQueueSender(object):
  
  def __init__(self, queue_name):
    self.queue_name = queue_name
    self.init_connnection()

  def init_connnection(self):
    self.initialized = False
    try:
      host = os.getenv('RABBITMQ_HOST', "localhost")
      port = os.getenv('RABBITMQ_PORT', "5672")
      user = os.getenv('RABBITMQ_USER', "guest")
      password = os.getenv('RABBITMQ_PASS', "guest") 
      
      credentials = pika.PlainCredentials(user, password)
      parameters = pika.ConnectionParameters(host, port, '/', credentials)
      self.connection = pika.BlockingConnection(parameters)
      self.channel = self.connection.channel()
      self.initialized = True
    except Exception:
      logging.error(">>> MessageQueueSender not initialized")

  def try_to_initialize(self):
    logging.info(">>> trying to initialize connection with queue")
    thread = threading.Thread(target=self.init_connnection)
    thread.start()

  def send_message(self, message):
    if not self.initialized:
      logging.info(">>> Message saved and will be send later")
      self.try_to_initialize()
      return
   
    # create queue if doesn't exist
    self.create_queue(self.queue_name)
    
    try:
      # send message
      self.channel.basic_publish(exchange='', 
                                routing_key=self.queue_name, 
                                body=message,
                                # make message persistent
                                properties=pika.BasicProperties(delivery_mode=2))
      logging.info("Message sent to MQ '{}".format(message))
    except Exception:
      self.initialized = False
      logging.error(">>> Connection lost, message saved and will be send later")
    

  def create_queue(self, queue_name):
    # mark as durable to resist to rabbitmq crashes
    try:
      self.channel.queue_declare(queue=queue_name, durable=True)
    except Exception:
      logging.error(">>> Failed to queue_declare")
    
        
  def close(self):
    self.channel.close()
    self.connection.close()
