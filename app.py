from flask import Flask
import gnupg

app = Flask(__name__)
gpg = gnupg.GPG()

def get_app():

	@app.route("/")
	def hello_world():
		return {"message":"hello, world!"}

	
	@app.route("/ping")
	def pinging():
		return {"message":"ping"}




	
	return app








if __name__ == '__main__':
	app = get_app()
	app.run(debug = True)