from langchain_core.prompts import ChatPromptTemplate
def build_prompt():
    return ChatPromptTemplate.from_template("""
Generate ONLY valid FastAPI Python code.
STRICT RULES:
- Output ONLY Python code
- No explanation
- Must include: app = FastAPI()
- Must run directly using: uvicorn
- No undefined variables
- No YAML reading inside generated code
--------------------------------------------------
SETUP:
- Use pandas to read CSV
- File name: StudentsPerformance.csv
- Clean columns:
    - replace spaces with _
    - convert to lowercase
--------------------------------------------------
CORS (MANDATORY):
- Must include:
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
--------------------------------------------------
ENDPOINTS (ALL REQUIRED):
1. GET /
   - Return:
     {{ "message": "API is running" }}
-------------------------------------------------
2. GET /load-data
   - Load CSV using pandas
   - Store in memory (global variable)
   - Return:
     {{ "message": "Data loaded successfully" }}
--------------------------------------------------
3. GET /students
   - Return full dataset
   - If data not loaded, load automatically
--------------------------------------------------
4. GET /scores
   - Extract:
     math_score
     reading_score
     writing_score
   - Calculate:
     avg_math_score
     avg_reading_score
     avg_writing_score
   - Return JSON:
     {{
        "avg_math_score": 0,
        "avg_reading_score": 0,
        "avg_writing_score": 0,
        "scores": []
     }}
--------------------------------------------------
IMPORTANT:
- Use pandas properly
- Use global variable for storing dataset
- Ensure no crash if API called before loading data
- All endpoints must work independently
- No missing imports
- No syntax errors
--------------------------------------------------
OUTPUT:
ONLY Python code
""")

