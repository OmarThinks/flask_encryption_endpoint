from pydantic import BaseModel, constr


message_constraint = constr(max_length=100000000000)
passphrase_constraint = constr(min_length=2, max_length=1000000)


class EncryptionInputs(BaseModel):
   message : message_constraint
   passphrase : passphrase_constraint
