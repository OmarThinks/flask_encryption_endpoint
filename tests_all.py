import unittest



from test_cryp import (Cryp_1_SuccesstullEncryption, 
	Cryp_2_encrypt_gpg, Cryp_3_decrypt_gpg)
from test_endpoints import (_1_DecryptionTestCase, 
	_2_EncryptionTestCase, _3_ErrorHandlingTestCase)
from test_pydantic_models import (
	Pydantic_1_SuccessfullInputsTestCase, 
	Pydantic_2_FailingInputsTestCase)
from test_schema import (Schema_1_EncryptionTestCase, 
	Schema_2_DecryptionTestCase)

# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()	
