from confluent_kafka import Consumer, KafkaException
import json
from pymongo import MongoClient

def consume_messages(consumer, topics, mongo_collection):
    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1000)
            if msg is None:
                continue
            if msg.error():
                if isinstance(msg.error(), KafkaException) and msg.error().code() == KafkaException.PARTITION_EOF:
                    continue
                else:
                    print('Error: {}'.format(msg.error()))
                    break

            message = json.loads(msg.value())
            print('Received message: {}'.format(message))

            mongo_collection.insert_one(message)
            print('Message uploaded to MongoDB')

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

def main_consumer():
    mongo_uri = "mongodb+srv://sujithvl109:sujithvl109@db1.d8tr7xm.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_uri)

    db = client.get_database('stockdatabase')  
    mongo_collection = db['btc']  

    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',  
        'group.id': 'python-consumer',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_conf)
    consume_messages(consumer, topics=['stock'], mongo_collection=mongo_collection)

if __name__ == '__main__':
    main_consumer()
