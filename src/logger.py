import logging #This module is used to configure and write log messages.
import os # Provides functions to interact with the operating system, such as file and directory manipulation.
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #logs_path = /current_pwd/logs/09_12_2024.log

os.makedirs(logs_path,exist_ok=True) #if directory already exist, then don't throw error

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
filename=LOG_FILE_PATH,
format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
level=logging.INFO


)



# [2024-09-12 14:30:15,678] 10 root - INFO - This is a test message.
