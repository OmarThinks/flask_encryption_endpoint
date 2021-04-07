from pydantic import BaseModel, constr


message_constraint = constr(max_length=1000000000000)
original_constraint = constr(max_length=1000000)
passphrase_constraint = constr(min_length=2, max_length=10000)



class DecryptionInputs(BaseModel):
   message : str
   passphrase : passphrase_constraint


class EncryptionInputs(BaseModel):
   original : original_constraint
   passphrase : passphrase_constraint

