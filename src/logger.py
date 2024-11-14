'''
Everything will be logged. Easy to track errors. For that we implement logger.
'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{ datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# getting log path
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

#log files will be created w.r.t the current working directory
os.makedirs(logs_path, exist_ok=True) 
## exist_ok = True => even if the folder exists, it will keep appending the logs

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

'''
To change anything from the default, change in the basicConfig of logging module
'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  #print the specific messages
)

##testing...
#if __name__ == "__main__":
#    logging.info("Logging has started!")