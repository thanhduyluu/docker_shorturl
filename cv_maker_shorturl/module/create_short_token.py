from model.config import db, SHORT_LINK
import string
import secrets
import datetime
from model.model import URL


def random_token(length):
    alphabet = string.ascii_lowercase + string.digits
    token = ''.join(secrets.choice(alphabet) for i in range(length))
    return token


def create_without_user(content):
    check_token = True

    long_url = content["long_url"]
    time = content["time"]

    resp = {
            "message": "Create Sucess",
            "status": "SUCCESS",
            "short_url": "",
            "short_token": "",
            "code": "200"
            }

    query = db.session.query(URL).filter(URL.longURL == long_url)
    if query.count() == 0:
        while check_token is True:
            short_token = random_token(6)
            if db.session.query(URL.shortToken).filter(URL.shortToken == short_token).count() == 0:
                check_token = False
            else:
                continue
            short_url = SHORT_LINK.format(short_token)
            create_at = datetime.datetime.now()
            expire_at = create_at + datetime.timedelta(days=int(time))
            data = URL(short_token, long_url, create_at, expire_at)
            db.session.add(data)
            db.session.commit()

            resp["short_url"] = short_url
            resp["short_token"] = short_token


    else:
        url = query.first()

        short_url = SHORT_LINK.format(url.shortToken)
        resp["message"] = "Create fail, URL exists"
        resp["short_url"] = short_url
        resp["short_token"] = url.shortToken
        resp["code"] = 200
        resp["status"] = "FAIL"

    return resp


def create_with_user(content):
    check_token = True

    long_url = content["long_url"]
    email = content["email"]
    time = content["time"]

    resp = {
        "message": "Create Sucess",
        "status": "SUCCESS",
        "short_url": "",
        "short_token": "",
        "code": "200"
    }
    query_email = db.session.query(URL).filter(URL.userEmail == email)
    if query_email.count() == 0:
        query = db.session.query(URL).filter(URL.longURL == long_url)
        if query.count() == 0:
            is_duplicate = 0
            while check_token is True:

                if is_duplicate == 0:
                    short_token = email.split("@")[0]
                else:
                    short_token = email.split("@")[0] + "-" + str(is_duplicate)
                if db.session.query(URL).filter(URL.shortToken == short_token).count() == 0:
                    check_token = False
                else:
                    is_duplicate +=1
                    continue
                short_url = SHORT_LINK.format(short_token)
                create_at = datetime.datetime.now()
                expire_at = create_at + datetime.timedelta(days=int(time))
                data = URL(short_token, long_url, create_at, expire_at)
                data.userEmail = email
                db.session.add(data)
                db.session.commit()
                resp["short_url"] = short_url
                resp["short_token"] = short_token



        else:
            url = query.first()

            short_url = SHORT_LINK.format(url.shortToken)
            resp["message"] = "Create fail, URL exists"
            resp["short_url"] = short_url
            resp["short_token"] = url.shortToken
            resp["code"] = 404
            resp["status"] = "FAIL"
    else:
        url = query_email.first()
        short_url = SHORT_LINK.format(url.shortToken)
        resp["message"] = "Create fail, email exists"
        resp["short_url"] = short_url
        resp["short_token"] = url.shortToken
        resp["code"] = 404
        resp["status"] = "FAIL"
    return resp



