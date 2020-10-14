'''
公共方法
'''

import hashlib
from core import src
#md5加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '我爱你，LSM'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()


#登录认证装饰器
def login_auth(func):
    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('您未登录,请登录')
            src.login()
    return inner