from transformers import pipeline
import torch

# Check if CUDA is available
print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))

# set device=0 to use GPU
model = pipeline(task="summarization", model="facebook/bart-large-cnn", device="cpu")
response = model("text to summarize")
print(response)