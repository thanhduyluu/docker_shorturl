from flask import request

from model.config import app
from module.create_all_table import create_table
from module.create_short_token import create_without_user, create_with_user
from module.extend_time import renew_URL
from module.short2long import short2long

create_table()


@app.route('/api-short/l2s-nouser', methods=["POST"])
def createTok_nouser():
    content = request.json
    resp = create_without_user(content)

    return resp


@app.route('/api-short/l2s-user', methods=["POST"])
def createTok_user():
    content = request.json
    resp = create_with_user(content)

    return resp


@app.route('/api-short/s2l', methods=["POST"])
def get_long():
    content = request.json
    resp = short2long(content)

    return resp


@app.route('/api-short/renew', methods=["POST"])
def renew():
    content = request.json
    resp = renew_URL(content)
    return resp

@app.route('/abc', methods=["GET"])
def rene():
    return "hello"

if __name__ == '__main__':
    app.run()
