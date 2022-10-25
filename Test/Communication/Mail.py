#devautowayne@gmail.com
#mrxntmwqnpqolowe

import smtplib #importing the module

class Mail:
    def __init__(self, sender_add, password):
        self.sender_add= sender_add #storing the sender's mail id
        self.password = password #storing the password to log in
        self.smtp_server=smtplib.SMTP("smtp.gmail.com",587)

    def connect(self):
        self.smtp_server.ehlo() #setting the ESMTP protocol
        self.smtp_server.starttls() #setting up to TLS connection
        self.smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
        self.smtp_server.login(self.sender_add,self.password) #logging into out email id

    def send(self, receiver_add, message):
        self.connect()
        msg_to_be_sent =message

        #sending the mail by specifying the from and to address and the message 
        self.smtp_server.sendmail(self.sender_add,receiver_add,msg_to_be_sent)
        print('Message sent') #priting a message on sending the mail

        self.smtp_server.quit()#terminating the server