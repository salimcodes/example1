
import os
from dotenv import load_dotenv
load_dotenv()
app_api_key = os.getenv("api_key")


OpenAI.ChatCompletion.create(OpenAI_Key, model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
print(OpenAI_Key)