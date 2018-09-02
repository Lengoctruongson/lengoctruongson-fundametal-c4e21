from datetime import datetime
now = datetime.now()
print(now.day,"/", now.month,"/", now.year,": ", now.hour,"h ", now.minute,"' ", now.second,"s", sep="")