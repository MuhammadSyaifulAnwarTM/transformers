import os
from vllm import LLM, SamplingParams

def main():
    model_name = os.getenv("MODEL_NAME", "facebook/opt-125m")
    llm = LLM(model=model_name, tensor_parallel_size=1)
    # Serving logic for cloud deployment

# Optimized for high-throughput cloud inference pipelines