import json 
import boto3
import logging
from botocore.exceptions import ClientError
  
# Opening JSON file 
#f = open('temp.json',) 
  
# returns JSON object as  
# a dictionary 
#data = json.load(f) 
  
# Iterating through the json 
# list 
#for i in data['menu']: 
 #   print(i) 
  
# Closing file 
#f.close() 


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


s3 = boto3.client('s3')
with open("temp.json", "rb") as f:
    s3.upload_fileobj(f, "pranayawsbucket", "OBJECT_NAME")