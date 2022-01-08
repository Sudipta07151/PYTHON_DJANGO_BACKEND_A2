from django.conf import settings
import boto3
from botocore.config import Config


class S3:
    def __init__(self):
        self.client = boto3.client('s3',
                                   region_name="us-west-2",
                                   aws_access_key_id="AKIATGJS6UQPZGLPKXBY",
                                   aws_secret_access_key="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",
                                   config=Config(signature_version='s3v4')
                                   )

    def get_presigned_url(self, key, time=3600):
        return self.client.generate_presigned_url(ClientMethod='put_object', ExpiresIn=time,
                                                  Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': key})

    def get_file(self, key, time=3600):
        return self.client.generate_presigned_url(ClientMethod='get_object', ExpiresIn=time,
                                                  Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': key})

    def delete_file(self, key):
        return self.client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)


