from typing import Union
from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from transliter import *

app = FastAPI()

@app.get("/")
async def homepage():
	return JSONResponse({'Hello': 'world'})

@app.get("/calc")
async def calc(a, b):
	result = int(a)+int(b)
	print('here')
	return JSONResponse({'Hello': F'={result}'})

@app.get("/translit")
async def translit(text):
	result = transform_word(text)
	print('here')
	return JSONResponse({'result': F'{result}'})

@app.get("/caps")
async def caps_lock(text):
	result = text.lower()
	return JSONResponse({'result': F'{result}'})

@app.get("/counter")
async def counter(text):
	result = text.lower()
	return JSONResponse({'result': F'{result}'}) #Этот метод будет считать количество каждой из букв в тексте
# text: "aa bb cc dd eeee"
#
#     {
#         a: 2
#         b: 2
#         c: 2
#         d: 2
#         e: 4
#     }

