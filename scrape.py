import requests
from bs4 import BeautifulSoup
from models import ScrapeJob, Session

def scrape_url(job_id, url):
    session = Session()
    job = session.query(ScrapeJob).get(job_id)
    
    job.status = "in_progress"
    session.commit()
    
    for attempt in range(3):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job.result = str(soup)
                job.status = "completed"
                break
            else:
                job.status = "failed"
        except Exception as e:
            job.status = "failed"









# rootuser_password = candee1@unekwuojo

# fastapiuser_pass = candee1@