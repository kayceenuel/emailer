# Email Sender Script

This is a simple Python script for sending personalized emails to a list of contacts using Gmail's SMTP server. The script supports the use of environment variables for storing sensitive information like email credentials.

## Features

- Sends emails to multiple contacts listed in a `contacts.txt` file.
- Uses a customizable email template from a `message.txt` file.
- Supports placeholders in the template for personalized content.
- Credentials are loaded securely from a `.env` file.
- Basic error handling for missing data and invalid contact entries.

## Requirements

- Python 3.x
- `smtplib` (built-in Python library)
- `python-dotenv` (to load environment variables)

## Installation__+

1. Clone this repository:
    ```bash
    git clone https://github.com/kayceenuel/emailer.git
    cd emailsender
    ```

2. Install the required Python package:
    ```bash
    pip install python-dotenv
    ```

3. Create a `.env` file in the project directory and add your Gmail credentials:
    ```plaintext
    EMAIL=your-email@gmail.com
    PASSWORD=your-app-password
    ```

4. Prepare your `contacts.txt` file with the email addresses and personalized data:
    ```plaintext
    recipient1@example.com, Name1, AdditionalData1
    recipient2@example.com, Name2, AdditionalData2
    ```

5. Create your `message.txt` file with the email subject and body:
    ```plaintext
    Subject Line Here

    Dear {0},

    Your personalized message goes here. Your additional data: {1}.

    Best regards,
    Your Name
    ```

## Usage

Run the script with Python:

```bash
python main.py