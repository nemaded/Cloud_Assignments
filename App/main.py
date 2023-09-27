from fastapi import FastAPI, Depends, HTTPException, status, Request
# from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import psycopg2
from psycopg2.extras import RealDictCursor
from .database import  engine
from fastapi.responses import JSONResponse
from .database import SessionLocal


app = FastAPI()
def middleware():
    try:
            connection=engine.connect()        
            test_query = text('SELECT 1')
            connection.execute(test_query)
           
            return True
    except OperationalError:
        return False

@app.get("/healthz",status_code=status.HTTP_200_OK)
def root():
    if middleware():
         headers = {"Cache-Control": "no-cache"}  
         return JSONResponse(content={"message":"connected"},headers=headers)
        
    else:
         raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Bad connection")









