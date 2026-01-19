#Upload video to S3
#Return video URL

import boto3
import uuid

BUCKET_NAME = "edtech-video-storage-2026"

s3_client = boto3.client("s3")

def upload_video_to_s3(file):
    file_extension = file.filename.split(".")[-1]
    s3_filename = f"videos/{uuid.uuid4()}.{file_extension}"

    s3_client.upload_fileobj(
        file.file,
        BUCKET_NAME,
        s3_filename,
        ExtraArgs={"ContentType": file.content_type}
    )

    video_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_filename}"
    return video_url
