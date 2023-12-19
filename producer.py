from confluent_kafka import Producer
import json
import time
import pandas as pd
import random

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_message(producer, topic, message):
    producer.produce(topic, value=json.dumps(message), callback=delivery_report)
    producer.poll(0)
    time.sleep(1)

def read_random_row_from_csv(used_indices):
    df = pd.read_csv('data.csv')
    
    # Exclude used indices
    available_indices = set(range(len(df))) - set(used_indices)
    
    if not available_indices:
        raise ValueError("All rows have been used. Resetting indices.")
    
    random_index = random.choice(list(available_indices))
    used_indices.add(random_index)
    
    random_row = df.iloc[random_index]
    return random_row.to_dict(), used_indices

def main_producer():
    producer_conf = {
        'bootstrap.servers': 'localhost:9092',  
        'client.id': 'python-producer'
    }

    producer = Producer(producer_conf)
    
    used_indices = set()

    try:
        while True:
            # Read a random row from the CSV dataset
            message, used_indices = read_random_row_from_csv(used_indices)
            produce_message(producer, 'stock', message)

            # Wait for 2 seconds before sending the next message
            time.sleep(2)

    except KeyboardInterrupt:
        pass
    finally:
        producer.flush()

if __name__ == '__main__':
    main_producer()
