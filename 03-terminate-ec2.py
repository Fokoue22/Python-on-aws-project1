import boto3
import logging 
import schedule
import time 
from dotenv import load_dotenv
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#call the boto client
ec2 = boto3.resource('ec2', region_name = 'us-east-1')
 
def terminate_ec2():

   statefilters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
   terminatefilters=[{'Name': 'instance-state-name', 'Values': ['terminated']}]
   # command to terminate and ec2 instance 
   #ec2.instances.filter(statefilters).terminate()
   instance = ec2.instances.filter(Filters=statefilters)
   for instance in ec2.instances.filter(Filters=statefilters).terminate():
   #this code will print the image id of all ec2 that was terminated
      #instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}])
      print(type(instance(terminatefilters)))

#    try:
#          instance = ec2.instances.filter()
#    except ClientError as error:
#          logging.error(f'An error occurred try to read the error messages:{error}')
#          return False
#    return True 
      
# schedule.every(10).seconds.do(terminate_ec2)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == '__main__':
    instances = terminate_ec2()



