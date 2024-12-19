from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

flow = Flow(source="flow.yaml")

input_dict = {"topic": "Hard Life", "style": "Lil Wayne"}

response = client.flow.test(flow, input_dict)

print(response)