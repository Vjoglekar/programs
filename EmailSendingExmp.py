import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'vjoglekar81@gmail.com'
PASSWORD = 'varuntheswift'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(name,filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    temp1 = template_file_content.split(',')[0]
    temp2 = template_file_content.split(',')[1]
    template_file_content = temp1 + ' ' + name + '\n' + temp2
    print(template_file_content)

    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    
    # set up the SMTP server
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.ehlo()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        message_template = read_template(name,'message.txt')

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
