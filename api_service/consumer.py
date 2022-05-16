from kafka import KafkaConsumer

consumer = KafkaConsumer('topic-name',
                         group_id='1',
                         bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print(msg)
