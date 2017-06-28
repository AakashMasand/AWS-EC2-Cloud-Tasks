"""
01KeyPairGenerator.py
====================

The script is responsible for generating 
key-pairs which can be used for authentication
when running ec2 instances in AWS.
These key-pairs will be stored in the home folder.


Author	:	Akash Masand
Email	:	akash27@protonmail.com
Version: 0.1, 28/06/2017
"""

import boto3

ec2 = boto3.resource('ec2', region_name="ap-southeast-2")

#opening/creating a file MyKeyPair in write only mode
outfile = open('MyKeyPair.pem','w')

#key pair creation for authentication
KeyPairOut=""
try:
	key_pair = ec2.create_key_pair(KeyName='MyKeyPair')
	KeyPairOut = str(key_pair.key_material)
	print(KeyPairOut+"\n\n Success, Keypair Generated!")
	outfile.write(KeyPairOut) #write the value of KeyPairOut in MyKeyPair.pem
	
except Exception as e:

    print(str(e)) # print the error message if an error is generated.
