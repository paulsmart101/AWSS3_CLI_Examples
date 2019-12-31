#!/bin/python
import boto3

bucketname = 'paulsmart89898989'
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket=bucketname,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    })