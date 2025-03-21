import os
from dotenv import load_dotenv
from langchain_community.llms import VLLMOpenAI

load_dotenv()

llm = VLLMOpenAI(
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    openai_api_base=os.getenv("DEEPSEEK_API_URL") + "/v1",
    model_name=os.getenv("DEEPSEEK_MODEL"),
    model_kwargs={"stop": ["."]},
)
print(llm.invoke("Poprad is"))