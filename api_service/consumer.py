import json
import requests
from kafka import KafkaConsumer
from messager.settings import CONFIRMATION_PATH

consumer = KafkaConsumer('Messages',
                         bootstrap_servers=['localhost:9092'],
                         api_version=(3, 1, 1)
                         )


def check_string(message):
    if "абракадабра" in message:
        return True
    else:
        return False


for msg in consumer:
    if check_string(json.loads(msg.value.decode('unicode-escape'))['message']):
        payload = dict(message_id=json.loads(msg.value.decode('unicode-escape'))['id'], success=False)
    else:
        payload = dict(message_id=json.loads(msg.value.decode('unicode-escape'))['id'], success=True)
    requests.post('http://127.0.0.1:8000/api/v1/message_confirmation/', data=payload, headers={'Authorization': f'Bearer {json.loads(msg.value.decode("unicode-escape"))["token"]}'})
