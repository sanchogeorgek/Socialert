# Import smtplib for the actual sending function

import smtplib

class emailimg:

    def emailwithimg(self,IncType,Location,AEName,AEemail,Polcount,InsValue):

        # Email-Socialert Package Modules
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage

        # Email-Socialert Addresses Inputs
        strFrom = 'socialerttravelers@gmail.com'
        strTo = AEemail

        #Incident Type
        Incident = IncType
        Location = Location
        AE =AEName
        PolCnt =Polcount
        InsAmt = InsValue

        # Create the root message and fill in the from, to, and subject headers
        msg = MIMEMultipart('multipart')
        msg['Subject'] = Incident +' ' + "Alert!!!"
        msg['From'] = strFrom
        msg['To'] = strTo

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)

        # Msg Text Part
        msgText = MIMEText('<img src="cid:image1"> <br><br>  Hi <b>' + AE + '</b>,<br> There is a <b>' + Incident +'</b> in ' + Location +'. Alert our Representatives and Customers in <b>' + Location + '</b> location.'
                           '<br><br> Total Policies  Insured - <b>' + str(PolCnt) + '</b> '
                                                                           '<br>Total Insured Amount - <b>' + str(InsAmt)+ '</b><br><br>Regards, <br> <b> Socialert Team', 'html')
        msgAlternative.attach(msgText)

        # Reading the image from the current directory
        fp = open('sm_socialert.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)

        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()
        mail.starttls()

        mail.login('socialerttravelers@gmail.com', 'socialert123')
        mail.sendmail(strFrom, strTo, msg.as_string())

        mail.quit()
