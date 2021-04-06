import gnupg




def encrypt_gpg(gpg, data, recipients = None):
	return gpg.encrypt(data, recipients)

def decrypt_gpg(gpg, message, passphrase):
	return gpg.decrypt(message, passphrase = passphrase,
		always_trust =True)
	#return gpg.encrypt(data, recipients)





