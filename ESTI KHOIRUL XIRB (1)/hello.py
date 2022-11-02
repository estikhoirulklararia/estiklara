from flask import Flask
app = Flask(__nama__)
@app.route("/")
def hello_world():

	return "Hello world"
@app.route("/tentang/")
def tentang ():
	return "ini halaman tentang"
@app.route