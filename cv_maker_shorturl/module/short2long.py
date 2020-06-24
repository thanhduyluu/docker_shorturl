from model.config import db, SHORT_LINK
import string
import secrets
import datetime
from model.model import URL


def short2long(content):

    short_token = content["short_token"]

    resp = {
        "message": "URL not exist",
        "status": "FAIL",
        "long_url": "",
        "code": 404
    }

    query = db.session.query(URL).filter(URL.shortToken == short_token)
    if query.count() == 0:
       resp["message"] = "URL not exist"
       resp["status"] = "FAIL"
       resp["code"] = 404
    else:
        url = query.first()
        if datetime.datetime.now() > url.expireAt:
            resp["message"] = "URL expired"
            resp["status"] = "EXPIRED"
            resp["code"] = 402
        else:
            long_url = url.longURL
            resp["message"] = "Get Success"
            resp["long_url"] = long_url
            resp["code"] = 200
            resp["status"] = "SUCCESS"

    return resp


