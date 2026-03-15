#!/usr/bin/env python3
"""
Encrypt a question bank JSON file for use with utils/decryptQuestionBank.ts.

Pipeline (matches decrypt order in reverse):
  1. Read JSON and encrypt with AES-256 (key = SHA256(secret), ECB, PKCS7).
  2. Encode ciphertext as Base64 (UTF-8 string).
  3. Compress with gzip (so the .enc file starts with gzip header 1f 8b).
  4. Write to .enc file.

Usage:
  QUESTION_BANK_SECRET=exam_app_secret_2026 python scripts/encrypt_question_bank.py path/to/exam.json

Output:
  path/to/exam.enc  (same path with .json replaced by .enc)

Env:
  QUESTION_BANK_SECRET  Required. Must match the secret in utils/cryptoKey.ts.
"""

import argparse
import base64
import gzip
import hashlib
import os
import sys
from pathlib import Path

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except ImportError:
    print("Install PyCryptodome: pip install pycryptodome", file=sys.stderr)
    sys.exit(1)


def get_aes_key(secret: str) -> bytes:
    """AES-256 key = SHA256(secret). Matches utils/decryptQuestionBank.ts."""
    return hashlib.sha256(secret.encode("utf-8")).digest()


def encrypt_aes_ecb(plaintext: str, key: bytes) -> bytes:
    """Encrypt plaintext with AES-256 ECB, PKCS7 padding. Returns raw ciphertext bytes."""
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode("utf-8"), AES.block_size)
    return cipher.encrypt(padded)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encrypt question bank JSON to .enc (gzip + AES-256, SHA256 key)."
    )
    parser.add_argument(
        "json_path",
        type=Path,
        help="Path to the input JSON file",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output .enc path (default: same as input with .enc extension)",
    )
    args = parser.parse_args()

    secret = os.environ.get("QUESTION_BANK_SECRET")
    if not secret or not isinstance(secret, str):
        print(
            "Missing QUESTION_BANK_SECRET. Set it when running:",
            "  QUESTION_BANK_SECRET=your-secret python scripts/encrypt_question_bank.py <input.json>",
            sep="\n",
            file=sys.stderr,
        )
        sys.exit(1)

    json_path = args.json_path.resolve()
    if not json_path.exists():
        print(f"Input file not found: {json_path}", file=sys.stderr)
        sys.exit(1)

    if args.output is not None:
        enc_path = args.output.resolve()
    else:
        enc_path = json_path.with_suffix(".enc")

    # 1. Read JSON (preserve as-is for consistent stringify)
    with open(json_path, "r", encoding="utf-8") as f:
        plaintext = f.read()

    # 2. AES encrypt (key = SHA256(secret), ECB, PKCS7)
    key = get_aes_key(secret)
    ciphertext = encrypt_aes_ecb(plaintext, key)

    # 3. Base64 encode (decrypt expects a string from ungzip)
    b64 = base64.b64encode(ciphertext).decode("ascii")

    # 4. Gzip so .enc starts with gzip header 1f 8b
    compressed = gzip.compress(b64.encode("utf-8"))

    enc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(enc_path, "wb") as f:
        f.write(compressed)

    # Sanity check: first two bytes are gzip magic
    assert compressed[:2] == bytes([0x1F, 0x8B]), "expected gzip header 1f 8b"
    print("Encrypted and compressed:", json_path.name, "->", enc_path.name)
    print("First 2 bytes (hex):", compressed[:2].hex(), "(gzip header)")
    print("Upload", enc_path, "to your CDN.")


if __name__ == "__main__":
    main()
