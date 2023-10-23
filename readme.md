# TOTP Generator API

## Introduction

This is a simple TOTP (Time-based One-Time Password) generator API built using Flask and the `pyotp` library. It allows users to setup accounts with a secret key for two-factor authentication and retrieve TOTP codes for those accounts.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Martzyx/totp-api
    cd your-repository-directory
    ```

2. **Install necessary packages:**

    ```bash
    pip install Flask pyotp
    ```

3. **Run the application:**
    ```bash
    python app.py
    ```
    The application will start, and you can access it at `http://127.0.0.1:5000`.

## Usage

### Setup Account

To set up an account, make a POST request to the `/setup` endpoint with a JSON payload containing the username and secret key.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "secret": "your_secret_key"}' http://127.0.0.1:5000/setup
```

### Get TOTP Code

To retrieve the TOTP code for a specific account, make a GET request to the `/get-totp/<username>` endpoint.

```bash
curl http://127.0.0.1:5000/get-totp/your_username
```

## Security Notice

-   This application is a basic demonstration and not suitable for production use as it lacks essential security measures.
-   Secrets should be stored securely, with encryption, in a production environment.
-   Implement proper authentication mechanisms to secure the API endpoints.
-   Make sure to use HTTPS to encrypt data transmitted between the client and server.
