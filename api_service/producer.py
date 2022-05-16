from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0, 1))

name = b'Oleg'
producer.send('name', name)
producer.flush()
print(name)
