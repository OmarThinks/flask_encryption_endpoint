import gnupg




def encrypt_gpg(gpg, original:str, passphrase:str):
	gpg = gnupg.GPG()
	original = "123"
	gpg.encoding = 'utf-8'
	encrypted_data = gpg.encrypt(original, 
		passphrase = passphrase, recipients=None, 
		symmetric = True)
	return {
	"status": encrypted_data.status,
	"data": str(encrypted_data.data,"utf-8"),
	"success":encrypted_data.success
	}	

def decrypt_gpg(gpg, message, passphrase):
	return gpg.decrypt(message, passphrase = passphrase,
		always_trust =True)
	#return gpg.encrypt(data, recipients)





