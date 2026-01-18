#function writes into existing videos table

from database.db import SessionLocal
from sqlalchemy import text

def insert_video(title, subject, video_url, teacher_id):
    db = SessionLocal()
    query = text("""
        INSERT INTO videos (title, subject, video_url, status, teacher_id)
        VALUES (:title, :subject, :video_url, 'PUBLISHED', :teacher_id)
    """)
    db.execute(query, {
        "title": title,
        "subject": subject,
        "video_url": video_url,
        "teacher_id": teacher_id
    })
    db.commit()
    db.close()