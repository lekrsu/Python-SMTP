import yagmail
receiver=""
body=""
mailsender=input("Enter Email to send from: ")

def get_emails():
    emails = []
    with open('emails.txt') as my_file:
        for line in my_file:
            emails.append(line)
    i = 0
    formatted_emails=[]
    for i in emails:
        formatted_emails.append(i.strip())

    i = 0
    while i < len(formatted_emails):
        receiver = formatted_emails[i]
        i += 1
    get_emails.formatted_emails = formatted_emails


def get_keys():
    keys = []
    with open('keys.txt') as key_file:
        for line in key_file:
            keys.append(line)
    i = 0
    formatted_keys=[]
    for i in keys:
        formatted_keys.append(i.strip())

    i = 0
    while i < len(formatted_keys):
        receiver = formatted_keys[i]
        i += 1
    get_keys.formatted_keys = formatted_keys

def send_mail():
    i = len(get_emails.formatted_emails) - 1
    while i > -1:

        receiver = get_emails.formatted_emails[i]
        sent_keys = get_keys.formatted_keys[i]
        print(str(i) + " " + str(receiver) + " " + str(sent_keys))
        filename = "document.pdf"
        yag = yagmail.SMTP(mailsender)
        yag.send(
            to=receiver,
            subject="Ai-Onic key",
            contents="Grattis du vann utlottningen! Här är din nyckel till steam: " + sent_keys + ". Tack för du var med!", 
            # attachments=filename,
        )
        i += -1 
    else:
        print("Done.")
        exit

get_emails()
get_keys()
send_mail() 
