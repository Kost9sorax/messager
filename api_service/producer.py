from kafka import KafkaProducer
import json
import pickle


def post_kafka(message):
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    data = {
        'message': {
            'id': message.id,
            'message': message.message
        },
    }
    serialized_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
    producer.send('Topic', serialized_data)
    return print('ok')
