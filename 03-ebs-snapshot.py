import boto3
import logging 
from dotenv import load_dotenv
from botocore.exceptions import ClientError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SNAPSHOT_NAME = 'snapshot_list'

def create_snapshot():
    ec2 = boto3.resource('ec2', region_name = 'us-east-1')
    sns_client= boto3.client('sns')

    statefilters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    snapshot_list=[]
    for instance in ec2.instances.filter(Filters=statefilters):
        for volume in instance.volumes.all():
            Volume_id = volume.id
            volume = ec2.Volume(Volume_id)
            desc = 'This is the snapshot of a stopped ec2 instance {}'.format(Volume_id)
            print('Creating the snapshot of the following volume: ', Volume_id)
            snapshot=volume.create_snapshot(Description=desc)
            snapshot_list.append(snapshot)

    print(snapshot_list) 

    sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:671765845629:notify-snapshot-vai-python',
        Subject='EBS Snapshots of a stopped ec2 instance',
        Message=str(snapshot_list)

    )
    # try:
    #     snapshot=create_snapshot()
    # except ClientError as error:
    #     logging.error(f'An error occurred try to read the error messages:{error}')
    #     return False
    # return True 


if __name__ == '__main__':
    instances = create_snapshot()
    


