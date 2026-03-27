
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to store dataset
data = None

# Load data from CSV
def load_data():
    global data
    try:
        data = pd.read_csv('StudentsPerformance.csv')
        data.columns = data.columns.str.replace(' ', '_').str.lower()
        return {"message": "Data loaded successfully"}
    except Exception as e:
        return {"message": str(e)}

# Endpoint to load data
@app.get("/load-data")
async def load_data_endpoint():
    return load_data()

# Endpoint to get full dataset
@app.get("/students")
async def get_students():
    global data
    if data is None:
        return load_data()
    return data.to_dict(orient='records')

# Endpoint to get scores
@app.get("/scores")
async def get_scores():
    global data
    if data is None:
        return load_data()
    scores = data[['math_score', 'reading_score', 'writing_score']].values.tolist()
    avg_math_score = data['math_score'].mean()
    avg_reading_score = data['reading_score'].mean()
    avg_writing_score = data['writing_score'].mean()
    return {
        "avg_math_score": avg_math_score,
        "avg_reading_score": avg_reading_score,
        "avg_writing_score": avg_writing_score,
        "scores": scores
    }

# Endpoint to check API status
@app.get("/")
async def root():
    return {"message": "API is running"}
