from flask import Flask, request, jsonify
import json

app = Flask(__name__)
token = "X53ilBf]XYUc8%zILW"
old_token = []

@app.route('/api/v1/tools/getwhitelist/', methods=['POST'])
def receive_alert():
    data = request.json
    if data["token"] == "":
        return jsonify({'code': 1002, 'data': [], 'message': 'Token not input.'})
    elif data["token"] != token:
        return jsonify({'code': 1003, 'data': [], 'message': 'Token is invalid.'})
    elif data["token"] in old_token:
        return jsonify({'code': 1004, 'data': [], 'message': 'Token is expired. Please contact administrator!'})
    elif data["action"] != "getwhitelist":
        return jsonify({'code': 1001, 'data': [], 'message': 'Action not supported.'})
    else:
        try:
            with open("whitelist.txt", "r") as file:
                whitelist = file.read()
            return jsonify({'code': 0, 'data': [whitelist], 'message': 'success.'})
        except FileNotFoundError:
            return jsonify({'code': 1006, 'data': [], 'message': 'File not found.'})
        except Exception as e:
            return jsonify({'code': 1007, 'data': [], 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)