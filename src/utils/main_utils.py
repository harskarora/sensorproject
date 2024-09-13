import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle 

# Python’s pickle module that serializes and saves Python objects to a file. 
# Serialization is the process of converting a Python object into a byte stream that can be stored in a file or transmitted over a network.

import yaml
"""
YAML is widely adopted in various fields, including DevOps, application development, and data interchange, 
due to its ease of use and clear syntax.

"""

import boto3


from src.constant import *
from src.exception import CustomException
from src.logger import logging #The src.logger module configures how and where the log messages will be written (to a file with a specific format). When MainUtils uses logging.info(), it writes messages to the log file configured by src.logger.




class MainUtils:
    def __init__(self) -> None:
        pass


    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)


        except Exception as e:
            raise CustomException(e, sys) from e


    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))


            return schema_config


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")


        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)


            logging.info("Exited the save_object method of MainUtils class")


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")


        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)


            logging.info("Exited the load_object method of MainUtils class")


            return obj


        except Exception as e:
            raise CustomException(e, sys) from e
   
    @staticmethod    
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e,sys)
   