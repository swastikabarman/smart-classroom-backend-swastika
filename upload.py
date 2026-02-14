#function writes into existing videos table

from database.db import SessionLocal
from sqlalchemy import text


def insert_video(title, subject, video_url, teacher_id, description=None):
    db = SessionLocal()

    query = text("""
        INSERT INTO videos
        (title, description, subject, video_url, status, teacher_id)
        OUTPUT INSERTED.id
        VALUES
        (:title, :description, :subject, :video_url, 'PUBLISHED', :teacher_id)
    """)

    result = db.execute(query, {
        "title": title,
        "description": description,
        "subject": subject,
        "video_url": video_url,
        "teacher_id": teacher_id
    })

    video_id = result.scalar()

    db.commit()
    db.close()

    return video_id


def insert_notes(video_id, language, content):
    db = SessionLocal()

    query = text("""
        INSERT INTO video_notes (video_id, language, content)
        VALUES (:video_id, :language, :content)
    """)

    db.execute(query, {
        "video_id": video_id,
        "language": language,
        "content": content
    })

    db.commit()
    db.close()
