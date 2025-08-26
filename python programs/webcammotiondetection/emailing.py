import smtplib
import imghdr

from email.message import EmailMessage

password="hasu mhen drfv utcf"

def send_email(image_path):
    email_mssage=EmailMessage()
    email_mssage["Subject"]="new person"
    email_mssage.set_content("i just saw a new person!")

    with open(image_path,"rb") as file:
        content=file.read()
    email_mssage.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("archiettanwar71@gmail.com",password)
    gmail.sendmail("archiettanwar712gmail.com","archiettanwar71@gmail.com",email_mssage.as_string())
    gmail.quit()

if __name__=="__main__":
    send_email(image_path="images/29.png")
