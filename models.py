import os
from sqlalchemy import create_engine, Column, Integer, String, Text


from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class ScrapeJob():
    def __init__(self, job_id, url, status):
        self.job_id = job_id
        self.url = url
        self.status = status

    def __repr__(self):
        return f"<ScrapeJob(job_id={self.job_id}, url={self.url}, status={self.status})>"
    
