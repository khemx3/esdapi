from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}

@router.get("/getapi")
async def Call_Rick_And_Morty_API():
    response = requests.get("https://rickandmortyapi.com/api/character/1").json()
    return response["id"], response["name"]