import time

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'alex-for-cluster',
    bootstrap_servers=['10.124.5.222:9092'],
    api_version=(2, 13),
    group_id='test',
    auto_offset_reset='earliest'
)
for msg in consumer:
    print(msg.value)

