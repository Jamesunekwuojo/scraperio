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
                title = soup.title.string if soup.title else "No title found"
                job.result = f"Title: {title}"
                job.status = "completed"
                break
            else:
                job.status = "failed"
                job.result = f"Failed to fetch URL, status code: {response.status_code}"
        except Exception as e:
            job.result= f"Error:{str(e)} (attempt {attempt+1}/3)"
        finally:
            session.commit()
            session.close()









# rootuser_password = candee1@unekwuojo

# fastapiuser_pass = candee1@

# I used scp -r  to copy files from my local machine to the server recursively
# scp -r /path/to/local/dir username@remote_host:/path/to/remote/dir
# Used nginix  for reverse proxy . i.e make  the api available or accessible on the public port I assignedd to it.

# U can proxy that's  route request from a public address port to a local Ip adress.  