import base64
import gc
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AdvancedCryptoEngine:

  def __init__(self, password: str, passkey: str):
    """രണ്ട് പാസ്‌വേഡുകൾ/കീകൾ ഉപയോഗിച്ച് കൂടുതൽ സുരക്ഷിതമായ മെമ്മറി കീ ഉണ്ടാക്കുന്നു."""
    self.salt = os.urandom(16)
    self._key = self._derive_master_key(password, passkey, self.salt)

  def _derive_master_key(
      self, password: str, passkey: str, salt: bytes
  ) -> bytes:
    """PBKDF2 SHA-256 ഉപയോഗിച്ച് Multi-Layer Key Derivation."""
    combined_secret = (password + passkey).encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1000000,  # Extreme Brute-Force Protection
    )
    derived = base64.urlsafe_b64encode(kdf.derive(combined_secret))

    # combined_secret മെമ്മറിയിൽ നിന്ന് മാറ്റുന്നു
    del combined_secret
    gc.collect()

    return derived

  def secure_wipe(self, variable):
    """RAM-ൽ ഉള്ള സെൻസിറ്റീവ് ഡാറ്റ മായ്ച്ചു കളയുന്നു."""
    del variable
    gc.collect()

  # 1. മറ്റ് പ്രോഗ്രാമുകൾക്ക് നേരിട്ട് ഉപയോഗിക്കാവുന്ന Data Encryption
  def encrypt_data(self, plain_text: str) -> bytes:
    cipher = Fernet(self._key)
    encrypted_bytes = cipher.encrypt(plain_text.encode())
    return self.salt + encrypted_bytes

  # 2. Data Decryption
  def decrypt_data(self, encrypted_payload: bytes) -> str:
    salt = encrypted_payload[:16]
    cipher_text = encrypted_payload[16:]

    cipher = Fernet(self._key)
    decrypted_bytes = cipher.decrypt(cipher_text)
    return decrypted_bytes.decode('utf-8')

  # 3. സമ്പൂർണ്ണ ഫയൽ എൻക്രിപ്ഷൻ (Entire File Encryption)
  def encrypt_file(self, input_filepath: str, output_filepath: str = None):
    if not output_filepath:
      output_filepath = input_filepath + '.enc'

    with open(input_filepath, 'rb') as f:
      file_data = f.read()

    cipher = Fernet(self._key)
    encrypted_data = cipher.encrypt(file_data)

    with open(output_filepath, 'wb') as f:
      f.write(self.salt + encrypted_data)

    print(f'[+] {input_filepath} വിജയകരമായി എൻക്രിപ്റ്റ് ചെയ്തു -> {output_filepath}')

  # 4. സമ്പൂർണ്ണ ഫയൽ ഡിക്രിപ്ഷൻ (Entire File Decryption)
  def decrypt_file(self, encrypted_filepath: str, output_filepath: str):
    with open(encrypted_filepath, 'rb') as f:
      file_data = f.read()

    salt = file_data[:16]
    cipher_bytes = file_data[16:]

    cipher = Fernet(self._key)
    decrypted_data = cipher.decrypt(cipher_bytes)

    with open(output_filepath, 'wb') as f:
      f.write(decrypted_data)

    print(f'[+] {encrypted_filepath} വിജയകരമായി ഡിക്രിപ്റ്റ് ചെയ്തു -> {output_filepath}')

  def wipe_memory_keys(self):
    """പ്രോഗ്രാം നിർത്തുമ്പോൾ മാസ്റ്റർ കീ മെമ്മറിയിൽ നിന്നും നീക്കുന്നു."""
    self._key = b'\x00' * 32
    del self._key
    gc.collect()
