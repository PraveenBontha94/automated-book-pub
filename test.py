'''import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCBVjMu0TDawDCCMjtOiHLosbjiA1K0G2E")

model = genai.GenerativeModel("gemini-1.5-flash")
print(model.generate_content("Define AI.").text)
'''
import openai

openai.api_key = "a083f657d0e087535effc17a3123afda72af0466de229b2615c78efbe2625032"
openai.api_base = "https://api.together.xyz/v1"

response = openai.ChatCompletion.create(
    model="meta-llama/Llama-3-70b-chat-hf",
    messages=[
        {"role": "user", "content": "Define AI."}
    ],
    temperature=0.7,
)

print(response['choices'][0]['message']['content'])
