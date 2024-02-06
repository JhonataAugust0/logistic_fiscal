import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from application.adapters.HTTP.routes.tag_route import TagRoute

app = FastAPI(
    title="logistic_fiscal",
    version="1.0.0",
    openapi_url="/v1/openapi.json"
)

origins = ["*"]
tag_route = TagRoute()
app.include_router(tag_route.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
