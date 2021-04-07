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
		print(query)
		result = schema.execute(query)
		print(result)
		print("test_001: successful")


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
