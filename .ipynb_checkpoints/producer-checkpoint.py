import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['16.16.196.230:9092'],
                         value_serializer = lambda x:
                         dumps(x).encode('utf-8'))

producer.send('demo_testing', value={'hello':'world'})