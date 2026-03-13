from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running!", "status": "ok"})

@app.route('/files', methods=['GET'])
def list_files():
    files = ["image1.png", "log1.txt"]
    return jsonify({"files": files})

@app.route('/files', methods=['POST'])
def upload_file():
    data = request.json
    return jsonify({"message": "File uploaded", "file": data.get("name")}), 201

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    return jsonify({"message": f"File {filename} deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
