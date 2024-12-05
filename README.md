Android Penetration Testing Utility

This project provides an Android penetration testing utility designed for educational purposes and security assessments. It enables users to generate and manage payloads for remote access to Android devices, incorporating Metasploit functionalities such as session management and payload creation.

---

Table of Contents

1. Create Payload APK and Merge with Another APK  
2. Launch Listener  
3. Exit  

*Select an option (1, 2, or 3):*

---

Prerequisites

Ensure the following tools and libraries are installed on your system:

- Python 3.6 or higher  
- Metasploit Framework  
- Python library `pymetasploit3`  
- Tools: `msfvenom`, `msfconsole`, and `apktool`

---

Installation Steps

1. Clone the Repository:
   ```
   git clone https://github.com/alihusseinabdulkalaq/Ethical-Access-to-Mobile-Files.git
   cd yourrepository
   ```

2. Set Up the Python Environment:
   Create and activate a virtual environment for better package management:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install pymetasploit3
   ```

3. Install Metasploit Framework:
   If Metasploit is not installed, use the following command:
   ```
   sudo apt update
   sudo apt install metasploit-framework
   ```

4. Install Additional Tools:
   Ensure `apktool`, `msfvenom`, and `zipalign` are installed:
   ```
   sudo apt install apktool
   ```

---

Important Notes

- Permissions: The generated payload APK may request various permissions (e.g., camera and location access) to demonstrate testing scenarios.  
- Usage: Restrict testing to authorized environments and devices only. Unauthorized use is strictly prohibited.  
