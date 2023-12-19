# Stock Data Pipeline using Kafka Producer and Consumer 

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
  ```bash
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
  ```bash
  mongo_uri: MongoDB connection URI
  consumer_conf: Kafka consumer configuration.


## How to improve this pipeline?

- The Concept of data pipeline is to store the real time data from the producer and store it in the database or cloud storage
- The problem that I faced is the pricing of APIs 
- There is no free APIs which are as much as effective compared to the Paid ones
- Too overcome this I download a huge dataset and make this data pipeline works with the real time data
- If you have the access to the APIs replace the dataset ("data.csv") with API connection

## Contact me
### Have any issues while using this? Feel free to contact me

- LinkedIN  - https://www.linkedin.com/in/sujithvl/
- Instagram - https://www.instagram.com/sujith_vl_/
