import slack
import logging 
import os 
# import schedule
# import time 
from dotenv import load_dotenv
from botocore.exceptions import ClientError
from pathlib import Path 
from dotenv import load_dotenv 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# SLACK_TOKEN = 'xoxb-4796957867426-4852417593346-VuygW4wavH8zF7Kposz2QQff'
FILE_NAME = 'ec2-report.csv'
EBS = 'snapshot_list'

def send_slack_message():

   ## creating ebs Snapshot that only create snapshot for stopped ec2 instance
    EMAIL = 'willcabrel735@gmail.com'
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path = env_path)
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    client.chat_postMessage(channel="#general", text= (f'Hello sir,\n\n And Ec2 report was generated, it containe {FILE_NAME}\n\n{EBS} and was send to this email:\n{EMAIL}\n\nThanks, \n\nFokoue Thomas!'))
    
    # try:
    #         client = client.chat_postMessage(channel="#general")
    # except client as error:
    #         logging.error(f'An error occurred try to read the error messages:{error}')
    #         return False
    # return True 


# schedule.every(5).seconds.do(send_slack_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


if __name__ == '__main__':
    instances = send_slack_message()