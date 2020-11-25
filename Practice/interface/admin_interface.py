from db import models


def register_interface(username, password, confirm_password, *args, **kwargs):
    back_dic = {
        "code": 1,
        "msg": ""
    }
