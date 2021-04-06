from pydantic import BaseModel, constr


passphrase_constraint = constr(min_length=2, max_length=1000000)
message_constraint = constr(max_length=100000000000)


class EncryptionInputs(BaseModel):
    passphrase = passphrase_constraint
    message = message_constraint
