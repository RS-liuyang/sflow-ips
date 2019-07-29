#!/usr/bin/env python

import subprocess
from kafka import KafkaProducer

KAFKA_TOPIC = 'sflow'
KAFKA_BROKERS = '127.0.0.1:9092'

producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKERS])

p = subprocess.Popen(
  ['/usr/local/bin/sflowtool','-j'],
  stdout=subprocess.PIPE,
  stderr=subprocess.STDOUT
)

lines = iter(p.stdout.readline,'')
for line in lines:
    msg = str(line[:-1], encoding='utf-8')
    print(msg)
    producer.send(KAFKA_TOPIC, value=line[:-1])
