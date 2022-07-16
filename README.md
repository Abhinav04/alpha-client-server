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

It is always recommended to create AWS Systems Manager parameters following the principles of Infrastructure as Code(IaC). This ensures parameters can be repeatedly deployed across multiple regions/accounts from a single template. However, as of this time AWS Systems Manager Parameter store does not natively support replicating parameters across AWS regions/accounts. If you run into a situation where you may have existing SSM parameters created previously that now need to be copied over to another region/account but no code scripts to fulfill that purpose, we have an APG pattern created for you.

The code in this repository is related to the APG pattern [Cross-Account and Cross-Region Migration of AWS Systems Manager Parameters](https://apg-library.amazonaws.com/content-viewer/author/ca6167e0-d53d-4623-80a4-91a94ef47af9) which provides detailed instructions on how to use the code.

At a high level, the pattern provides an AWS Lambda function code written and tested in Python 3.8 or later to handle -

- Copying existing AWS Systems Manager parameters to a different supported region in the same AWS account
- Copying existing AWS Systems Manager parameters to any cross account supported region
