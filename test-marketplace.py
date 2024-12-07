from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "0.0.1"
input_data = {"question": "What does Agglayer do, and what is its future vision?"}

# If no version is provided it'll use latest version by default
if version:
	flow_name = f"venmus/polygon-stack/{version}"
else:
	flow_name = "venmus/polygon-stack"

result = client.flow.execute(flow_name, input_data)
print(result)