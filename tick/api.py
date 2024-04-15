import uvicorn
from fastapi import FastAPI


app = FastAPI(title='Tick API')


@app.get("/")
def get_all_operators():
    raise NotImplementedError()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
