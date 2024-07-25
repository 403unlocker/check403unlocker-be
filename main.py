from fastapi import FastAPI
from services.Anti403 import GetAnti403Handler
from services.Begzar import GetGetBegzarHandler
from services.Vanillapp import GetVanillappHandler
from services.Shecan import GetShecanHandler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/shecan")
def GetShecan(url):
    return GetShecanHandler(url)

@app.get("/begzar")
def GetBegzar(url):
    return GetGetBegzarHandler(url)

# @app.get("/anti403")
# def Get403(url):
#     return GetAnti403Handler(url)

@app.get("/vanillapp")
def GetVanillapp(url):
    return GetVanillappHandler(url)