from flask import Flask

def get_app():
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
		return {"message":"Hello, World!"}

	
	@app.route('/ping')
	def pinging():
		return {"message":"Ping"}
	return app








if __name__ == '__main__':
	app = get_app()
	app.run(debug = True)