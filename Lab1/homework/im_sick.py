from gmail import GMail, Message
from datetime import datetime

mail = GMail("leson1871995", "mountain1871995")
msg = Message("Boss - Xin nghi om", to="truongsonle18@gmail.com", text="Em bi om anh oi")

while True:
    now = datetime.now()
    if now.hour == 7:
        mail.send(msg)
        break