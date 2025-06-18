# wttj/init_db.py

from database.models import Base
from database.db import engine

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès dans la base SQL Azure.")

if __name__ == "__main__":
    init_db()
