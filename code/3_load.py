import os 
import pandas as pd
import boto3
from botocore.exceptions import ClientError

def upload_file(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket"""
    s3 = boto3.resource('s3', 
        endpoint_url='https://play.min.io:9000',
        aws_access_key_id='Q3AM3UQ867SPQQA43P2F',
        aws_secret_access_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
        aws_session_token=None,
        config=boto3.session.Config(signature_version='s3v4'),
        verify=False
    ).meta.client

    # create bucket if it does not exist
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    if bucket_name not in buckets:
        s3.create_bucket(Bucket=bucket_name)   

    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        response = s3.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        print("ERROR", e)
        return False
    return True

if __name__ == '__main__':
    # 👇 Replace with your NetID
    bucket = 'ist356447352240'  # e.g. 'ist356mdaniel'
    
    # 👇 Local file to upload
    file_path = 'cache/survey.csv'  # or any file you want to upload
    object_name = os.path.basename(file_path)  # 'survey.csv'

    if upload_file(file_path, bucket, object_name):
        print(f"✅ Uploaded {file_path} to {bucket}/{object_name}")
    else:
        print(f"❌ Failed to upload {file_path}")
