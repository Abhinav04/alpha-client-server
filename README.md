## Alpha Client-Server Setup

## Summary
This repository contains Alpha Client-Server Setup where Alpha Client and Alpha Server is defined as below:

- Alpha Client:
A linux based AWS Ec2 instance where users can login using SSH. As soon as an SSH login attempt is made on the instance, it is reported to Alpha Server.

- Alpha Server:
A linux based AWS Ec2 instance which runs a simple flask web app. This web app reports metrics of SSH attempts made on various alpha clients.

## Steps to setup architecture.

1. This complete architecture can be deployed using AWS Cloudformation. "deployment.yaml" is the cloudformation template which defines a VPC, subnets, security groups, An autoscaling client setup and a web server
2. You will need an AWS account and an IAM user with permissions to deploy the cloudformation stack.
3. Go to AWS Console > Services > Cloudformation > Create Stack > Upload a template file and select deployment.yaml
4. Fill in the parameter values. Values must be provided for "KeyPair" (You will be able to attempt SSH on the client instances using this keypair) and "YourCurrentIp" parameters. Rest of the parameters have a default value provided.
5. On hitting "Create Stack", the cloudformation stack will be deployed in around 5 minutes.
6. Go to Services > EC2. You will be able to see 3 client EC2 instances and 1 Server EC2 instance. To SSH into client instance, select the instance checkbox and grab the public IP. You can then use your KeyPair and attempt SSH to the instance. The client instances are part of an Auto-scaling group. The number of instances can be increased/decreased by adjusting the desired, min and max property for the autoscaling group in the cloudformation template.
7. To get the ssh attempt metrics you can run the below command on a terminal on your machine:

curl -k -X POST http://server-public-ip:5000/get-data

(Replace server-public-ip with Server IP address. You can grab the IP address from EC2 console)
