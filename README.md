# Building Your Own Flows
This repository demonstrates how to use the **Mira SDK** to build and execute custom flows on the Mira Marketplace. It includes an example implementation for creating and managing your own flows, enabling the integration of tailored workflows into your projects. 
Refer to the following [docs](https://docs.mira.network/sdk/building-your-own-flow) to understand the concept even better.
---
## **Features**
- Initialize the Mira SDK client with an API key.
- Build and deploy custom flows to the Mira Marketplace.
- Execute your custom flows with dynamic user input.
- Fetch metadata and manage your custom flows efficiently.
- Securely manage sensitive data using environment variables.
---
## **Prerequisites**
1. **Mira Account**: Ensure you have created an account at [Mira Marketplace](https://console.mira.network/).
2. **API Key**: Generate an API Key from your [Mira Account Dashboard](https://console.mira.network/account/api-keys).
3. **Python**: Ensure you have Python 3.10.0 installed. Currently, `mira-sdk@0.1.8` is compatible with Python 3.10.0.
4. **Dependencies**: Install the required libraries using the steps in the **Setup** section.
---
## **Setup**
### 1. Clone the Repository
```bash
git clone https://github.com/B-Venkatesh7210/building-your-own-flows.git
cd building-your-own-flows
```
### 2. Install Dependencies
```bash
pip install mira-sdk python-dotenv
```
### 3. Configure the API Key
- Create a `.env` file in the root of the project:
  ```bash
  touch .env
  ```
- Add your Mira Marketplace API key to the `.env` file:
  ```plaintext
  API_KEY=your_api_key_here
  ```
### 4. To create a basic flow, you need to define its configuration in a YAML file
- Refer to the following [docs](https://docs.mira.network/sdk/building-your-own-flow).
### 5. Run the Example Scripts
Run the example scripts for creating, executing, and managing your own flows:
```bash
python deploy-flow.py
python execute-flow-local.py
python execute-flow-marketplace.py
```
---
## **Usage**
### Example Input
In the provided examples, you can define the behavior of your custom flow and pass user-specific input for execution. For example:
```python
input_data = {
    "question": "What is the capital of France?",
    "difficulty": "medium"
}
```
### Example Output
The output of the custom flow execution will be printed in the terminal:
```plaintext
{'result': 'The capital of France is Paris.'}
```
---
## **Project Structure**
```plaintext
.
├── flow.yaml                        # A YAML file describing your custom flow
├── deploy-flow.py                   # Script to deploy a custom flow to the marketplace
├── execute-flow-local.py            # Script to test the flow locally
├── execute-flow-marketplace.py      # Script to test the flow from the marketplace
├── .env                             # Environment variables file (not tracked in Git)
├── .env.example                     # Example environment variables file
├── README.md                        # Project documentation
```
---
## **How It Works**
1. The `MiraClient` is initialized with an API key from the `.env` file.
2. The YAML file describes your custom flow.
3. The **Deploy Flow** script demonstrates how to build and deploy a new flow to the marketplace using the Mira SDK.
4. The **Execute Flow** script shows how to execute your deployed flows using user-provided input.
---
## **Dependencies**
- **[mira-sdk](https://pypi.org/project/mira-sdk/)**: To interact with the Mira Marketplace.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: To securely load environment variables.
Install all dependencies with:
```bash
pip install mira-sdk python-dotenv
```
---
## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
---
## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Push the branch and open a pull request.
---
## **Contact**
If you have any questions or feedback, feel free to open an issue or contact [B-Venkatesh7210](https://github.com/B-Venkatesh7210).
