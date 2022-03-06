import csv
from typing import Dict, List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

def read_data(delimiter=","):
    # Read data from csv file
    data = []
    with open("data.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = list(reader)
    return data


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data")
async def get_data() -> List[Optional[Dict[str, str]]]:
    """ Get data from csv file """
    return read_data()

@app.get("/shipment")
async def get_shipment() -> List[Optional[float]]:
    """ Get all shipments """
    return []

@app.get("/shipment/{int:id}")
async def get_shipment(id) -> List[Optional[float]]:
    """ Get all shipments """
    return []


@app.get("/random/{length}")
async def get_random_with_length(length: int) -> List[Optional[float]]:
    """ Get random array with given length """
    return create_random_array(length)


if __name__ == "__main__":
    print(read_data())
