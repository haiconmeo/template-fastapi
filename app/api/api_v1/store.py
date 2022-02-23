import boto3
from app.core.config import settings
session = boto3.session.Session()

client = session.client('s3',
                        region_name=settings.AWS_DEFAULT_REGION,
                        endpoint_url=settings.AWS_ENDPOINT,
                        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

url_cdn_s3 = settings.AWS_URL
url_cdn_cnd =settings.AWS_CDN
Bucket = settings.AWS_BUCKET
# OBJECT_NAME =None
# url_cdn_font =settings.AWS_URL_FONT
public_read = boto3.resource('s3',
    region_name=settings.AWS_DEFAULT_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    endpoint_url=settings.AWS_ENDPOINT,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,)

