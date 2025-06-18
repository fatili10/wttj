from pathlib import Path

readme_content = """
# Welcome to the Jungle Job Scraper & API

Ce projet extrait des offres d’emploi depuis [Welcome to the Jungle](https://www.welcometothejungle.com/fr), les structure, les nettoie et les expose via une API REST.  
Il utilise **FastAPI**, **SQLAlchemy**, **Azure SQL Database**, et des outils de scraping comme **Selenium** et **BeautifulSoup**.

---

## 🚀 Objectifs du projet

- Scraper les offres d’emploi et entreprises depuis Welcome to the Jungle.
- Nettoyer et structurer les données.
- Stocker les données dans une base relationnelle sur Azure (SQL Server).
- Exposer les données à travers une API REST moderne avec FastAPI.

---

## 🏗️ Architecture du projet

Toujours afficher les détails

Copier
from pathlib import Path

readme_content = """
# Welcome to the Jungle Job Scraper & API

Ce projet extrait des offres d’emploi depuis [Welcome to the Jungle](https://www.welcometothejungle.com/fr), les structure, les nettoie et les expose via une API REST.  
Il utilise **FastAPI**, **SQLAlchemy**, **Azure SQL Database**, et des outils de scraping comme **Selenium** et **BeautifulSoup**.

---

## 🚀 Objectifs du projet

- Scraper les offres d’emploi et entreprises depuis Welcome to the Jungle.
- Nettoyer et structurer les données.
- Stocker les données dans une base relationnelle sur Azure (SQL Server).
- Exposer les données à travers une API REST moderne avec FastAPI.

---

## 🏗️ Architecture du projet

.
├── api/ # Routes FastAPI
│ └── jobs.py
├── clean_job/ # Scripts de nettoyage des données
├── data/ # Fichiers CSV temporairement stockés
├── database/
│ ├── db.py # Connexion DB
│ ├── models.py # Modèles SQLAlchemy
├── schemas/ # Pydantic schemas
│ └── job.py
├── scrapper/ # Scripts de scraping (Selenium, BS4)
├── main.py # Entrée de l'application FastAPI
└── README.md # Ce fichier