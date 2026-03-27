import subprocess
import sys

print("🚀 Generating APIs...")
subprocess.run([sys.executable, "generator.py"])

print("🚀 Starting server...")
subprocess.run([
    sys.executable, "-m", "uvicorn",
    "generated_api:app",
    "--reload"
])