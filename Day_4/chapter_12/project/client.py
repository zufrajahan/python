# In your terminal, first run:
# pip install openai

# Install OpenAI if not installed: pip install openai

from openai import OpenAI

# Directly assigning the API key (not recommended for production use)
client = OpenAI(
    api_key="xai-dBu619gILUIlImhxkpBV2Q5Hc4efyEt6CUZmbJ1SUetk1685PS0J4vYq6M5N6An2l5lCheXOh3PhMEKk",
    base_url="https://api.x.ai/v1",
)

# Sending a request
completion = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."},
        {"role": "user", "content": "What is the meaning of life, the universe, and everything?"},
    ],
)

# Printing the response
print(completion.choices[0].message.content)
