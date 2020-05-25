import smtplib
rcvr = "saptarsiroy12@gmail.com"
sender = "chattopadhyaysaranya@gmail.com"
pswd = "24052001"
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender,pswd)
print("Access Granted")
server.sendmail(sender,receiver,str(l))
print("Mail sent!!")