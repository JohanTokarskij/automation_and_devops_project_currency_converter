# Currency Converter
## Project description
A simple Flask web application that converts currencies using the [Free Currency API](https://freecurrencyapi.com/). This project focuses on CI/CD aspects of the project, which includes automated testing using GitHub Actions, creating a Docker image and deploying to Azure Web Apps.

## Prerequisites
* Python 3.6+ installed on your machine.
* Git installed for version control.

## Setup
1. Clone the Repository
```bash
git clone https://github.com/JohanTokarskij/automation_and_devops_project_currency_converter
cd https://github.com/JohanTokarskij/automation_and_devops_project_currency_converter
```

2. Create a Virtual Environment
It's recommended to use a virtual environment to manage your project's dependencies.

```bash
python3 -m venv venv
```

3. Activate the Virtual Environment
Activate the virtual environment using the appropriate command for your operating system.

On Windows:
```bash
venv\Scripts\activate
```

On Linux and macOS:
```bash
source venv/bin/activate
```

4. Install Dependencies
Install the required Python packages using requirements.txt.

```bash
pip install -r requirements.txt
```

5. Configure Environment Variables
To securely manage your API key, follow these steps:

**Obtain an API Key**: Sign up at [Free Currency API](https://freecurrencyapi.com/) to obtain your API key.

**Create a .env File**: In the root directory of the project, create a file named .env and add the following line:

```bash
FREE_CURRENCY_API_KEY=<your_api_key_here>
```

Note: Ensure that the .env file is added to your .gitignore to prevent it from being committed to version control.

## Run the Application
Start the Flask application by running:

```bash
python app.py
```

Access the Application
Open your web browser and navigate to http://127.0.0.1:5000/ to use the Currency Converter.

Usage
Select Currencies:

Choose the base currency from the "From" dropdown.
Choose the target currency from the "To" dropdown.
Get Exchange Rate:

Click the "Get Exchange Rate" button to view the current exchange rate between the selected currencies.