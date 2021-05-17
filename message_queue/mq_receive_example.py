#!/usr/bin/env python

import pika
import time

queue = "hello-cv2"

# queue listener
def callback(ch, method, properties, body):
  print("Received %r" % body)
  print("Processing %r ..." % body)
  time.sleep(0.5)
  print("Finished %r" % body)
  ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue=queue, durable=True)

  # define the amount of tasks to fetch before work
  channel.basic_qos(prefetch_count=1)
  channel.basic_consume(queue=queue, on_message_callback=callback)
  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()


if __name__ == '__main__':
  main()