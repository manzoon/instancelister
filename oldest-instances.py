import sys
from datetime import datetime, timezone
import boto3


aws_region = sys.argv[1]
instance_max = int(sys.argv[2])
current_time = datetime.now().replace(tzinfo=timezone.utc)
instance_counter = 0

ec2 = boto3.resource('ec2', aws_region)

all_instances = ec2.instances.all()

instance_list = []

for instance in all_instances:
    instance_id = instance.id
    instance_type = instance.instance_type
    instance_state = instance.state['Name']
    instance_age = round((current_time - instance.launch_time).total_seconds())
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            instance_name = tag['Value']
    instance_list.append({'ID': instance_id, 'Type': instance_type, 'Age': instance_age, 'State': instance_state, 'Name': instance_name})

sorted_list_of_instances = sorted(instance_list, key = lambda age: age['Age'], reverse=True)

for instance in sorted_list_of_instances:
    if (instance_counter < instance_max):
        if instance['State'] == 'running':
            print(instance['ID'], instance['Type'], instance['Age'], instance['Name'])
            instance_counter = instance_counter + 1