from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts.prompt import PromptTemplate

#  model="mistralai/Mistral-7B-Instruct-v0.1",
model = pipeline(task="text-generation",
                 model="unsloth/DeepSeek-V3-0324-GGUF",
                 max_length=256,
                 truncation=True
        )

llm = HuggingFacePipeline(pipeline=model)

# Create a prompt template
template = PromptTemplate.from_template("Explain {topic} in detail for a {age} year old to understand.")

chain = template | llm
topic = input("Topic: ")
age = input("Age: ")

response = chain.invoke({"topic": topic, "age": age})
print(response)