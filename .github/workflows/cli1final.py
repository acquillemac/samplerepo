
import click
import requests
import json

# URL for Artifactory API 
ARTIFACTORY_URL = "https://trialnv45ts.jfrog.io/artifactory/api/pypi/my_cli_project"

#variable to store the API token from user login
api_token = None  

# function to authenticate with username/password and retrieve API token
def authenticate(username, password):
    url = f"{ARTIFACTORY_URL}/api/security/token"
    data = {
        'username': username,
        'password': password,
        'grant_type': 'password'
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        click.echo("Authentication failed. Check your username/password.")
        exit(1)

# API requests with the token
def make_api_request(endpoint, method="GET", data=None):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    
    url = f"{ARTIFACTORY_URL}{endpoint}"

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=json.dumps(data))
    elif method == "PUT":
        response = requests.put(url, headers=headers, data=json.dumps(data))
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)
    
    if response.status_code in range(200, 299):
        return response.json()
    else:
        click.echo(f"Error: {response.status_code} - {response.text}")
        exit(1)

# Command to ping the system
@click.command()
def ping():
    """Ping the Artifactory system."""
    result = make_api_request("/api/system/ping")
    click.echo(result)

# Command to get system version
@click.command()
def version():
    """Get the Artifactory system version."""
    result = make_api_request("/api/system/version")
    click.echo(result)

# Command to create a new user
@click.command()
@click.argument('username')
@click.argument('password')
@click.argument('email')
def create_user(username, password, email):
    """Create a new user in Artifactory."""
    data = {
        "name": username,
        "password": password,
        "email": email
    }
    result = make_api_request("/api/security/users", method="POST", data=data)
    click.echo(result)

# Command to delete a user
@click.command()
@click.argument('username')
def delete_user(username):
    """Delete an existing user."""
    result = make_api_request(f"/api/security/users/{username}", method="DELETE")
    click.echo(result)

# Command to get storage info
@click.command()
def storage_info():
    """Get Artifactory storage information."""
    result = make_api_request("/api/storageinfo")
    click.echo(result)

# Command to create a repository
@click.command()
@click.argument('repo_key')
@click.argument('repo_type')
def create_repo(repo_key, repo_type):
    """Create a repository."""
    data = {
        "rclass": "local",
        "packageType": repo_type
    }
    result = make_api_request(f"/api/repositories/{repo_key}", method="POST", data=data)
    click.echo(result)

# Command to update a repository
@click.command()
@click.argument('repo_key')
@click.argument('repo_type')
def update_repo(repo_key, repo_type):
    """Update an existing repository."""
    data = {
        "rclass": "local",
        "packageType": repo_type
    }
    result = make_api_request(f"/api/repositories/{repo_key}", method="PUT", data=data)
    click.echo(result)

# Command to list repositories
@click.command()
def list_repos():
    """List all repositories."""
    result = make_api_request("/api/repositories")
    click.echo(result)

# Main CLI entry point
@click.group()
def cli():
    """Artifactory CLI to interact with your Artifactory SaaS instance."""
    pass

.......................

# CLI entry point to start the program
if __name__ == '__main__':
    cli()

