from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Halo Kawab!"

@app.route("/hagemaru")
def hagemaru():
	return "hai cuk!"

if __name__ == "__main__":
	app.run()
