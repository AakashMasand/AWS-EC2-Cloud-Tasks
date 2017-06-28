TechConnect Graduate Cloud Engineer Tasks to Script/Automate
============================================================

Introduction
--------------
This project contains scripts for the purpose of AWS EC2 Instances Automation with specified requirements.


Intended Operating System
----------------------------

The script has been created in Windows 10. However, the script can be executed from the terminal/command prompt of any Operating System (Windows 7,8.x,10, Linux, etc.)

Scripting Languages Used
---------------------------

Python 3 has been used as the scripting language.

Packages/Library requirements needed to run any scripts
----------------------------------------------------------

In order to run all the scripts, **boto3** library is required. **Boto3** can be installed using pip in Python.

Each Task and Commands needed to run
---------------------------------------

NOTE: Please make sure that Python 3 has been installed on the system and the environment variables have been set up appropriately.


The tasks and the commands to execute the tasks are as follows:

1. Create a key-pair named **MyKeyPair** and save it as a **PEM** file in the home directory.

**Command: python 01KeyPairGenerator.py**

2. Launch two **t2.micro sized Amazon Linux EC2 instances** using MyKeyPair.pem generated in the previous tasks. The EC2 instances will have the following tags:

- **Deployment** Tag with the value **TestSession**
- **Name** Tag with one machine named as **TestMachineA** and other named as **TestMachineB**

**Command: python 02InstanceGenerator.py**

3. Add a new tag **Inspected** with current date and time to all EC2 instances that contain the **Deployment** tag and value from the previous task.

**Command: python 03InspectedTag.py**

4. Update that tag value of **Inspected** with current date and time to all EC2 instances that have **Name** tag with value **TestMachineA**.

**Command: python 04UpdateInspected.py**

5. Stop instances with **Name** tag of **TestMachineB** and contain the **Deployment** tag and value from the first task.

**Command: python 05StopInstance.py**

6. Terminate all EC2 instances with the **Deployment** tag and **TestSession** value.

**Command: python 06TerminateInstance.py**







