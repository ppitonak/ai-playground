from transformers import pipeline
from transformers.utils.logging import set_verbosity_error
import torch

# Don't print useless messages
set_verbosity_error()

# Check if CUDA is available
print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))

# set device=0 to use GPU
model = pipeline(task="summarization", model="unsloth/DeepSeek-V3-0324-GGUF", device="cpu")
response = model("text to summarize")
print(response)
