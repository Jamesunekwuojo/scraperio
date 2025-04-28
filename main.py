from fastapi import FastAPI, Depends, HTTPException, Header

from models import ScrapeJob, Session

from contextlib import asynccontextmanager
import multiprocessing

AUTH_TOKEN = "secretapi"
pool = None

@asynccontextmanager

async def lifespan(app: FastAPI):
    global pool
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    yield
    pool.close()
    pool.join()

app = FastAPI(lifespan=lifespan)

def verify_token(x_auth_token: str = Header(...)):
    if x_auth_token != AUTH_TOKEN:
        raise HTTPException(status_code=403, detail= "Invalid auth_token")
    
@app.post("/submit", dependencies=[Depends(verify_token)])

def submit_scrape_job(url:str):
    session = Session()
    new_job = ScrapeJob(url=url)
    session.add(new_job)
    session.commit()
    
    # web scraping logic
    
    return {"job_id": new_job.id, "status":"submitted"}

@app.get("/status/{job_id}", dependencies=[Depends(verify_token)])

def get_job_status(job_id:int):
    session = Session()
    job = session.query(ScrapeJob).get(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return {"job_id": job.id, "status": job.status, "result": job.result}
 
    