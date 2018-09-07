import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("leson1871995@gmail.com", "mountain1871995")

msg = "YOUR MESSAGE!"
server.sendmail("leson1871995@gmail.com", "truongsonle18@gmail.com", msg)
server.quit()