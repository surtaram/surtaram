import json
import logging
import pytest
import os
from dotenv import set_key
from config.api_config import ApiUrls
from restclient import apiclient
from utils.requests_payload import SimpleBookApiRequests


# Add command-line options to pytest
def pytest_addoption(parser):
    """Add custom command-line options for pytest."""
    parser.addoption("--host", action="store", default="staging")


# Update environment configuration in endpoints.json based on the host option
def update_env(config):
    """Update the environment configuration in endpoints.json."""
    with open("config/endpoints.json") as jsonFile:
        data = json.load(jsonFile)
        # Set the environment to the value provided via command-line option
        data['environment']['env'] = config.getoption("--host").lower()
        jsonFile.close()


# Hook into pytest configuration to apply custom settings
@pytest.hookimpl
def pytest_configure(config):
    """Hook that is called to configure pytest."""
    update_env(config)


# Fetch authentication token from the API
def fetch_auth_token():
    """Fetch the auth token from the API."""
    headers = {
        "Content-Type": "application/json"
    }
    # Make a POST request to obtain the auth token
    response = apiclient.post_request(ApiUrls.url_get_auth(), None, SimpleBookApiRequests.AUTH_TOKEN, headers)

    # Check for successful response and return the access token
    if response.status_code == 201:
        return response.json()['accessToken']
    else:
        raise Exception(f"Error fetching token: {response.status_code} - {response.text}")


# Save the fetched token to a .env file
def save_token_to_env(token):
    """Save the token to .env file."""
    env_file = '.env'
    # Check if the .env file exists
    if os.path.exists(env_file):
        set_key(env_file, 'AUTH_TOKEN', token)  # Update existing file
    else:
        # Create a new .env file and write the token
        with open(env_file, 'w') as f:
            f.write(f'AUTH_TOKEN={token}\n')


# Fixture to fetch the auth token before any tests run
@pytest.fixture(scope='session', autouse=True)
def auth_token():
    """Fixture to fetch the auth token before any tests run."""
    token = fetch_auth_token()  # Fetch token
    save_token_to_env(token)  # Save token to .env
    yield token  # Provide the token to tests


# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Fixture to set up logging for each test
@pytest.fixture(autouse=True)
def setup_logging():
    """Fixture to set up logging for each test."""
    logger.info("Starting a new test.")  # Log the start of the test
    yield  # Run the test
    logger.info("Finished the test.")  # Log the end of the test
