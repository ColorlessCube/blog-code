import json
from datetime import datetime
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.124.5.191:9092',
                         value_serializer=lambda msg: json.dumps(msg).encode(),
                         api_version=(2, 13))
topic = 'test-for-cluster'
for i in range(0, 100):
    data = {
        'num': i,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    print(data)
    producer.send(topic, data)
    time.sleep(1)

