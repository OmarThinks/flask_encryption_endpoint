from flask import Flask, jsonify
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
		if decrypted["success"] == True:
			return {"DecryptedMessage":decrypted["data"]}
		else:
			return jsonify(
				{'validation_error': 
				{'body_params': 
					[
						{
							'loc': ['message'], 
							'msg': decrypted["status"], 
						'type': 'value_error.decryption_failure'
						}
					]}
			}),422








	@app.route("/encryptOriginal", methods=["POST"])
	@validate()
	def encryption_end_point(body: EncryptionInputs):
		#print(body.__dict__)
		encrypted = encrypt_gpg(
			original = body.original, 
			passphrase = body.passphrase)
		if encrypted["success"] == True:
			return {"EncryptedMessage":encrypted["data"]}
		else:
			return jsonify(
				{'validation_error': 
				{'body_params': 
					[
						{
							'loc': ['message'], 
							'msg': encrypted["status"], 
						'type': 'value_error.decryption_failure'
						}
					]}
			}),422
	return app









if __name__ == '__main__':
	app = get_app()
	app.run(debug = True)