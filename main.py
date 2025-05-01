from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys



if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifact=DataIngestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)