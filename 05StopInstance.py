"""
05StopInstance.py
====================

The script is responsible for changing the state of EC2 Instances that have
their 'Name' tag as TestMachineB and 'Deployment' tag to 'stopped' state.

Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""

import boto3
import time

ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
	
	#variables
	nameFound = 0
	DeploymentFound= 0
	name = ""
	inspected = ""
	state = instance.state['Name']
	
	for tag in instance.tags:
		
		#condition to verify if TestMachineB exists
		if tag['Value'] == 'TestMachineB':
			nameFound = 1
			name = tag['Value']
		
		#condition to check if Deployment exists
		if tag['Key'] == 'Deployment':
			DeploymentFound = 1
			
	if nameFound == 1 and DeploymentFound == 1:
		instance.stop()
		
		#reload attributes of instances
		instance.load()
		state = instance.state['Name']
	
	#Wait until the machine transitions from stopping state to stopped state
	while state == 'stopping':	
		print("\n"+instance.id+" is stopping...")
		time.sleep(15)
		
		#reload attributes of instances
		instance.load()
		state = instance.state['Name']
	
	#Display instances with instance-state-name = "stopped"
	if state == 'stopped':
		print("\n"+instance.id+" has been stopped")
	
		
		
	
				
