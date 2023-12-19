# Kafka Producer and Consumer Data Pipeline

This Python script demonstrates how to create a data pipeline using Kafka for producing random messages from a CSV dataset and consuming those messages to upload to MongoDB. The example uses the `confluent_kafka` library for Kafka integration, `pymongo` for MongoDB integration, and `pandas` for reading CSV data.

## Prerequisites

- Python 3.x
- Install required Python packages:
  ```bash
  pip install confluent_kafka pymongo pandas

  
## How to Use
- Clone the repository:
  ```bash
  git clone https://github.com/SujithVeeramani/Stock_Data_Pipeline
  cd Stock_Data_Pipeline
  

- Configure MongoDB URI in the main_consumer function:
    mongo_uri = "your_mongodb_uri"


- Configure Kafka consumer settings in the main_consumer function:
    ```bash
    consumer_conf = {
    'bootstrap.servers': 'your_kafka_bootstrap_servers',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
    }
- Configure Kafka producer settings in the main_producer function:
    ```bash
    producer_conf = {
    'bootstrap.servers': 'your_kafka_bootstrap_servers',
    'client.id': 'python-producer'
  }
  
- Run the Kafka producer script:
  ```bash
  python producer.py
  
- Run the Kafka consumer script:
  ```bash
  python consumer.py


- Configuration

  mongo_uri: MongoDB connection URI
  
  consumer_conf: Kafka consumer configuration.




