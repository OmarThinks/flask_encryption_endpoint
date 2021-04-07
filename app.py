from flask import Flask
import gnupg

from pydantic_models import (EncryptionInputs,DecryptionInputs)
from cryp import (encrypt_gpg, decrypt_gpg)

from flask_pydantic import validate

def get_app():
	app = Flask(__name__)

	@app.route("/")
	def hello_world():
		return {"message":"hello, world!"}

	
	@app.route("/ping")
	def ping():
		return {"message":"ping"}


	@app.route("/decryptMessage", methods=["POST"])
	@validate()
	def decryption_end_point(body: DecryptionInputs):
		#print(body.__dict__)
		decrypted = decrypt_gpg(
			encrypted_message = body.message, 
			passphrase = body.passphrase)
		return decrypted
	return app








if __name__ == '__main__':
	app = get_app()
	app.run(debug = True)