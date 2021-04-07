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
		#print(encrypted_ascii_data)
		
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
		#print(encrypted_byte_like)
		decrypted = gpg.decrypt(encrypted_byte_like, 
			passphrase = passphrase)
		#print(decrypted)
		print("test_002: Checking what is going on!")


	def test_003(self):
		gpg = gnupg.GPG()
		gpg.encoding = 'utf-8'
		message = """-----BEGIN PGP MESSAGE-----

jA0EBwMCCh8jyvfn2RPj0l0BmJ8zvlBA6xEJ9+LbMbSkvCBl0AfdC+NdLeXeU6st
HaC4I34AqY0zHBB7rOwyxOCbvVXbi2djaseXI16N/g/tnns3D7jChvbtyG5T/ec/
El5Oq0MsOcNYPD8Wmes=
=cHQI
-----END PGP MESSAGE-----"""
		passphrase = "topsecret"
		encrypted_byte_like_message = str.encode(message,'utf-8')
		decrypted = gpg.decrypt(message, 
			passphrase = passphrase)
		#print(decrypted.__dict__)
		"""
		{'gpg': <gnupg.GPG object at 0x0000016CAA1DE708>, 
		'valid': False, 'fingerprint': None, 
		'creation_date': None, 'timestamp': None, 
		'signature_id': None, 
		'key_id': None, 
		'username': None, 
		'key_status': None, 
		'status': 'decryption ok', 
		'pubkey_fingerprint': None, 
		'expire_timestamp': None, 'sig_timestamp': None, 
		'trust_text': None, 'trust_level': None, 
		'sig_info': {}, 
		'data': 
			b'148983A563091519643D6CB55FE5F8C3A3795DCA', 
		'ok': True, 
		'stderr': 
		'gpg: AES.CFB encrypted data\n[GNUPG:] NEED_PASSPH
		RASE_SYM 7 3 2\ngpg: encrypted with 1 passphras
		e\n[GNUPG:] BEGIN_DECRYPTION\n[GNUPG:] DECRYPTION_C
		OMPLIANCE_MODE 23\n[GNUPG:] DECRYPTION_INFO 2 7 0\n[GNU
		PG:] PLAINTEXT 62 1617749602 \n[GNUPG:] PLAINTEXT_LE
		NGTH 40\n[GNUPG:] DECRYPTION_OKAY\n[GNUPG:] GOODMDC\n
		[GNUPG:] END_DECRYPTION\n'}
		"""
		#print(decrypted)
		self.assertEqual(str(decrypted.data,"utf-8"), 
			"148983A563091519643D6CB55FE5F8C3A3795DCA")
		print("test_003:successful_decryption")





	def test_004_failing_decryption(self):
		gpg = gnupg.GPG()
		gpg.encoding = 'utf-8'
		message = "2132"
		passphrase = "topsecret"
		decrypted = gpg.decrypt(message, 
			passphrase = passphrase)
		#print((decrypted.__dict__))
		"""
		{'gpg': <gnupg.GPG object at 0x000001CF61E7D9C8>, 
		'valid': False, 
		'fingerprint': None, 
		'creation_date': None, 
		'timestamp': None, 
		'signature_id': None, 
		'key_id': 'decrypt 4294967295', 
		'username': None, 'key_status': None, 
		'status': 'no data was provided', 
		'pubkey_fingerprint': None, 
		'expire_timestamp': None, 
		'sig_timestamp': None, 
		'trust_text': None, 
		'trust_level': None, 
		'sig_info': {}, 
		'data': 
			b'', 
		'ok': False, 
		'stderr': 'gpg: no valid OpenPGP data found.\n[GNUPG:] 
		NODATA 1\n[GNUPG:] NODATA 2\n[GNUPG:] FAILURE decrypt 
		4294967295\ngpg: decrypt_message failed: Unknown 
		system error\n'}
		"""	
		#print(decrypted.stderr)
		self.assertEqual(decrypted.ok, False)
		self.assertEqual(decrypted.status, "no data was provided")
		print("test_004_failing_decryption")






	def test_005_before_encryption_after_decryption(self):
		gpg = gnupg.GPG()
		original = "123"
		gpg.encoding = 'utf-8'
		passphrase = "topsecret"
		encrypted_data = gpg.encrypt(original, 
			passphrase = passphrase, recipients=None, 
			symmetric = True)
		#print((encrypted_data.__dict__))
		"""
{'gpg': <gnupg.GPG object at 0x000001EDD313CC48>, 
'valid': False, 'fingerprint': None, 'creation_date': None, 
'timestamp': None, 'signature_id': None, 'key_id': None, 
'username': None, 'key_status': None, 

'status': 'encryption ok', 

'pubkey_fingerprint': None, 'expire_timestamp': None, 
'sig_timestamp': None, 'trust_text': None, 'trust_level': None, 
'sig_info': {}, 

'data': b'-----BEGIN PGP MESSAGE-----\n\njA0EBwMCfOkvRdwM7MDn0j
gBnBq714pZz0955bTNE1IrIbL4nstjIibQOOoCHQkq\nqmu3HNs4
N0jXS3yDjaqc3F+n6Vrj/Cf/oQ==\n=QeTC\n-----END PGP MESSAGE--
---\n', 

'ok': True, 

'stderr': '[GNUPG:] PROGRESS need_entropy X 32 128\n[GNUPG:] PROGR
ESS need_entropy X 128 128\n[GNUPG:] NEED_PASSPHRASE_SYM 7 3 2
\n[GNUPG:] BEGIN_ENCRYPTION 2 7\n[GNUPG:] END_ENCRYPTION\n'}		
		"""
		decrypted = gpg.decrypt(str(encrypted_data.data,"utf-8"), 
			passphrase = passphrase)
		#print(((decrypted.__dict__)))
		"""
{'gpg': <gnupg.GPG object at 0x000001EDD313CC48>, 'valid': False, 
'fingerprint': None, 'creation_date': None, 'timestamp': None, 
'signature_id': None, 'key_id': None, 'username': None, 
'key_status': None, 

'status': 'decryption ok', 
'pubkey_fingerprint': None, 'expire_timestamp': None, 
'sig_timestamp': None, 'trust_text': None, 'trust_level': None, 
'sig_info': {}, 


'data': b'123', 

'ok': True, 

'stderr': 'gpg: AES.CFB encrypted data\n[GNUPG:] NE
ED_PASSPHRASE_SYM 7 3 2\ngpg: encrypted with 1 passp
hrase\n[GNUPG:] BEGIN_DECRYPTION\n[GNUPG:] DECRYPTI
ON_COMPLIANCE_MODE 23\n[GNUPG:] DECRYPTION_INFO 2 7 0\n[GNUP
G:] PLAINTEXT 62 1617792579 \n[GNUPG:] PLAINTEXT_LENGTH 3\n[GNUP
G:] DECRYPTION_OKAY\n[GNUPG:] GOODMDC\n[GNUPG:] END_DECRYPTI
ON\n'}
"""		
		#print((str(decrypted.data,"utf-8")))
		decrypted_string = str(decrypted.data,"utf-8")
		self.assertEqual(decrypted_string,original)
		"""
		{'gpg': <gnupg.GPG object at 0x000001CF61E7D9C8>, 
		'valid': False, 
		'fingerprint': None, 
		'creation_date': None, 
		'timestamp': None, 
		'signature_id': None, 
		'key_id': 'decrypt 4294967295', 
		'username': None, 'key_status': None, 
		'status': 'no data was provided', 
		'pubkey_fingerprint': None, 
		'expire_timestamp': None, 
		'sig_timestamp': None, 
		'trust_text': None, 
		'trust_level': None, 
		'sig_info': {}, 
		'data': 
			b'', 
		'ok': False, 
		'stderr': 'gpg: no valid OpenPGP data found.\n[GNUPG:] 
		NODATA 1\n[GNUPG:] NODATA 2\n[GNUPG:] FAILURE decrypt 
		4294967295\ngpg: decrypt_message failed: Unknown 
		system error\n'}
		"""	
		#print(decrypted.stderr)
		#self.assertEqual(decrypted.ok, False)
		#self.assertEqual(decrypted.status, "no data was provided")
		print("test_005_before_encryption_after_decryption")








