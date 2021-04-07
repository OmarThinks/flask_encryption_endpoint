import unittest

from pydantic_models import DecryptionInputs


import unittest
import json
from flask import Flask, request, abort, jsonify

from app import get_app


unittest.TestLoader.sortTestMethodsUsing = None

class _1_DecryptionTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		# create and configure the app
		self.app = get_app() #Flask(__name__)
		self.client = self.app.test_client

	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")


	def test_2_Failing_encryption(self):
		message = "123"
		passphrase = "secret"
		response = self.client().post('/decryptMessage',
			json={"message":message,"passphrase":passphrase})
		print(response.data)
		self.assertEqual(response.status_code,200)
		data = json.loads(response.data)
		print(data)



# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
