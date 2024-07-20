from fastapi import FastAPI
from services.Anti403 import GetAnti403Handler
from services.Begzar import GetGetBegzarHandler
from services.Vanillapp import GetVanillappHandler
from services.Shecan import GetShecanHandler

app = FastAPI()

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