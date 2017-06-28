"""
02InstanceGenerator.py
====================

The script is responsible for creating two EC2 instances with
Amazon Linux Image and MyKeyPair.pem generated in
KeyPairGenerator.py

The script also adds the following tags to the EC2 Instances:

EC2 Instance 1:
Name: TestMachine A
Deployment: TestSession

EC2 Instance 2:
Name: TestMachine B
Deployment: TestSession

Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""

import boto3
import time

ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

#Generating instances using the create_instances method
instances = ec2.create_instances(
	ImageId='ami-a18392c2',	#ami-a18392c2 is the AMI ID for Amazon Linux Image. 
							#To find the AMI ID of the other Images, 
							#refer: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html
	KeyName="MyKeyPair",	#KeyPair Generated in 01KeyPairGenerator.py
	MinCount=1,
	MaxCount=2,				#Generates 2 Ec2 Instances. Change this value to generate the desired number of Images.
	InstanceType="t2.micro"
)


counter=0 					#variable to keep a track of running instances.
							#For Name Tag
for instance in instances:
	state = instance.state['Name']	#Getting instance state - pending, running, etc.
									#This is important because an EC2 instance needs to be in
									#running state if tags need to be created for EC2 instances.
	counter+=1
	#time.sleep(10)
	while state == 'pending':		#Checking if EC2 Instance is in pending state
		print("\n"+instance.id+" is in pending state...")
		time.sleep(10)
		instance.load()				#Update all the attributes of the Instance so that EC2 Instance
									#state can be checked again.
		state = instance.state['Name']
		
	if state == 'running':
		print(instance.id+" is running")
		ec2.create_tags(Resources = [instance.id], Tags=[{'Key': 'Deployment', 'Value':'TestSession'}])	#Creating Tag - Deployment key with value TestSession for both EC2 Instances
		ec2.create_tags(Resources = [instance.id], Tags=[{'Key': 'Name', 'Value':'TestMachineA' if counter==2 else 'TestMachineB'}]) #Creating Tags - Test Machine A and B 
																																	
	instance.reload() #Update all the attributes of the instance to get tag information
	print("\nTags created:")
	for tag in instance.tags:
		print(tag['Key']+":"+tag['Value'])