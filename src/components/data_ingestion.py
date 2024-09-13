import sys
import os
import numpy as np
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder)


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config= DataIngestionConfig()
        self.utils = MainUtils()

    def export_collection_as_dataframe(self,collection_name,db_name):

        try:
            mongo_client = MongoClient(MONGO_DB_URL)

            collection = mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            """
            collection.find() : 

                                            {
                                    "_id": ObjectId("64f9c7ad63d0c69e4b9bb1e7"),
                                    "name": "John",
                                    "age": 25,
                                    "city": "New York"
                                },
                                {
                                    "_id": ObjectId("64f9c7ad63d0c69e4b9bb1e8"),
                                    "name": "Jane",
                                    "age": 30,
                                    "city": "Los Angeles"
                                }

            list(collection.find()):


                                                [
                                        {
                                            "_id": ObjectId("64f9c7ad63d0c69e4b9bb1e7"),
                                            "name": "John",
                                            "age": 25,
                                            "city": "New York"
                                        },
                                        {
                                            "_id": ObjectId("64f9c7ad63d0c69e4b9bb1e8"),
                                            "name": "Jane",
                                            "age": 30,
                                            "city": "Los Angeles"
                                        }
                                    ]

                    pd.Dataframe :
                    

                                    _id	name	age	city
                                    001	John	25	New York
                                    002	Jane	30	Los Angeles
                                    003	Mike	na	Chicago

            """



            if "_id" in df.columns.to_list():
                df = df.drop(columns=['_id'],axis=1)
            
            df.replace({"na":np.nan},inplace=True)

            return df
        except Exception as e:
            raise CustomException(e,sys)

    def export_data_into_feature_store_file_path(self)-> pd.DataFrame:

        try:

            logging.info(f"Exporting data from mongodb")
            raw_file_path = self.data_ingestion_config.artifact_folder

            os.makedirs(raw_file_path,exist_ok=True)

            sensor_data = self.export_collection_as_dataframe(
                collection_name= MONGO_COLLECTION_NAME,
                db_name = MONGO_DATABASE_NAME
            )

            logging.info(f"saving exported data into feature store file path :{raw_file_path}")

            feature_store_file_path = os.path.join(raw_file_path,'wafer_fault.csv')

            sensor_data.to_csv(feature_store_file_path,index=False)

            return feature_store_file_path
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self) -> Path:

        logging.info("Entered initiated_data_ingestion method of data_integration class")

        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()

            logging.info("got the data from mongodb")

            logging.info("exited initiate_data_ingestion methos of data ingestion class")

            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys) from e
        

        """
class Number:
    def __init__(self,val):
        self.val=val

a=Number(1)
a.val
--------------------
#with dataclass : mainly used for storing info

@dataclass
class Number:

    val:int

a=Number(1)
a.val

"""
