from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Table d'association many-to-many
job_tags = Table(
    'job_tags', Base.metadata,
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

job_locations = Table(
    'job_locations', Base.metadata,
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)

job_languages = Table(
    'job_languages', Base.metadata,
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('language_id', Integer, ForeignKey('languages.id'))
)

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    industry = Column(Text, nullable=True)
    creation_year = Column(Integer)
    nb_employees = Column(Integer)
    parity_women = Column(Float)
    average_age = Column(Float)
    url = Column(String(500))  # URL de l'entreprise
    logo = Column(Text)
    description = Column(Text)
    media_website = Column(String(500))
    media_linkedin = Column(String(500))
    media_twitter = Column(String(500))
    media_github = Column(String(500))
    media_stackoverflow = Column(String(500))
    media_behance = Column(String(500))
    media_dribbble = Column(String(500))
    media_xing = Column(String(500))
    jobs = relationship("Job", back_populates="company")


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    wttj_reference = Column(String(100))
    job_reference = Column(String(100))
    poste = Column(String(255))
    description = Column(Text)
    profile = Column(Text)
    published_at = Column(DateTime)
    updated_at = Column(DateTime)
    url = Column(String(500))
    remote = Column(String(50))
    remote_policy = Column(String(255))
    office_remote_ratio = Column(Float)
    contract_type = Column(String(50))
    contract_duration_min = Column(Integer)
    contract_duration_max = Column(Integer)
    salary_min = Column(Float)
    salary_max = Column(Float)
    salary_currency = Column(String(10))
    salary_period = Column(String(50))
    education_level = Column(String(100))
    recruitment_process = Column(Text)
    profession = Column(String(255))


    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="jobs")

    tags = relationship("Tag", secondary=job_tags, back_populates="jobs")
    locations = relationship("Location", secondary=job_locations, back_populates="jobs")
    languages = relationship("Language", secondary=job_languages, back_populates="jobs")


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    jobs = relationship("Job", secondary=job_tags, back_populates="tags")


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    jobs = relationship("Job", secondary=job_locations, back_populates="locations")


class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    jobs = relationship("Job", secondary=job_languages, back_populates="languages")
