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