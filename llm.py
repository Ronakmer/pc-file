import os
import openai
from langchain.llms import OpenAI

api_key = "sk-proj-Fvh8PJbHyDOjwikYwXv6T3BlbkFJafedzKL0v9U6YrtMH4Cj"

# Initialize OpenAI LLM with the GPT-4o model
llm = OpenAI(openai_api_key=api_key, model="gpt-4o-2024-05-13", temperature=0.3)

# Use the LLM to predict
print(llm.predict("what is the capital of India?"))














# Retrying langchain.llms.openai.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised RateLimitError: You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors..
