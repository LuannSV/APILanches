## para rodar o projeto:uvicorn main:app --reload
from fastapi import FastAPI
app = FastAPI()
from auth_routes import auth_router
from order_routes import order_router
app.include_router(auth_router)
app.include_router(order_router)
##endpoint:
#/ordens
#oque vem apos o / é o endpoint


#Rest APIs
#get busca
#post cria
#put modifica
#delete apaga
