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
{'data': {'encryptMessage': 
'-----BEGIN PGP MESSAGE-----\n\njA0EBwMCnfx01GLicp7n0jgBK25j4EwOm+rM85AVyJv6p1uuhY1wY8oNP5dLKEB0\nvs7PW5hz2KM+D3+eBa/LXZI90MmCQEQQQA==\n=O6rp\n-----END PGP MESSAGE-----\n'
}}
		"""
		#print(type(result.data))
		#print((result.data))
		self.assertEqual(type(
			result.data["encryptMessage"]),str)
		print("test_001: Encryption successful")


	def test_002_missing_inputs(self):
		query = "query{encryptMessage()}"

		result = schema.execute(query)
		#print(result)
		"""
{'errors': [{'message': 'Syntax Error GraphQL (1:22) Expected Name, 
found )\n\n1: query{encryptMessage()}\n                        ^\n', 
'locations': [{'line': 1, 'column': 22}]}]}
		"""
		try:
			result.data
			raise Exception("result does not have data")
		except Exception as e:
			pass
		print("test_002_Encryprion_missing_inputs")







class Schema_2_DecryptionTestCase(unittest.TestCase):
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")	

	def test_000(self):
		print("Strating Decryption Tests")
		print("test_000: Hello, tests!")

	
	def test_001_successful_inputs(self):
		message='-----BEGIN PGP MESSAGE-----\n\njA0EBwMCnfx01GLicp7n0jgBK25j4EwOm+rM85AVyJv6p1uuhY1wY8oNP5dLKEB0\nvs7PW5hz2KM+D3+eBa/LXZI90MmCQEQQQA==\n=O6rp\n-----END PGP MESSAGE-----\n'
		variables = {"message": message,"passphrase":"secret"}
		query = """
query($message: String, $passphrase: String)
{
    decryptMessage(
        message:$message,
        passphrase:$passphrase,
        )
}
		"""
		#print(query)
		"""
query($message: String, $passphrase: String){
    decryptMessage(
        message:$message,
        passphrase:$passphrase,
        )
}
"""
		result = schema.execute(query, variable_values=variables)
		#print(result)
		#"{'data': {'decryptMessage': '123'}}"
		#print(type(result.data))
		#print((result.data))
		self.assertEqual(result.data["decryptMessage"],"123")
		print("test_001: Decryption successful")


	def test_002_missing_inputs(self):
		query = "query{decryptMessage()}"

		result = schema.execute(query)
		#print(result)
		"""
{'errors': [{'message': 'Syntax Error GraphQL (1:22) Expected Name, 
found )\n\n1: query{decryptMessage()
}\n                        ^\n', 'locations': [{'line': 1, 
'column': 22}]}]}
		"""
		try:
			result.data
			raise Exception("result does not have data")
		except Exception as e:
			pass
		print("test_002_Decryprion_missing_inputs")

















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
