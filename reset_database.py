# reset_database.py

from database.db import engine
from database.models import Base

# ⚠️ Attention : cela supprime toutes les tables de la base de données !
print("⚠️ Suppression des tables...")
Base.metadata.drop_all(engine)

print("✅ Création des tables...")
Base.metadata.create_all(engine)

print("🎉 Base de données réinitialisée avec succès.")
