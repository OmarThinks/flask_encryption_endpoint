import graphene


class EncryptionResult(graphene.ObjectType):
    encryptedMessage = graphene.String()

class DecryptionResult(graphene.ObjectType):
    decryptedMessage = graphene.String()







