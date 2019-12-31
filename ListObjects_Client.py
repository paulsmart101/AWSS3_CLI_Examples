#!/bin/python
import boto3

s3_client = boto3.client('s3')

objects = s3_client.list_objects_v2(Bucket='paulsmart-pics2')
print objects
print
print objects['Name']
print
print objects['ResponseMetadata']

for obj in objects['Name']:
    print obj
    
#for obj in s3_client.list_objects_v2(Bucket='paulsmart-pics2'):
#    print(obj.key)