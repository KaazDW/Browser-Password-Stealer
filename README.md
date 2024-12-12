
# 🔒🔑 P-Buster - Browser Password Stealer

P-Buster is a Python tool designed to **Decrypt** and **Extract** local saved passwords on Windows.

Originally, I got a Raspberry Pi Pico to use it as a Bad-USB. I wrote a few light scripts for fun and this his one of them.
P-Buster for Password-Buster is a python script use to steal browser saved password.

## Script Development
**How does this work ?**
- **Encryption Keys**: <br/>
Chrome Browsers encrypt saved passwords using a unique key called the _master key_, which is further secured using the operating system's encryption features (e.g., Windows DPAPI - Data Protection API).
This master key is stored in the Local State file in a JSON format and is encrypted using DPAPI.
- **Password Encryption**:<br/>
Individual passwords are encrypted using AES-GCM with this master key and stored in the Login Data database, which is an SQLite file.

Opera (GX here) is a Chromium-based browser, so the process is the same, only the local directory name is different.

Once the passwords are decrypted, depending on the intended use, it can be helpful to implement an extraction method to retrieve the extracted passwords. In this case, I opted to use a Discord webhook for sending revealed passwords.

**Documentations** :
- [https://superuser.com/questions/146742/how-does-google-chrome-store-passwords](https://superuser.com/questions/146742/how-does-google-chrome-store-passwords)
- [https://github.com/ohyicong/decrypt-chrome-passwords/tree/main](https://github.com/ohyicong/decrypt-chrome-passwords/tree/main)
- [https://github.com/hassaanaliw/chromepass/blob/master/chromepass.py](https://github.com/hassaanaliw/chromepass/blob/master/chromepass.py)
- [https://fr.wikipedia.org/wiki/Galois/Counter_Mode](https://fr.wikipedia.org/wiki/Galois/Counter_Mode)
- [https://www.watchguard.com/help/docs/help-center/fr-FR/Content/en-US/Fireware/mvpn/general/ipsec_algorithms_protocols_c.html](https://www.watchguard.com/help/docs/help-center/fr-FR/Content/en-US/Fireware/mvpn/general/ipsec_algorithms_protocols_c.html)

## Requirements

- **Python 3.x**
- Libraries:
  - `json`
  - `base64`
  - `sqlite3`
  - `win32crypt`
  - `pycryptodome` (`Crypto`)
  - `requests`
- A valid Discord webhook URL for extraction.

## Installation

1. Clone the repository or download the script file. 
2. Install the required Python libraries:

   ```
   pip install pycryptodome pypiwin32 requests
   ```
3. ```python p-buster.py```

## Usability
For extract data put your own discord webhook.
```
webhook_url = "..."
```

You can use PiInstaller to make an application file (.exe) from your python script like this
  ```bash
pip install pyinstaller
cd your-directory
python -m PyInstaller --onefile --noconsole p-buster.py
  ```


<br/>

## MIT Licence

Copyright (c) 2024 KaazDW

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**Translation: Ofcourse you can use this for you project! Just make sure to say where you got this from :)**

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


