from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from database.upload import insert_video, insert_notes
from s3_service import upload_video_to_s3
from app.teacher.video_notes.notes_generator import generate_notes

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/upload-video")
def upload_video(
    file: UploadFile = File(...),
    title: str = Form(...),
    subject: str = Form(...),
    teacher_id: int = Form(...),
    description: str = Form(None)
):

    # 1 save locally
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2 upload to S3
    video_url = upload_video_to_s3(temp_path)

    # 3 save video → get id FIRST
    video_id = insert_video(title, subject, video_url, teacher_id, description)

    # 4 generate notes
    generate_notes(temp_path, video_id)

    # 5 delete temp
    os.remove(temp_path)

    return {"message": "Video + notes generated"}
