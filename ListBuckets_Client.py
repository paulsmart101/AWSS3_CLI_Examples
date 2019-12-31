#!/bin/python
import boto3

s3 = boto3.client('s3')
bucket_list = s3.list_buckets()

print bucket_list
print

for bucket in bucket_list['Buckets']:
    print bucket['Name']