"""
This script requires that you have the proper key and ids in place,
Which are obviously not going to be included in a public GitHub repo.
"""
from itertools import chain
from os import system
import boto3
s3 = boto3.resource('s3')

def view_buckets():
	for bucket in s3.buckets.all():
		print(bucket.name)

def upload(bucket, *files):
	"""
	Uploads files or folders to a specific S3 bucket
	"""
	try:
		for items in files:
			data = open(items, 'rb')
			s3.Bucket(bucket).put_object(Key=items, Body=data)
			print("{0} uploaded successfully".format(items))
	except IsADirectoryError:
		for items in files:
			# Rather than reinvent the wheel, use the Amazon CLI for directories
			system("aws s3 cp {items} s3://{bucket}/ --recursive".format(bucket=bucket, items=items))

def sync(src, dst, src_bucket=False):
	"""
	Sync S3 bucket or local directory with S3 bucket
	"""
	if src_bucket == False:
		system("aws s3 sync {src} s3://{dst}".format(src=src, dst=dst))
		print("Local directory '{src}' and S3 bucket '{dst}' synced successfully".format(src=src, dst=dst))
	else:
		system("aws s3 sync s3://{src} s3://{dst}".format(src=src, dst=dst))
		print("S3 buckets '{src}' and '{dst}' synced successfully".format(src=src, dst=dst))