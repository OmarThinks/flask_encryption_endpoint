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


	def test_1_successfull_decryption(self):
		message = """-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----"""
		passphrase = "secret"
		response = self.client().post('/decryptMessage',
			json={"message":message,"passphrase":passphrase})
		self.assertEqual(response.status_code,200)
		data = json.loads(response.data)
		self.assertEqual(data,{'DecryptedMessage': '123'})
		#print(data)
		print("test_1_successfull_decryption")

	def test_2_failing_pydantic(self):
		message = "123"
		passphrase = "secret"
		response = self.client().post('/decryptMessage',
			json={})
		#print(response.data)
		self.assertEqual(response.status_code,400)
		data = json.loads(response.data)
		#print(data)
		self.assertEqual(data,
			{'validation_error': 
				{'body_params': 
					[
						{
							'loc': ['message'], 
							'msg': 'field required', 
							'type': 'value_error.missing'
						}, 
						{	
							'loc': ['passphrase'], 
							'msg': 'field required', 
							'type': 'value_error.missing'
						}
					]
				}
			})
		print("test_2_failing_pydantic")




	def test_3_failing_decryption(self):
		message = "123"
		passphrase = "secret"
		response = self.client().post('/decryptMessage',
			json={"message":message,"passphrase":passphrase})
		#print(response.data)
		self.assertEqual(response.status_code,200)
		data = json.loads(response.data)
		#print(data)



# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
