from functions import *
from flask import Flask, request


app = Flask(__name__)

@app.route("/",methods=["GET"])
def return_movies():
    city = request.args.get("city").lower()
    return getMovies(city)


if __name__ == "__main__":
    app.run(debug=True)