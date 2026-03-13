import json
import gzip
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from pathlib import Path
import sys

# secret key
SECRET = "exam_app_secret_2026"

if len(sys.argv) < 2:
    print("Usage: python encrypt_question_bank.py <input_json_file>")
    sys.exit(1)

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = INPUT_FILE.rsplit('.', 1)[0] + ".enc"

# read JSON
data = Path(INPUT_FILE).read_bytes()

# gzip compress
compressed = gzip.compress(data)

# create AES key
key = hashlib.sha256(SECRET.encode()).digest()

# fixed IV (16 bytes)
iv = b"\x00" * 16

cipher = Cipher(
    algorithms.AES(key),
    modes.CBC(iv),
    backend=default_backend()
)

encryptor = cipher.encryptor()

# padding
pad_length = 16 - (len(compressed) % 16)
compressed += bytes([pad_length]) * pad_length

encrypted = encryptor.update(compressed) + encryptor.finalize()

# save encrypted file
Path(OUTPUT_FILE).write_bytes(encrypted)

print("Encryption complete:", OUTPUT_FILE)