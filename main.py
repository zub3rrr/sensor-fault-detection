from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline

# from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

# if __name__ == "__main__":
#   training_pipeline_config = TrainingPipelineConfig()
#   data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
#   print(data_ingestion_config.__dict__)

if __name__ == "__main__":
  training_pipeline = TrainPipeline()
  training_pipeline.run_pipeline()
  


