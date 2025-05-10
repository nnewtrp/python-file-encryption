# 🔐 File Encryption with Python

This project uses Python to encrypt and decrypt files with a combination of classic and modern techniques, including RSA and custom-built ciphers. For more details, see the [Project_Report.pdf](./Project_Report.pdf) file.

---

## 🔐 Algorithms Used

### Caesar Cipher
A classical substitution cipher that shifts characters **K positions** forward.  
> 📝 In this implementation, we **do not use mod 26**, allowing for an extended character range beyond just A-Z.

---

### Rail-Fence Cipher
A transposition cipher that arranges the plaintext in a zigzag pattern across **K rows**, then reads it row-by-row to produce ciphertext.

---

### Long-Code Cipher
A **custom encryption method** developed for this project. Each plaintext character is transformed into **two ciphertext characters**, effectively **doubling the length** of the encrypted message. This technique adds complexity and obscurity to the encryption process.

---

### RSA Algorithm
An asymmetric cryptographic algorithm used to **securely exchange keys**. RSA generates a pair of public and private keys for encryption and decryption, providing a layer of security for message transfer.

---

## 🛠 Installation & Setup

### Prerequisites

- Python 3.x installed on your machine

### Steps

#### 1. **Clone the Repository**
```bash
git clone https://github.com/nnewtrp/file-encryption-python.git
cd file-encryption-python
```

#### 2. **Add Your File**
Place the file you want to encrypt or decrypt into the **root folder** of the project.

#### 3. **Run the Program**
```bash
python main.py
```

#### 4. **Follow the On-Screen Menu**
- Type the number to choose a function:

  - 1 → Encrypt

  - 2 → Decrypt

- Enter the **file name** you want to encrypt or decrypt when prompted.

## 📜 Learn More
[Python Docs](https://docs.python.org/3/)

[Caesar Cipher - Wiki](https://en.wikipedia.org/wiki/Caesar_cipher)

[Rail Fence Cipher - Wiki](https://en.wikipedia.org/wiki/Rail_fence_cipher)

[RSA Algorithm - Wiki](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

---

## 📬 More Information  

This project was developed as the **final project** for **ITS335 - IT Security** at **Sirindhorn International Institute of Technology, Thammasat University**.

📧 Contact: teerapat.sat24@gmail.com

🔗 GitHub: [nnewtrp](https://github.com/nnewtrp)
