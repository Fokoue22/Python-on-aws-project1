import boto3
import logging
import schedule
import time 

#setup loggers that will track event when my code will run
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def list_all_instances():

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()

    my_list = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            server_name = instance['Tags'][0]['Value']
            instance_id = instance['InstanceId']
            image_id = instance['ImageId']
            instance_type = instance['InstanceType']
            instance_state = instance['State']['Name']
            # for devicemappings in instance['BlockDeviceMappings']:
            #     volume_id = devicemappings['Ebs']['VolumeId']
            my_list.append([server_name, instance_id, image_id, instance_type, instance_state])
            print(my_list)
    return my_list

schedule.every().day.at("01:18").do(list_all_instances)


if __name__ == '__main__': 
    logger.info(f'our list of servers: {list_all_instances()}')
    # retrieve&get data needed for the report
    instances = list_all_instances() # this statement will store all the return it will store it on the varaible INSTANCES
    
while True:
    schedule.run_pending()
    time.sleep(1)


