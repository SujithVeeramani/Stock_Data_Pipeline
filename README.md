# Kafka Consumer with MongoDB Integration

This Python script demonstrates how to consume messages from a Kafka topic and upload them to MongoDB. The example uses the `confluent_kafka` library for Kafka integration and `pymongo` for MongoDB integration.

## Prerequisites

- Python 3.x
- Install required Python packages:
  ```bash
  pip install confluent_kafka pymongo pandas

  
## How to Use
- Clone the repository:
  ```bash
  git clone https://github.com/SujithVeeramani/Stock_Data_Pipeline
  

- Configure MongoDB URI in the main_consumer function:
    mongo_uri = "your_mongodb_uri"


- Configure Kafka consumer settings in the main_consumer function:
    ```bash
    consumer_conf = {
    'bootstrap.servers': 'your_kafka_bootstrap_servers',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
    }

  
- Run the Kafka consumer script:
  ```bash
  python consumer.py


Configuration

mongo_uri: MongoDB connection URI.
consumer_conf: Kafka consumer configuration.




