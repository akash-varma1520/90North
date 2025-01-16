import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    file_content = event['file_content']
    file_name = event['file_name']

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    return {'message': 'File uploaded successfully'}
