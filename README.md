# sensor-fault-detection
This project aims at classifying whether a failure cause in heavy duty vehicle is caused by APS system or not . Where APS stands for Air Pressure System. An End-to-End project where affirmative class means failure is due to APS and negative class means Non APS system.

## Tech Stack Used

1. MongoDB
2. Kafka
3. FastAPI
4. Machine Learning Algorithms
5. Docker
6. Python

## Data Pipeline 
The Data which we will be using for our analytics usecase is generated number of sensors of Heavy Duty Vehicle(HDV). First we will write a Producer Kafka script in python so that pull the continously generated data from this sensors to Kafka Storage. Then we will use consumer script written in python so that we can pull the data from Kafka Storage to Mongo Storage. 
Further this data stored in Mongo Storage will be fetched in our local system for analytic use case.

### Data Pipeline Schema:
![alt text](https://raw.githubusercontent.com/zub3rrr/sensor-fault-detection/main/diagrams/data%20pipeline.png)
