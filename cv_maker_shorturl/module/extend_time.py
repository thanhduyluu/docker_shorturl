from model.config import db
import datetime
from model.model import URL


def renew_URL(content):

    time = content["time"]
    short_token = content["short_token"]

    resp = {
        "message": "Get URL Sucess",
        "status": "SUCCESS",
        "code": "200"
    }

    query = db.session.query(URL).filter(URL.shortToken == short_token)
    if query.count() == 0:
        resp["message"] = "Renew URL Fail"
        resp["status"] = "FAIL"
        resp["code"] = 404
    else:
        url = query.fist()
        if datetime.datetime.now() > url.expireAt:
            url.expireAt = datetime.datetime.now() + datetime.timedelta(days=int(time))
        else:
            url.expireAt += datetime.timedelta(days=int(time))

    return resp


