"""
This script requires that you have the proper key and ids in place,
Which are obviously not going to be included in a public GitHub repo.
"""


import boto3
s3 = boto3.resource('s3')

def view_buckets():
	for bucket in s3.buckets.all():
		print(bucket.name)

def upload(bucket, *files):
	for items in files:
		data = open(items, 'rb')
		s3.Bucket(bucket).put_object(Key=items, Body=data)