'''
用户接口
'''
from db import db_handler
from lib import commen

def register_interface(username, password, balance = 15000):
    # 2.查看用户是否存在
    ##2.1调用数据处理中的select函数，返回值
    # 3.如存在，return重新输入
    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户存在'
    # 4.不存在，保存用户数据
    password = commen.get_pwd_md5(password)
    ##4.组织用户的数据的字典信息
    user_dic = {
        'username': username,
        'password': password,
        'balance': 15000,
        # 用于记录用户流水的列表
        'flow': [],
        # 用于记录用户的购物车
        'shop_car': {},
        # 用户被管理状态
        'locked': False
    }
    db_handler.save(user_dic)
    return True,f'用户{username}注册成功'

def login_interface(username, password):
    #查看数据
    #判断数据是否存在
    user_dic = db_handler.select(username)
    if user_dic:
        #校验密码/用户名
        password = commen.get_pwd_md5(password)
        if password == user_dic.get('password'):
            return True, f'用户{username} 登陆成功'
        else:
            return False, '密码错误'
    return False, '用户不存在，请注册或重新输入'

def check_bla_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']

