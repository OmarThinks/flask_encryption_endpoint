import gnupg




def encrypt_gpg(original:str, passphrase:str):
	gpg = gnupg.GPG()
	original = "123"
	gpg.encoding = 'utf-8'
	encrypted_data = gpg.encrypt(original, 
		passphrase = passphrase, recipients=None, 
		symmetric = True)
	return {
	"status": encrypted_data.status,
	"data": str(encrypted_data.data,"utf-8"),
	"success":encrypted_data.ok
	}	

def decrypt_gpg(encrypted_message, passphrase):
	gpg = gnupg.GPG()
	gpg.encoding = 'utf-8'
	decrypted = gpg.decrypt(str.encode(encrypted_message,"utf-8"), 
		passphrase = passphrase)
	return {
	"status": decrypted.status,
	"data": str(decrypted.data,"utf-8"),
	"success":decrypted.ok
	}





