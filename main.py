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
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()
server.login(sender_email, password)

def get_contacts(filename):
    contacts_list = {}
    with open(filename, mode='r', encoding='utf-8') as f: 
        contacts = f.read().split('\n')
        f.seek(0) #look at the beginning of the file. 
        first = f.read() #read the beginning of the file.
        if first == '': #if it's empty, there are no contacts, print error. 
            print('Contacts file is empty.')
            sys.exit() #exit the program
    for item in contacts: 
        contacts_list[item.split(', ')[0]] = item.split(', ')[1:]
    return contacts_list

def read_message(filename):
    with open(filename, mode='r', encoding='utf-8') as template:
        template_content = template.read() #read the contents in the file to a variable
        template.seek(0) #Look at the beginning of the file 
        if template_content == '': # if template is empty. 
            print('Template file is empty.')
            sys.exit() #exit the program.
        subject = template_content.splitlines()[0].rstrip()
        return subject, '\n'.join(template_content.split('\n')[1:])

# Main logic
if __name__ == "__main__":
    contacts = get_contacts('contacts.txt')
    subject, template_content = read_message('message.txt')
    print(contacts)
    print(subject, template_content)

    for contact_mail in list(contacts):
        msg = MIMEMultipart()
        msg_body = template_content.format(*tuple(contacts[contact_mail]))

        msg['From'] = sender_email
        msg['To'] = contact_mail
        msg['Subject'] = subject

        msg.attach(MIMEText(msg_body, 'plain'))
        print(msg)
        server.sendmail(sender_email, contact_mail, msg.as_string())
        print("Sent Successfully!")

    server.quit()
