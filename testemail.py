import email
import smtplib 

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUREMAIL@gmail.com", "YOURPASSWORD")
 
msg = "MY CAR RUNS ON FUEL NOT FRIENDSHIP"
server.sendmail("YOUREMAIL", "FRIENDEMAIL", msg)
server.quit()