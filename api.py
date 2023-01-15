from fastapi import FastAPI, File, UploadFile
from PhotorazeController import Controller, STORAGE
import shutil
app = FastAPI(
    title='photoraze-stock'
)
controller = Controller()


@app.get('/')
def mainpage():
    return 'hello'


@app.get('/pictures')
def allpics():
    return controller.get_pics()


@app.get('/pictures/{id}/delete')
def show(id):
    return controller.delete(id)

@app.put('/addpic/')
def addpic(file: UploadFile):
    with open(STORAGE+file.filename,'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        controller.add_pic(file.filename)