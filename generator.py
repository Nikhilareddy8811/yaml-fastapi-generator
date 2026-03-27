import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompt_builder import build_prompt

def generate_code():
    print("🚀 Generating code using LLM...")

    # Load YAML
    with open("api.yaml", "r") as f:
        yaml_data = f.read()

    # LLM setup
    llm = ChatGroq(
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"   # ✅ updated model
    )

    prompt = build_prompt()

    chain = prompt | llm | StrOutputParser()

    # Generate
    response = chain.invoke({"yaml": yaml_data})

    # 🔥 CLEAN OUTPUT (VERY IMPORTANT)
    code = response.strip()

    # Remove markdown if present
    if "```" in code:
        code = code.split("```")[1]
        if code.startswith("python"):
            code = code.replace("python", "", 1)

    # Save file
    with open("generated_api.py", "w") as f:
        f.write(code)

    print("✅ CLEAN GENERATED API SAVED!")

if __name__ == "__main__":
    generate_code()
