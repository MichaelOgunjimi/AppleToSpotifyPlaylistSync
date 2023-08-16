import datetime


def get_current_day_of_week():
    # Get the current date
    current_date = datetime.date.today()
    # Get the name of the day
    day_name = current_date.strftime("%A")
    return day_name


def find_none_indices(track_uris):
    indices = []
    for i, uri in enumerate(track_uris):
        if uri is None:
            indices.append(i)
    return indices


import smtplib
from email.mime.text import MIMEText


# This part of code is to send notifications when a song can't be added or bot finished running you can comment it
# out if it not needed
def notify(album=None):
    if album:
        if len(album) > 1:
            album = ",\n".join(album)
            gmail_smtp = "smtp.gmail.com"  # you can change this to your smtp
            my_mail = "your sender email"
            my_password = "YourPassword"

            with smtplib.SMTP(gmail_smtp) as connection:
                connection.starttls()
                connection.login(user=my_mail, password=my_password)

                message = MIMEText(f"Sorry this song below couldn't be added automatically \n{album}")
                message['Subject'] = "Apple Spotify Sync!"
                message['From'] = "your sender email"
                message['To'] = "your recipient email address"

                connection.send_message(message)
            print("Email sent!")
    else:
        gmail_smtp = "smtp.gmail.com"   # you can change this to your smtp
        my_mail = "your sender email"
        my_password = "YourPassword"

        with smtplib.SMTP(gmail_smtp) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)

            message = MIMEText("Your automation for your playlist sync just finished running")
            message['Subject'] = "Apple Spotify Sync!"
            message['From'] = "your sender email"
            message['To'] = "your recipient email address"

            connection.send_message(message)
        print("Email sent!")
