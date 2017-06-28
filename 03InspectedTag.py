"""
03InspectedTag.py
=================

The script is responsible for creating an Inspected Tag with current date and time
to all the EC2 instances that contain the ‘Deployment’ tag and value from the previous task.
No change has been made to the Tags generated in 02InstanceGenerator.py

Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""
import boto3
import datetime #Inbuilt Library to import current date and Time
ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]) #Create a dict of all running instances

#Creating the Inspected tag with current date and time
for instance in instances:
	name = ''
	tags = {}
	
	for tag in instance.tags:
		
		inspectTime = datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')
		
		if tag['Key'] == 'Deployment' and tag['Value'] == 'TestSession':
			ec2.create_tags(Resources = [instance.id], Tags=[{'Key': 'Inspected', 'Value':''+inspectTime}])
			print("Inspected tag created for "+ instance.id+" is "+inspectTime)