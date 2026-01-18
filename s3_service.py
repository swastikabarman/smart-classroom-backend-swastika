#Upload video to S3
#Return video URL

import boto3
import uuid

# AWS credentials (TEMPORARY – later we move to env variables)
AWS_ACCESS_KEY = "AKIARE6QMVYGODZF3LF7"
AWS_SECRET_KEY = "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"
AWS_REGION = "ap-south-1"
BUCKET_NAME = "edtech-video-storage-2026"

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_video_to_s3(file):
    file_extension = file.filename.split(".")[-1]
    s3_filename = f"videos/{uuid.uuid4()}.{file_extension}"

    s3_client.upload_fileobj(
        file.file,
        BUCKET_NAME,
        s3_filename,
        ExtraArgs={"ContentType": file.content_type}
    )

    video_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_filename}"
    return video_url
