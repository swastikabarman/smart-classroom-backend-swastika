from fastapi import FastAPI, UploadFile, File, Form
from s3_service import upload_video_to_s3
from database.upload import insert_video

app = FastAPI()


@app.post("/upload-video")
async def upload_video(
    file: UploadFile = File(...),
    title: str = Form(...),
    subject: str = Form(...),
    teacher_id: int = Form(...),
    description: str = Form(None)
):
    # 1. Upload video to S3
    video_url = upload_video_to_s3(file)

    # 2. Save metadata
    insert_video(
        title=title,
        subject=subject,
        video_url=video_url,
        teacher_id=teacher_id,
        description=description
    )

    return {
        "message": "Video uploaded and saved successfully",
        "video_url": video_url
    }