class Cryp_2_encrypt_gpg(unittest.TestCase):
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_001_sucessfull_encryption(self):
		encrypted = encrypt_gpg(
			original="123",passphrase="secret")
		self.assertEqual(encrypted["success"],True)
		self.assertEqual(encrypted["status"],
			"encryption ok")
		self.assertEqual(type(encrypted["data"]),str)
		print("test_001_sucessfull_encryption")
		#print(encrypted["data"])
		"""
-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----"""








class Cryp_3_decrypt_gpg(unittest.TestCase):
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_001_sucessfull_decryption(self):
		decrypted = decrypt_gpg(
			encrypted_message= """-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----""",
			passphrase="secret")
		#print(decrypted)
		self.assertEqual(decrypted,{
			'status': 'decryption ok', 'data': '123', 
			'success': True})
		print("test_001_sucessfull_decryption")
		#print(encrypted["data"])
		"""
-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----
		"""


	def test_002_failing_decryption(self):
		decrypted = decrypt_gpg(
			encrypted_message= """wrong message""",
			passphrase="secret")
		#print(decrypted)
		self.assertEqual(decrypted,{
			'status': 'no data was provided', 
			'data': '', 'success': False})
		print("test_002_failing_decryption")
		#print(encrypted["data"])
		"""
-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----
		"""


















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
