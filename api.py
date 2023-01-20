from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PhotorazeController import Controller, STORAGE,Service
import shutil
import sys
import os
sys.setrecursionlimit(3000)
app = FastAPI(
    title='photoraze-stock'
)
controller = Controller()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def mainpage():
    return 'hello'


@app.get('/pictures')
def allpics():
    return controller.get_pics()


@app.delete('/pictures/{id}/delete')
def delete(id):
    return controller.delete(id)

@app.post('/addpic/')
def addpic(file: UploadFile):
    with open(STORAGE+file.filename,'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        controller.create(STORAGE+file.filename)
        return STORAGE+file.filename

@app.get('/search/{request}')
def searchpic(request):
    return controller.search(request)

@app.put('/pictures/{id}/edit')
def editpic(id, name, tags):
    controller.update_name(id,name)
    controller.update_tags(id,tags,2)

@app.get('/pictures/{id}/show')
async def getpic(id):
    return controller.get_pic(id)

@app.post('/autotag')
async def getpic(file: UploadFile):
    with open(STORAGE+file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        tags = Service.autotag(STORAGE+file.filename)
        os.remove(STORAGE + file.filename)
        return tags


