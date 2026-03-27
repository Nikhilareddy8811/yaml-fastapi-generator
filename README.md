# 🚀 YAML to FastAPI Code Generator using Generative AI

## 📌 Overview
This project demonstrates an automated system that converts a YAML configuration file into a fully functional FastAPI backend using Generative AI (LLM).

The system dynamically generates API endpoints, processes data from a CSV dataset, and provides a frontend dashboard for visualization.

---

## 🎯 Objectives
- Automate backend API generation using YAML
- Use LLM for dynamic code generation
- Build scalable FastAPI applications
- Integrate frontend dashboard for visualization
- Perform data analysis via APIs

---

## 🛠️ Technologies Used
- Python
- FastAPI
- Pandas
- YAML
- HTML, CSS, JavaScript
- Uvicorn
- LangChain / Open-source LLM

---

## ⚙️ System Workflow
1. User provides YAML configuration  
2. Prompt builder creates structured prompt  
3. LLM generates FastAPI code  
4. Generated API is saved and executed  
5. Frontend interacts with APIs  
6. Data is displayed on dashboard  

---

## 📂 Project Structure
yaml_test/
│── api.yaml
│── app.py
│── generator.py
│── prompt_builder.py
│── generated_api.py
│── frontend.html
│── StudentsPerformance.csv
│── requirements.txt
│── students.db


---

## 📌 YAML Configuration Example
```yaml
api:
  title: Student API

data:
  source: StudentsPerformance.csv

endpoints:
  - name: students
    path: /students
    type: full_data

  - name: scores
    path: /scores
    type: selected_columns
    columns:
      - math score
      - reading score
      - writing score

🖼️ Project Visuals
🔹 YAML Configuration

🔹 LLM Prompt

🔹 API Output - Students

🔹 API Output - Scores

🔹 Dashboard


🔗 API Endpoints
| Endpoint     | Method | Description                         |
| ------------ | ------ | ----------------------------------- |
| `/load-data` | GET    | Loads dataset                       |
| `/students`  | GET    | Returns full dataset                |
| `/scores`    | GET    | Returns selected columns + averages |
| `/`          | GET    | Health check                        |


▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Generate API
python generator.py
3. Run server
python app.py
4. Open Swagger UI
http://127.0.0.1:8000/docs


🔐 Security Note
.env file is excluded using .gitignore
API keys are not pushed to GitHub
