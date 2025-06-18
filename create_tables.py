from database.db import engine
from database.models import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès !")

if __name__ == "__main__":
    create_tables()
