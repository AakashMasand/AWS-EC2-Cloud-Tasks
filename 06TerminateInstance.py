"""
05StopInstance.py
====================

The script is responsible for changing the state of EC2 Instances that have
'Deployment' tag value as 'TestSession' to 'terminated' state.

Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""

import boto3
import time

ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['*']}]) #all instances, unlike the previous tasks where only running instances were chosen

for instance in instances:
	
	#variables
	state = instance.state['Name'] #instance-state-name
		
	#conditions
	for tag in instance.tags:
		if tag['Key'] == 'Deployment' and tag['Value'] == 'TestSession': #condition for 'Deployment' == 'TestSession'
			instance.terminate()	#Method to terminate instance
			
			#reloading instance states
			instance.load()
			state = instance.state['Name']
	
	#Wait until the instance transitions from shutting-down to terminated state
	while state == 'shutting-down':
		print("\n"+instance.id+" is shutting-down...")
		time.sleep(15)
		
		#reloading instance states
		instance.load()
		state = instance.state['Name']
		
	#Display instances that have been terminated	
	if state == 'terminated':
		print(instance.id+" has been terminated.")