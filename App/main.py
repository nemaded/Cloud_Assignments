from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.exceptions import RequestValidationError
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
         return Response(headers=headers)
    else:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
        

@app.put("/healthz", status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
@app.patch("/healthz", status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
@app.delete("/healthz", status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
@app.post("/healthz", status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
def method_not_allowed():
    return Response(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)












