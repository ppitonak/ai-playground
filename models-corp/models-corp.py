import os
import httpx
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI

load_dotenv()

http_client = httpx.Client(
    verify=False
)

llm = OpenAI(
    openai_api_key=os.getenv("MODELS_CORP_API_KEY"),
    openai_api_base=os.getenv("MODELS_CORP_API_URL") + "/v1",
    model_name=os.getenv("MODELS_CORP_MODEL"),
    model_kwargs={"stop": ["."]},
    http_client=http_client,
)
print(llm.invoke("Bratislava is"))