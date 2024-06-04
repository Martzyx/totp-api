# TOTP Generation for Software Implementation Teams

## Purpose and background
In software implementation teams, like I am in, we often need to set up 2FA for many backends. With these scripts, we can input a secret key to get the TOTP (time-based one-time password). This is in contrast to each member of the team using private apps to store and retrieve TOTPs.


## Simple TOTP Generation Using Python Script

### Introduction

This is a straightforward Python script that allows you to generate TOTP codes locally on your machine. This method is ideal for quick tests or for those who prefer a more direct approach without the need for API calls.

### Usage

1. **Navigate to the Script Directory:**

   Ensure you're in the directory containing the Python script for TOTP generation.

2. **Run the Python Script:**

   You can generate a TOTP code by running the script and providing your secret key as an input. Use the following command in your terminal:

    ```bash
    python generate_totp.py
    ```

3. **Input Your Secret Key:**

   When prompted, enter the secret key for which you want to generate the TOTP code.

    ```
    Enter your secret key: [Your_Secret_Key]
    ```

   After entering the secret key, the script will display the TOTP code.

### Note:

- This script requires the `pyotp` library. Ensure that you have installed it using the command `pip install pyotp`.
- The TOTP code generated is valid only for a short period (usually 30 seconds). Make sure to use it within this timeframe.


## TOTP Generator API

### Introduction

This is a simple TOTP (Time-based One-Time Password) generator API built using Flask and the `pyotp` library. It allows users to setup accounts with a secret key for two-factor authentication and retrieve TOTP codes for those accounts.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/martzyx/totp-api
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

### Usage

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

### Security Notice

-   This application is a basic demonstration and not suitable for production use as it lacks essential security measures.
-   Secrets should be stored securely, with encryption, in a production environment.
-   Implement proper authentication mechanisms to secure the API endpoints.
-   Make sure to use HTTPS to encrypt data transmitted between the client and server.

### Useful links

- https://totp.danhersam.com/
