# from turtle import register_shape
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

users={
    1:{  
        "name":"Ritesh",
        "loc":"Mumbai",
        "desc":"Awesome"
    },
    2:{  
        
        "name":"Ameer",
        "loc":"Dubai",
        "desc":"2nd yr"
    }
}
@app.get('/')
def index():
    return "hey Ritesh"

@app.get('/getuser/{id}')
def myfirst(id: int):
    result=users[id]
    return result  


class Person(BaseModel):
        id:int
        name: str
        loc: str
        desc: Optional[str]
  
@app.post('/postuser')
def personPost(request:Person):
    users[request.id]=request
    print(users)
    return{f"user no.{request.id}  is created"}  


@app.put('/putuser/{id}')  
def personPut(id : int):
    users[id]=None
    print(users)
    return{f" null user with id {id} is created"}
      