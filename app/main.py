from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware
import sqltap
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os
from .schedulerRemove import run
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description= """ 
    Tìm các đối tượng title có chứa a 
    filter={"title__like":"%a%"}

    Tìm các đối tượng có  title có chứa a và id >=1  
    filter={"title__ilike":"%a%", "id__gte":1}

    Tìm các đối tượng có  title có chứa a và id <10 và owner_id =1
    filter={"title__like":"%a%", "id__lt":10, "owner_id": 1}
    
    Tìm các đối tượng có  title có chứa a(không phân biệt hoa thường) hoặc id >= 10 
    filter=[{"title__ilike":"%a%"}, {"id__gte":1}]
   
    Tìm các đối tượng có  title có chứa a hoặc id < 10  hoặc owner_id=1
    filter=[{"title__like":"%a%"}, {"id__lt":10}, {"owner_id": 1}]
    
    Tìm các đối tượng có  title có chứa a và id < 10  hoặc owner_id=1
    filter=[{"title__like":"%a%", "id__lt":10}, {"owner_id": 1}]
    
    Tìm các đối tượng có  title có chứa a và id < 10  và id >1 hoặc  owner_id=1
    filter=[{"title__like":"%a%", "id__lt":10, "id__gt": 1}, {"owner_id": 1}] 
    (A and B) or (C and D) \n 
    Tìm các đối tượng có  (title có chứa a và id < 10 ) hoặc ( id >1 và  owner_id=1)
    filter=[{"title__like":"%a%", "id__lt":10}, {"id__gt": 1, "owner_id": 1}] 
   
    Tìm các đối tượng có  (title có chứa a hoặc owner_id = 1 ) và ( owner_id >1 )
    filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "owner_id__lte": 20}

    Tìm các đối tượng có  (title có chứa a hoặc owner_id = 1 ) và ( owner_id__lte <=20 hoặc owner_id >= 10  )
    filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "1":[{"owner_id__lte": 20}, {"owner_id__gte": 10}]} """ 
)

#  scheduler
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=run, trigger='cron', hour='00', minute='00')
# scheduler.start()


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if settings.ENV == 'development':
    app.add_middleware(PyInstrumentProfilerMiddleware)

    @app.middleware("http")
    async def add_sql_tap(request: Request, call_next):
        profiler = sqltap.start()
        response = await call_next(request)
        statistics = profiler.collect()
        print(statistics)
        print("test")
        #sqltap.report(statistics, "report.html")
        # sqltap.report(statistics, "report.txt", report_format="text")
        return response
# Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())
app.include_router(api_router, prefix=settings.API_V1_STR)
