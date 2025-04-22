import smtplib, ssl, dotenv, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

black_listed_mails = [] # To add in the future

mail_port = 465 # SSL port
my_email = 'kevincncaplescu@gmail.com'


ssl_context = ssl.create_default_context()

def SendDetailsToMainMail(data,apiData):
    try:
        if black_listed_mails.index(data['CONTACT']): # should raise if not in the blacklist
            return # if in blacklist, end the process by returning nothing
        raise # go into exception branch with actual smtp logic
    except:
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",mail_port,context=ssl_context) as server:


                server.login(apiData["notifier_mail"],password=apiData["notifier_pass"])

                formatted_message = MIMEMultipart("alternative")
                formatted_message['Subject'] = f"MESSAGE FROM: {data['CONTACT']}"
                formatted_message['From'] = apiData["notifier_mail"]
                formatted_message['To'] = my_email

                hypertext = f"""\
                <html lang="en">
                    <body>
                        <h2>Enquiry type: {data['ENQUIRY']} <br></h2>
                        <p>{data['MESSAGE']}<br><br></p>
                        <p><i>Client name: {data['NAME']}<br>
                        Client Email: {data['CONTACT']}</i></p>
                    </body>
                </html>
                """

                formatted_message.attach(MIMEText(hypertext,"html"))

                server.sendmail(apiData["notifier_mail"],my_email,formatted_message.as_string())
        except Exception as e:
                print(f"Error logging: mail couldn't be sent for this individual: {data['CONTACT']}")
                print(f"Exception in question:\n{e}")
                raise


def SendReceiptToClient(ReceiptData,apiData):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",mail_port,context=ssl_context) as server:
            server.login(apiData["notifier_mail"],password=apiData["notifier_pass"])

            formatted_message = MIMEMultipart("alternative")
            formatted_message['Subject'] = f"We got your enquiry!"
            formatted_message['From'] = apiData["notifier_mail"]
            formatted_message['To'] = ReceiptData['CLIENT_EMAIL']

            requestType = ReceiptData['ENQUIRY']
            clientName = ReceiptData['CLIENT_NAME']

            hypertext = f"""\
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8" />
                <title>Thank You Email - Kevin-Caplescu.dev</title>
                <style>
                body {{
                    background-color: #15191d;
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', sans-serif;
                    color: #cfd8f1;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #1f2328;
                    border-radius: 8px;
                    padding: 20px;
                }}
                h1 {{
                    font-size: 24px;
                    color: #cfd8f1;
                    text-align: center;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.6;
                    color: #ffffff;
                }}
                .footer {{
                    text-align: center;
                    font-size: 12px;
                    color: #aaa;
                    margin-top: 30px;
                    padding: 10px 0;
                    border-top: 1px solid #333;
                }}
                .social-icons img {{
                    width: 24px;
                    margin: 0 6px;
                }}
                </style>
            </head>
            <body>
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td align="center">
                    <table class="container" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                        <td align="center">
                            <h1>THANK YOU FOR CONTACTING US!</h1>
                            <p>
                            Hey, {clientName}!<br /><br />
                            Thanks for reaching out! Our team of experts is already working on your {requestType} request and will get back to you as soon as possible.<br /><br />
                            In the meantime, feel free to explore our website and learn more about our services.<br /><br />
                            Have a great day!<br /><br />
                            <strong>Kevin Caplescu<br />Founder, Kevin-Caplescu.dev</strong>
                            </p>
                        </td>
                        </tr>
                        <tr>
                        <td class="footer">
                            Kevin-Caplescu.dev &copy; — Delivering smart, scalable digital solutions.<br /><br />
                            <div class="social-icons">
                            <a href="https://www.linkedin.com/in/kevin-cpl">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" />
                            </a>
                            <a href="https://github.com/Kevin-CNC">
                                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" />
                            </a>
                            </div>
                        </td>
                        </tr>
                    </table>
                    </td>
                </tr>
                </table>
            </body>
            </html>
            """

            formatted_message.attach(MIMEText(hypertext,"html"))

            server.sendmail(apiData["notifier_mail"],my_email,formatted_message.as_string())
    except Exception as e:
            print(f"Exception in question:\n{e}")
            raise