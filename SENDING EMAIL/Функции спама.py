import sendgrid
from sendgrid import Mail,Email,Content
sendgrid_api_key = "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"
SUBJECT = "SMS"
sg = sendgrid.SendGridAPIClient(sendgrid_api_key)


strings = ['Hello Emma it"s Mark how are u, i need your help!',
           'Hello Marty it"s Mark how are u, i need your help!',
          'Hello Mark it"s Mark how are u, i need your help!',
          'Sales! Li-ning sales!','Buy Right now',
           'Hello Emma, how do u do?Im gonna invite u to restaurant',
           'Hello Emma how are u? Have a nice day',
           'EMMA SOS!!! Production is down','Sales in Nike shop',
           'Emma hello, help me pls',
           'Hi Emma, its Marty McFly i want invite u to time-travel',
           'Hi, Emma, please, need to meet'
          ]
def function1(strings):
    for i in strings:
       with open("ВЕСЬ СПИСОК.txt","a") as file1:
            file1.write(i.lower() + "\n")\

function1(strings)


def filtration():
    with open("ВЕСЬ СПИСОК.txt", "r") as file2:
        var = file2.readlines()
        for sentence in var:
            print(var,end="")
            if sentence.startswith("sales") or sentence.startswith("buy right now"):
                with open("СПАМ.txt", "a") as file3:
                    file3.write(sentence)
            elif "emma" in sentence and "help" not in sentence and "sos" not in sentence:
                with open("Личные.txt", "a") as file4:
                    file4.write(sentence)
            elif "help" in sentence or "sos" in sentence or "dear" in sentence:
                with open("Рабочие.txt", "a") as file5:
                    file5.write(sentence)

filtration()



def sendgrid_emma():
        with open("Личные.txt", "r") as file6:
            emma_list = file6.readlines()
            for line in emma_list:
                body = line
                message = Mail(
                    from_email="almazbekovbaistan@gmail.com",
                    to_emails="emma.apigrid@gmail.com",
                    subject=SUBJECT,
                    plain_text_content=body
                )
                response = sg.send(message)

sendgrid_emma()


def sendgrid_stev():
    with open("Рабочие.txt", "r") as file7:
        steven_list = file7.readlines()
        for line1 in steven_list:
            body = line1
            message = Mail(
                from_email="almazbekovbaistan@gmail.com",
                to_emails="maximneveraa@gmail.com",
                subject=SUBJECT,
                plain_text_content=body
            )
            response = sg.send(message)


sendgrid_stev()
