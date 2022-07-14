#Server flask web app
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/',methods=['POST'])
def display_ssh_attempts():
    data = request.json
    return jsonify(data)
# main driver function
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)