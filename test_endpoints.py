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

	def test_3_empty_request_body(self):
		message = "123"
		passphrase = "secret"
		response = self.client().post('/decryptMessage')
		#print(response.data)
		self.assertEqual(response.status_code,415)
		data = json.loads(response.data)
		#print(data)
		self.assertEqual(data,
			{'detail': "Unsupported media type '' in request."+
			" 'application/json' is required."})
		print("test_3_empty_request_body")




	def test_4_failing_decryption(self):
		message = "123"
		passphrase = "secret"
		response = self.client().post('/decryptMessage',
			json={"message":message,"passphrase":passphrase})
		#print(response.data)
		self.assertEqual(response.status_code,422)
		data = json.loads(response.data)
		self.assertEqual(data,
			{'validation_error': 
				{'body_params': 
					[
						{
							'loc': ['message'], 
							'msg': 'no data was provided', 
						'type': 'value_error.decryption_failure'
						}
					]
				}
			})
		#print(data)
		print("test_4_failing_decryption")











class _2_EncryptionTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		# create and configure the app
		self.app = get_app() #Flask(__name__)
		self.client = self.app.test_client

	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")


	def test_1_successfull_encryption(self):
		original = """-----BEGIN PGP MESSAGE-----

jA0EBwMCtzzONNqLoY7n0jgBm/A6tUAsixA0D9CidvUp0IbSScjAZReHt7BD8q+X
HPL27ysOSglIxAdDWMxDSV692yYbbtO6yw==
=Bbnl
-----END PGP MESSAGE-----"""
		passphrase = "secret"
		response = self.client().post('/encryptOriginal',
			json={"original":original,"passphrase":passphrase})
		self.assertEqual(response.status_code,200)
		data = json.loads(response.data)
		self.assertEqual(data,{'DecryptedMessage': '123'})
		#print(data)
		print("test_1_successfull_decryption")

	def test_2_failing_pydantic(self):
		response = self.client().post('/encryptOriginal',
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
							'loc': ['original'], 
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

	def test_3_empty_request_body(self):
		original = "123"
		passphrase = "secret"
		response = self.client().post('/encryptOriginal')
		#print(response.data)
		self.assertEqual(response.status_code,415)
		data = json.loads(response.data)
		#print(data)
		self.assertEqual(data,
			{'detail': "Unsupported media type '' in request."+
			" 'application/json' is required."})
		print("test_3_empty_request_body")




	def test_4_failing_decryption(self):
		original = "123"
		passphrase = "secret"
		response = self.client().post('/encryptOriginal',
			json={"original":original,"passphrase":passphrase})
		#print(response.data)
		self.assertEqual(response.status_code,422)
		data = json.loads(response.data)
		self.assertEqual(data,
			{'validation_error': 
				{'body_params': 
					[
						{
							'loc': ['original'], 
							'msg': 'no data was provided', 
						'type': 'value_error.decryption_failure'
						}
					]
				}
			})
		#print(data)
		print("test_4_failing_decryption")



















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
