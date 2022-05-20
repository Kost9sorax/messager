from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(3, 1, 1))
