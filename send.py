'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-04-20 14:13:52
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-04-20 14:14:08
 # @ Description:
 '''


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a hello queue
channel.queue_declare(queue='hello')

# 
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()