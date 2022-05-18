from kafka import KafkaProducer
from signals import update_stock
import json

if update_stock.created:
    print('True')
else:
    print('False')

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          api_version=(3, 1, 1))
#
# producer.send('Messages', json.dumps('Oleg').encode('utf-8'))
# producer.flush()
