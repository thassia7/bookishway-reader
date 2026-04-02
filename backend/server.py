## 🎉 Ótimo! Vamos para o próximo!

---

## 📄 Arquivo 2: `backend/server.py`

Este é o arquivo principal do backend. É **grande**, mas é só copiar e colar!

### **1. Criar novo arquivo:**

- Clicar em **"Add file"** → **"Create new file"**
- Nome: `backend/server.py`

### **2. Colar este conteúdo:**
Action: file_editor view /app/backend/server.py
Observation: [Showing lines 1-50 of 414 total] /app/backend/server.py:
1|from fastapi import FastAPI, APIRouter, HTTPException, Request
2|from dotenv import load_dotenv
3|from starlette.middleware.cors import CORSMiddleware
4|from motor.motor_asyncio import AsyncIOMotorClient
5|import os
6|import logging
7|from pathlib import Path
8|from pydantic import BaseModel, Field, ConfigDict
9|from typing import List, Optional
10|import uuid
11|from datetime import datetime, timezone
12|import httpx
13|import urllib.parse
14|
15|# Load environment variables FIRST
16|ROOT_DIR = Path(__file__).parent
17|load_dotenv(ROOT_DIR / '.env')
18|
19|# Import auth functions and routes
20|from auth import seed_admin, get_current_user
21|from auth_routes import create_auth_router
22|
23|# MongoDB connection
24|mongo_url = os.environ['MONGO_URL']
25|client = AsyncIOMotorClient(mongo_url)
26|db = client[os.environ['DB_NAME']]
27|
28|# Create the main app without a prefix
29|app = FastAPI()
30|
31|# Create a router with the /api prefix
32|api_router = APIRouter(prefix="/api")
33|
34|# Define Models
35|class VocabWord(BaseModel):
36|    model_config = ConfigDict(extra="ignore")
37|    word: str
38|    part_of_speech: str
39|    definition: str
40|
41|class Chapter(BaseModel):
42|    model_config = ConfigDict(extra="ignore")
43|    id: str
44|    chapter_num: int
45|    title: str
46|    content: str
47|    vocab_list: List[VocabWord] = []
48|    quiz_questions: Optional[List[dict]] = []
49|    reflection_questions: Optional[List[str]] = []
50|
 [50 lines shown. Remaining: lines 51-414 (364 lines). Use view_range parameter to continue.]
