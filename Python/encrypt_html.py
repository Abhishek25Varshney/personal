import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.keywrap import InvalidUnwrap
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt_html(html_content: str, password: str) -> str:
    backend = default_backend()
    salt = os.urandom(16)
    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(password.encode('utf-8'))

    # Generate IV for AES-GCM
    iv = os.urandom(12)

    # Encrypt using AES-GCM
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=backend
    ).encryptor()

    ciphertext = encryptor.update(html_content.encode('utf-8')) + encryptor.finalize()
    tag = encryptor.tag

    # Combine: salt (16 bytes) + iv (12 bytes) + ciphertext + tag (16 bytes)
    combined = salt + iv + ciphertext + tag

    # Base64 encode
    encrypted_b64 = base64.b64encode(combined).decode('utf-8')
    return encrypted_b64
