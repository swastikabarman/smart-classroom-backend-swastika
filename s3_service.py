#Upload video to S3
#Return video URL

import boto3
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")


s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


def upload_video_to_s3(file_path: str):

    extension = file_path.split(".")[-1]
    key = f"videos/{uuid.uuid4()}.{extension}"

    s3.upload_file(file_path, BUCKET_NAME, key)

    return f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{key}"


