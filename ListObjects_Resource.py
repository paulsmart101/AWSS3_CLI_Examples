#!/bin/python
import boto3
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(name='paulsmart-pics2')

for object in bucket.objects.all():
    print object
    
print
for obj in bucket.objects.all():
    subsrc = obj.Object()
    print(obj.key, obj.storage_class, obj.last_modified,subsrc.version_id, subsrc.metadata)