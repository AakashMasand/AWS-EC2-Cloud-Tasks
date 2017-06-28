"""
04UpdateInspected.py
====================

The script is responsible for Updating the Inspected Tag with current date and time
to all the EC2 instances that have 'Name' tag and value as 'TestMachineA'

Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""

import boto3
import datetime
ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
	


for instance in instances:
	
	#variables
	nameFound = 0 	#flag to check Name = TestMachineA
	inspectedFound= 0	#flag to check Inspected Tag
	
	inspectedTime = ''	#to store value of the current Inspected Tag
	
	#conditions
	for tag in instance.tags:
	
		if tag['Key'] == 'Name' and tag['Value'] == 'TestMachineA':
			nameFound = 1

		if tag['Key'] == 'Inspected':
			inspectedFound = 1
			inspectedTime = tag['Value']
			
			
				
				
	if nameFound == 1 and inspectedFound == 1:	#if Name = "TestMachineA" and Inspected tag exists...
		
		print("\nOld Inspected Time for "+instance.id+" is "+inspectedTime) #printing current Inspected tag value
		
		newInspectedTime = datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')
		
		instance.delete_tags(Resources = [instance.id], Tags=[{'Key': 'Inspected'}])	#deleting current Inspected tag
		ec2.create_tags(Resources = [instance.id], Tags=[{'Key': 'Inspected', 'Value':''+newInspectedTime}])	#generating new inspected tag
		
		print("Regenerated Inspected Time for "+instance.id+" is "+newInspectedTime)	#printing new Inspected tag value

	
		