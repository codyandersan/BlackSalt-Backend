from flask import Flask, request, jsonify
from video import search_youtube

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/search')
#Eg: /search?query=polar+covalent+bond
def search():
    query = request.args.get('query')
    # Use the query to perform the search
    print("Searching for: " + query)
    resp = search_youtube(query)
    return jsonify(resp)




if __name__ == "__main__":
    app.run(debug=True)
