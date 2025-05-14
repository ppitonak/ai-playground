import os
import httpx
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain_core.prompts.prompt import PromptTemplate

load_dotenv()

http_client = httpx.Client(
    verify=False
)

with open('pipelines_0_65_0_to_0_65_7_git.log') as f: log_file = f.read()

# We should probably filter out line starting with Author, Date and those containing Signed-off-by

model = OpenAI(
    openai_api_key=os.getenv("MODELS_CORP_API_KEY"),
    openai_api_base=os.getenv("MODELS_CORP_API_URL") + "/v1",
    model_name=os.getenv("MODELS_CORP_MODEL"),
    http_client=http_client,
)

template = """
Create a human-readable change log for these git commits. Create separate categories for new features, bug fixes, dependency updates, and CI changes. 
Include 8-character commit digest in every bullet point, skip contributors. Explicitly mention breaking changes if there are some.

{git_log}
"""
prompt = PromptTemplate.from_template(template)
chain = prompt | model

response = chain.invoke({"git_log": log_file})
print(response)
