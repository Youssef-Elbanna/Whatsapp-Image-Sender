from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os  # To check if the image file exists

# List of phone numbers with +20 prefix
phone_numbers = [
    '+201207094190',
    '+201555122389',
    '+201274669278',
    '+201157666299'
]


# Base path to the images
image_path_base = r"C:/Users/Lenovo/Documents/walid and talaat ids/smouha al-mahmoudia pt2/smouha al-mahmoudia/"

# Setup WebDriver (Chrome in this case)
service = Service("C:/Users/Lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
input("Scan QR Code and press Enter")

# Maximum number of retries for each phone number
max_retries = 5
i = 20  # Start from image 1

# Iterate through the phone numbers and send images
for number in phone_numbers:
    attempt = 0
    success = False

    while attempt < max_retries and not success:
        #if i <=9:
        #image_path = f"{image_path_base}0{i}.jpg"
        #else:
        image_path = f"{image_path_base}{i}.jpg"

        # Check if the image exists
        if not os.path.exists(image_path):
            print(f"Image {image_path} not found. Trying the next image.")
            attempt += 1
            i += 1  # Try the next image number for the same phone number
            continue

        try:
            # Create a direct URL for WhatsApp web
            wa_url = f"https://web.whatsapp.com/send?phone={number}"

            # Open WhatsApp chat for the number
            driver.get(wa_url)

            # Wait for the chat to load by checking for the message input field
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"]'))
            )

            # Wait for the attachment button to be clickable
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x11xpdln span[data-icon="plus"]'))
            )

            # Click on the "Attach" button
            attach_button = driver.find_element(By.CSS_SELECTOR, 'div.x11xpdln span[data-icon="plus"]')
            attach_button.click()

            # Wait for the file input to appear
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
            )

            # Click on the "Photos & Videos" button and upload the image
            photo_video_button = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            photo_video_button.send_keys(image_path)

            # Wait for the send button to be present after the image is uploaded
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-icon="send"]'))
            )

            # Press the Send button
            send_button = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="send"]')
            send_button.click()

            # Wait for the message to be sent (either single or double checkmarks)
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-icon="msg-check"], span[data-icon="msg-dblcheck"]'))
                )
                success = True
                print(f"Image {image_path} successfully sent to {number}.")
            except Exception as e:
                print(f"Message not sent for {number}. Possible error: {e}")

            # Move to the next image for the next number
            i += 1

            # Wait a few seconds before moving to the next contact
            time.sleep(3)

        except Exception as e:
            print(f"Error sending image to {number}: {e}")
            attempt += 1

# Close the browser after all messages are sent
driver.quit()
