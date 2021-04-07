import graphene

from cryp import (encrypt_gpg, decrypt_gpg)

class EncryptionResult(graphene.ObjectType):
    encrypted_message = graphene.String()

class DecryptionResult(graphene.ObjectType):
    decrypted_message = graphene.String()


class EncryptionError(Exception):
	pass
class DecryptionError(Exception):
	pass


class RootQuery(graphene.ObjectType):
	encrypt_message = graphene.Field(EncryptionResult)
	decrypt_message = graphene.Field(DecryptionResult)

	def resolve_encrypt_message(root, info, 
		original:str, passphrase:str):
		encrypted = encrypt_gpg(original = original, 
			passphrase = passphrase)
		if encrypted["success"] == True:
			return encrypted["data"]
		else:
			raise EncryptionError(encrypted["status"])

	def resolve_decrypt_message(root, info, 
		message:str, passphrase:str):
		decrypted = encrypt_gpg(message = message, 
			passphrase = passphrase)
		if decrypted["success"] == True:
			return decrypted["data"]
		else:
			raise DecryptionError(decrypted["status"])



schema = graphene.Schema(query=RootQuery)










