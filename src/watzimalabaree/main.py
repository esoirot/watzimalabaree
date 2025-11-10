from fastapi import FastAPI
from watzimalabaree import malabaree, ovazlabaree

app = FastAPI(title="Watzimalabaree Personal Library Manager")

app.include_router(malabaree.router)
app.include_router(ovazlabaree.router)

@app.get("/")
def root():
    return  {"Welcome to Watzimalabaree": "Your personal Library assistant !"}
