import unittest

from cryp import encrypt_gpg, decrypt_gpg
import json
import gnupg


gpg = gnupg.GPG()

ecryption = ""


class Cryp_1_SuccesstullEncryption(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating Successful Tests")
		print("test_000: Hello, tests!")

	def test_001(self):
		print("Strating Successful Tests")
		print("test_000: Hello, tests!")



	def test_002(self):
		encrypted = """-----BEGIN PGP MESSAGE-----
Version: GnuPG v2
jA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroAKvJQ===
-----END PGP MESSAGE-----"""
		passphrase = "topsecret"

		#decrypted = decrypt_gpg(gpg,)
		#decrypted = decrypt_gpg(gpg,"kjklj","6546")
		#print(str(decrypted))
		#print("ok: ",decrypted.ok)
		#print("status: ",decrypted.status)
		#print(type(decrypted))
		#print(type(type(decrypted)))
		
		gpg = gnupg.GPG()
		gpg.encoding = 'utf-8'
		input_data = gpg.gen_key_input(key_type="RSA", 
			key_length=1024, passphrase = passphrase)

		key = gpg.gen_key(input_data)
		#print(key)
		# 524F10C5085C17477158B0A124F50836ED5EF628
		#print(type(key))
		#print(key.__dict__)
		"""{'gpg': <gnupg.GPG object at 0x000002BC5BCFC808>, 
		'type': 'P', 'fingerprint': 
		'C51BDA6A9A401C18A11EAC28930EF62CE0C6E166', 
		'data': b'', 'stderr': "gpg: key 930EF62CE0C6E166 marked as ultimately trusted\n[GNUPG:] KEY_CONSIDERED C51BDA6A9A401C18A11EAC28930EF62CE0C6E166 0\ngpg: revocation certificate stored as '/c/Users/Omar Magdy/.gnupg/openpgp-revocs.d/C51BDA6A9A401C18A11EAC28930EF62CE0C6E166.rev'\n[GNUPG:] KEY_CREATED P C51BDA6A9A401C18A11EAC28930EF62CE0C6E166\n"}
		"""
		key_bytes=str.encode(key.fingerprint)
		#print(key_bytes)
		encrypted_ascii_data = gpg.encrypt(key_bytes, 
			recipients=None, symmetric =True, 
			passphrase = passphrase)
		print(encrypted_ascii_data)
		
		#print(encrypted_ascii_data.__dict__)
		"""
		{'gpg': <gnupg.GPG object at 0x0000018A41CFC848>, 
		'valid': False, 'fingerprint': None, 'creation_date': None, 
		'timestamp': None, 'signature_id': None, 'key_id': None, 
		'username': None, 'key_status': None, 'status': 
		'encryption ok', 'pubkey_fingerprint': None, 
		'expire_timestamp': None, 'sig_timestamp': None, 
		'trust_text': None, 'trust_level': None, 'sig_info': {}, 
		'data': b'-----BEGIN PGP MESSAGE-----\n\njA0EBwMC7JJlH2GXguXj0
		lwBLomCjgGikMkZ4H7ItlZkvz9Zk4CDdgeopCD3IPhk\nC3G9a79nt
		5S6B9ydRwqahKJRaxTWt7O8J4h1E5YYIwMIC4TqviM6QyAmqV7QieJu\nne
		LzqnHHSDxFnpH4iw==\n=4DLh\n-----END PGP MESSAGE-----\n', 
		'ok': True, 
		'stderr': 
		'[GNUPG:] PROGRESS need_entropy X 32 128\n[GNUPG:] 
		PROGRESS need_entropy X 128 128\n[GNUPG:] NEED_PASSPHRASE_SYM
		 7 3 2\n[GNUPG:] BEGIN_ENCRYPTION 2 7\n[GNUPG:] END_ENCRYP
		 TION\n'}
		"""

		encrypted_byte_like = str(encrypted_ascii_data.data,'utf-8')
		decrypted = gpg.decrypt(encrypted_byte_like, 
			passphrase = passphrase)
		print(decrypted)
		print("test_002: Checking what is going on!")






# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
