import pandas as pd
import io
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# ----------------------
# CONFIGURATION
# ----------------------
STORAGE_ACCOUNT_NAME = "adlseljattioui"  # Remplace par le tien
CONTAINER_NAME = "wttj"
BLOB_NAME = "data.csv"

# ----------------------
# CONNEXION AU STORAGE ACCOUNT
# ----------------------
print(" Connexion au Storage Account Azure...")
ACCOUNT_URL = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url=ACCOUNT_URL, credential=credential)

blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)
csv_bytes = blob_client.download_blob().readall()

# ----------------------
# LECTURE DU CSV EN MÉMOIRE
# ----------------------
print("Lecture du fichier CSV...")
df = pd.read_csv(io.BytesIO(csv_bytes))

# ----------------------
# NETTOYAGE DE BASE
# ----------------------
print("Nettoyage des données...")

# Supprimer les doublons
#df.drop_duplicates(inplace=True)

# Supprimer les colonnes 100% vides
#df.dropna(axis=1, how='all', inplace=True)

# Nettoyer les chaînes (espaces, majuscules inutiles)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# Convertir les dates
df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')

# Remplacer les vides par NaN
df.replace('', pd.NA, inplace=True)

# Afficher un aperçu
print("Aperçu des données nettoyées :")
print(df.head())

# Sauvegarde locale (optionnel)
df.to_csv("cleaned_job_data.csv", index=False)
print("Fichier nettoyé sauvegardé : cleaned_job_data.csv")
