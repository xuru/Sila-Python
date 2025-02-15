#!/usr/bin/env python
import json

from flask import Flask, render_template, request

from silasdk import App

app1 = App("sandbox", '', "test1791.silamoney.eth")

app = Flask(__name__)


@app.route('/')
def output():
    return render_template('index.html', name='Joe')


@app.route('/checkHandle', methods=['POST'])
def checkHandle():
    data = request.json
    result = json.dumps(app1.users.checkHandle(data))
    return result


@app.route('/register', methods=['POST'])
def register():
    # read json + reply
    data = request.json
    result = json.dumps(app1.users.register(data))
    return result


@app.route('/requestKyc', methods=['POST'])
def requestKyc():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    result = json.dumps(app1.users.requestKyc(data, data["private_key"]))
    return result


@app.route('/checkKyc', methods=['POST'])
def checkKyc():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    # read json + reply
    data = request.json
    result = json.dumps(app1.users.checkKyc(data, data["private_key"]))
    return result


@app.route('/linkAccount', methods=['POST'])
def linkAccount():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.data
    data1 = json.loads(data)
    result = json.dumps(app1.users.linkAccount(data1, data1["private_key"], plaid=True))
    return result


@app.route('/getAccounts', methods=['POST'])
def getAccounts():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    private_key = data["private_key"]
    result = json.dumps(app1.users.getAccounts(data, private_key))
    return result


@app.route('/getTransactions', methods=['POST'])
def getTransactions():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    private_key = data["private_key"]
    result = json.dumps(app1.users.getTransactions(data, private_key))
    return result


@app.route('/issueSila', methods=['POST'])
def issueSila():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    private_key = data["private_key"]
    result = json.dumps(app1.transactions.issueSila(data, private_key))
    return result


@app.route('/redeemSila', methods=['POST'])
def redeemSila():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    private_key = data["private_key"]
    result = json.dumps(app1.transactions.redeemSila(data, private_key))
    return result


@app.route('/transferSila', methods=['POST'])
def transferSila():
    """SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction
    """
    data = request.json
    private_key = data["private_key"]
    result = json.dumps(app1.transactions.transferSila(data, private_key))
    return result


if __name__ == '__main__':
    # run!
    app.run()
