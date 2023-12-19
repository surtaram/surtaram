from datetime import datetime


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y%md%H%M%S")
    email = "test" + time_stamp + "@gmail.com"
    print(email)
    return email


generate_email_with_time_stamp()
