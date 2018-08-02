import boto3
import json


BUCKET_NAME = 'twitterbotybce' # replace with your bucket name
KEY = 'config_reddit.json' # replace with your object key

s3 = boto3.resource('s3')

content_object = s3.Object(BUCKET_NAME, KEY)
file_content = content_object.get()['Body'].read().decode('utf-8')
json_content = json.loads(file_content)