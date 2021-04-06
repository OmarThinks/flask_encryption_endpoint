import unittest

from cryp import encrypt_gpg, decrypt_gpg
import json


class Pydantic_1_SuccessfullInputsTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating Successful Tests")
		print("test_000: Hello, tests!")




# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
