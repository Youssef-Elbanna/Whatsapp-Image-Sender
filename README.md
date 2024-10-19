Here’s a detailed **README** for the **Automated WhatsApp Image Sender** project:

---

# Automated WhatsApp Image Sender

This project automates the process of sending images to multiple contacts via **WhatsApp Web** using **Python** and **Selenium**. The script handles WhatsApp login, opens individual chats, uploads images, and sends them to specific contacts. It also incorporates error handling and retry mechanisms to ensure reliable delivery.

## Features
- **Automated WhatsApp Login:**  
  The script uses **WhatsApp Web** for logging in. Users simply scan the QR code, and the script automates the rest.
  
- **Dynamic Image Sending:**  
  Each contact receives a unique image from a designated folder based on their order in the contact list.

- **Retry Mechanism:**  
  For each contact, the script retries up to 5 times if the image fails to send.

- **Error Handling:**  
  The script gracefully handles issues such as missing images or failed message deliveries, providing feedback in the terminal.

- **Delivery Confirmation:**  
  The script waits for WhatsApp’s delivery confirmation (single or double checkmarks) before proceeding to the next contact.

## Requirements
- Python 3.x
- Selenium
- ChromeDriver

### Install Required Packages:
```bash
pip install selenium
```

### Download ChromeDriver:
You can download the appropriate version of ChromeDriver for your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Setup Instructions

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/YOUR-USERNAME/Automated-WhatsApp-Image-Sender.git
    ```

2. Set up **ChromeDriver** and provide the correct path to the driver in the script:
    ```python
    service = Service("path/to/your/chromedriver.exe")
    ```

3. Define the **phone numbers** of your contacts (including the country code) in the script:
    ```python
    phone_numbers = [
        '+201200000000',
        '+201100000000',
        '+201000000000',
        '+201500000000'
    ]
    ```

4. Specify the base path for the images in the `image_path_base` variable:
    ```python
    image_path_base = r"C:/path/to/your/images/folder/"
    ```

5. Run the script:
    ```bash
    python whatsapp_image_sender.py
    ```

6. **Scan the WhatsApp Web QR code** using your mobile device when prompted. Once logged in, the script will start sending images to the specified contacts.

## Script Walkthrough

1. **Login to WhatsApp Web:**  
   The script will navigate to WhatsApp Web, prompting you to scan the QR code for authentication.

2. **Message Sending Loop:**  
   For each phone number in the list, the script:
   - Opens the corresponding WhatsApp chat using the URL `https://web.whatsapp.com/send?phone=<number>`.
   - Waits for the chat to load.
   - Uploads the corresponding image from the specified folder.
   - Sends the image to the contact.
   - Waits for delivery confirmation before proceeding to the next contact.

3. **Error Handling:**  
   If an image is missing or fails to send, the script retries up to 5 times before moving to the next contact.

4. **Image Naming Convention:**  
   The script assumes images are named sequentially (e.g., `1.jpg`, `2.jpg`, etc.). You can adjust the starting number by modifying the `i` variable in the script:
   ```python
   i = 1  # Start from image 1
   ```

## Customization

- **Image Path:**  
  Customize the `image_path_base` to point to the folder containing your images.
  
- **Phone Numbers:**  
  Update the `phone_numbers` list to include the phone numbers of your contacts.

- **Number of Retries:**  
  Modify the `max_retries` variable if you want to change the retry limit.

## Limitations

- **Manual Login:**  
  The script currently requires you to manually log in to WhatsApp Web by scanning the QR code.
  
- **Sequential Image Naming:**  
  Images are expected to follow a specific naming convention. You may need to rename files or adjust the logic if your images don't follow this pattern.

## Future Enhancements

- **Automated WhatsApp Login:**  
  Implementing automatic login through saved session cookies.
  
- **Enhanced Customization:**  
  Adding support for custom message text along with the images.

## License

This project is open-source and available under the [MIT License](LICENSE).
