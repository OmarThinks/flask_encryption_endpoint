import unittest

from pydantic_models import EncryptionInputs
import json


class Pydantic_1_SuccessfullInputsTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating Successful Tests")
		print("test_000: Hello, tests!")

	
	def test_001_successful_inputs(self):
		external_data = {
			'message': 'abc','passphrase': 'xyz'
			}
		data = EncryptionInputs(**external_data)
		#print(data.dict())
		self.assertEqual(data,
			{'message': 'abc', 'passphrase': 'xyz'})
		print("test_001: successful")


	def test_002_successful_inputs_casting(self):
		external_data = {
			'message': 123,'passphrase': 456
			}
		# Inputs must be casted to strings
		data = EncryptionInputs(**external_data)
		#print(data.dict())
		self.assertEqual(data,
			{'message': '123', 'passphrase': '456'})
		print("test_002: successful, inputs casted to strings")




class Pydantic_2_FailingInputsTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("")
		print("")
		print("")
		print("")
		print("")
		print("Strating Failing Tests")
		print("test_000: Hello, tests!")

	
	def test_001_missing_all_inputs(self):
		external_data = {}
		try:
			data = EncryptionInputs(**external_data)
		except Exception as e:
			#print(e.json())
			self.assertEqual(json.loads(e.json()),[
		{"loc": ["message"],
    		"msg": "field required","type": "value_error.missing"},
  		{"loc": ["passphrase"],
    		"msg": "field required","type": "value_error.missing"}
		])
		print("test_001: Failing: all missing inputs")


	def test_002_very_short_string(self):
		external_data = {
			'message': "",'passphrase': ""
			}
		# The message could be empty
		try:
			data = EncryptionInputs(**external_data)
		except Exception as e:
			#print(e.json())
			self.assertEqual(json.loads(e.json()),[
  		{"loc": ["passphrase"],
    		"msg": "ensure this value has at least 2 characters",
    		"type": "value_error.any_str.min_length",
    		"ctx": {"limit_value": 2}
  		}])

		print("test_002: Failing, short passphrase")


	def test_003_very_long_string(self):
		external_data = {
			'message': "1"*100000000,
			'passphrase': "1"*100000000
			}
		# Very long strings
		try:
			data = EncryptionInputs(**external_data)
		except Exception as e:
			#print(e.json())
			self.assertEqual(json.loads(e.json()),[
		{"loc": ["message"],
    		"msg": "ensure this value has at most 1000000 characters",
    		"type": "value_error.any_str.max_length",
    		"ctx": {"limit_value": 1000000}
  		},
		{"loc": ["passphrase"],
    		"msg": "ensure this value has at most 10000 characters",
    		"type": "value_error.any_str.max_length",
    		"ctx": {"limit_value": 10000}}])

		print("test_003: Failing, long passphrase and message")







# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
