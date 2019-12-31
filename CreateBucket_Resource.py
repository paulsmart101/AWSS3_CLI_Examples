#!/bin/python
import boto3

bucketname = 'paulsmart121212121'

s3_resource = boto3.resource('s3')

'''
s3_resource.create_bucket(Bucket=bucketname,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    })
'''    
bucket_versioning = s3_resource.BucketVersioning(bucketname)
print(bucket_versioning.status)
bucket_versioning.enable()
print(bucket_versioning.status)