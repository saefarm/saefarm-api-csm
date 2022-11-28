import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.farmland import farmland_router

api = FastAPI()

origins = [
    "http://127.0.0.1:8501"  # Streamlit
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api.include_router(farmland_router.router)


if __name__ == "__main__":
    uvicorn.run("main:api", reload=True)
