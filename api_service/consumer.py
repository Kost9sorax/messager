from kafka import KafkaConsumer

consumer = KafkaConsumer('Messages',
                         bootstrap_servers=['localhost:9092'],
                         api_version=(3, 1, 1)
                         )

for i in consumer:
    print(i.value)
