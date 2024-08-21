#imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setting up credentials from the .env file
sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Set up the SMTP server/connection
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        
        def get_contacts(filename):
            contacts_list = {}
            with open(filename, mode='r', encoding='utf-8') as f: 
                contacts = f.read().splitlines()  # Split lines instead of '\n'
                if not contacts:  # If file is empty
                    print('Contacts file is empty.')
                    sys.exit()
            for item in contacts:
                if item.strip():  # Skip any empty lines
                    parts = item.split(', ')
                    if len(parts) < 2:
                        print(f"Skipping invalid contact entry: {item}")
                        continue
                    contacts_list[parts[0]] = parts[1:]
            return contacts_list

        def read_message(filename):
            with open(filename, mode='r', encoding='utf-8') as template:
                template_content = template.read() # Read the file contents
                if not template_content.strip():  # If template is empty
                    print('Template file is empty.')
                    sys.exit()
                subject = template_content.splitlines()[0].rstrip()
                return subject, '\n'.join(template_content.split('\n')[1:])
        
        # Main logic
        if __name__ == "__main__":
            contacts = get_contacts('contacts.txt')
            subject, template_content = read_message('message.txt')
            print(contacts)
            print(subject, template_content)
            
            for contact_mail in contacts:
                msg = MIMEMultipart()
                contact_details = tuple(contacts[contact_mail])

                try:
                    msg_body = template_content.format(*contact_details)
                except IndexError:
                    print(f"Error: Not enough data provided for {contact_mail}. Skipping...")
                    continue

                msg['From'] = sender_email
                msg['To'] = contact_mail
                msg['Subject'] = subject

                msg.attach(MIMEText(msg_body, 'plain'))
                print(f"Sending email to {contact_mail}...")
                server.sendmail(sender_email, contact_mail, msg.as_string())
                print("Sent Successfully!")

except smtplib.SMTPException as e:
    print(f"Failed to send email: {e}")
