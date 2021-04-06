import unittest

from pydantic_models import EncryptionInputs

class PydanticInputsTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating tests")
		print("test_000: Hello, tests!")

	
	def test_001_successful_inputs(self):
		external_data = {
			'passphrase': '1321','message': '6865',
			}
		data = EncryptionInputs(**external_data)
		#print(data.dict())
		self.assertEqual(data,
			{'message': '6865', 'passphrase': '1321'})
		print("test_001: successful")


# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
