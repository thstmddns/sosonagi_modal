from fastapi import FastAPI
from pydantic import BaseModel
from utils import *
from fastapi.middleware.cors import CORSMiddleware

#  iniitialize fast api
app = FastAPI


# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용. 실제 배포 시에는 필요한 도메인만 허용해야 합니다.
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)
tokenizer, model, device = initializeModels() 

class classifyInput(BaseModel):
    classyfy : list

@app.post("/classify")
async def classify(input : classifyInput):
    cInput = 