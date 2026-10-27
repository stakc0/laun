from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/launch', methods=['POST'])
def launch_token():
    data = request.get_json()
    token_name = data['tokenName']
    token_symbol = data['tokenSymbol']
    wallet_secret = data['walletSecret']

    # Call the launcher script with the provided parameters
    result = subprocess.run(['python3', '/root/.hermes/workspace/launch/launcher.py', token_name, token_symbol, wallet_secret], capture_output=True, text=True)

    if result.returncode == 0:
        return jsonify({'message': 'Token launched successfully!'})
    else:
        return jsonify({'message': 'Error launching token', 'error': result.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
