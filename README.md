# Lambda for DB chart 0 on webpage

## Overview

The code contained in this repo includes:
* rds_config_sample.py
* app0.py

Replace the variables found in `rds_config_sample.py` with the variables provided to you from your backend developer.

## Creating the deployment package
Follow the instructions at the link below:
* https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

The basic idea here is that you will create a virtual enviornment with the external packages required then `cd` into that to zip and pull them out. After that would will just zip your application code (`app0.py` in this case) and specify the `file`.`handler` function call in the lambda function.

## Settings on the lambda function
* Set the lambda function into secturity gorup `wizard-2` and the execution role to `lambda-vpc-role`. These have been configured for you and will have the correct whitelists to access the RDS configured for you.