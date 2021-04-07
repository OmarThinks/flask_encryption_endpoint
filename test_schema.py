import unittest

from schema import schema
import json


class Schema_1_EncryptionTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating Encryption Tests")
		print("test_000: Hello, tests!")

	
	def test_001_successful_inputs(self):
		variables = {"original": "123","passphrase":"secret"}
		query = """
query{
	encryptMessage(
		original:\""""+variables["original"]+"""\",
		passphrase:\""""+variables["passphrase"]+"""\",
	)
}
		"""
		#print(query)
		"""
query{
        encryptMessage(
                original:"123",
                passphrase:"secret",
        )
}
"""
		result = schema.execute(query)
		#print(result)
		"""
{
	'data': 
	{
		'encryptMessage': '-----BEGIN PGP MESSAGE-----\n\n
		jA0EBwMCLuWD7sIvaOrn0jgBMQ+4bBuhr9h+HSy7C0jsftKFJ9
		5Y7+f0xHuiPYxd\nuGLK9yODSo6mWy1zr2v+40936qPMXFvC2g==
		\n=lzBk\n-----END PGP MESSAGE-----\n'
	}
}
		"""
		#print(type(result.data))
		#print((result.data))
		self.assertEqual(type(
			result.data["encryptMessage"]),str)
		print("test_001: successful")


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
