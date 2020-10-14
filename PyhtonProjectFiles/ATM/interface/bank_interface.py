'''
银行接口
'''
from db import db_handler

#提现接口
def withdraw_interface(username, money):
    #获取用户数据
    user_dic = db_handler.select(username)
    balance = int(user_dic.get('balance'))
    money1 = int(money) * 0.05
    money2 = money1 + int(money)

    #判断金额是否足够,足够减钱更新数据，不足够提示信息
    if balance >= money2:
        balance -= money2
        user_dic['balance']=balance

        flow = f'用户{username}提现了{money},手续费为{money1:.2f}\n总金额为{money2:.2f}\n余额为{balance:.2f}'
        user_dic['flow'].append(flow)

        db_handler.save(user_dic)
        return True, flow
    else:
        return False,'您的余额不足，请重新输入'
#还款/充值接口
def repay_interface(username, money):
    user_dic = db_handler.select(username)
    user_dic["balance"] += money
    balance = user_dic['balance']

    flow = f'用户{username} 还款金额为{money}\n目前总余额{balance}'
    user_dic['flow'].append(flow)

    db_handler.save(user_dic)
    return True, flow
#转账接口
def transfer_interface(login_user, tar_username, money):
    login_user_dic = db_handler.select(login_user)
    tar_user_dic = db_handler.select(tar_username)

    if not tar_user_dic:
        return False, '目标用户不存在'

    if login_user_dic["balance"] >= money:
        #当前用户减钱。目标用户加钱
        login_user_dic['balance'] -= money
        tar_user_dic['balance'] -=money
        balance_login = login_user_dic["balance"]
        login_user_flow = f'您给{tar_username}已转账{money},成功\n您的总余额是{balance_login}'
        login_user_dic['flow'].append(login_user_flow)
        tar_user_flow = f'收到用户{login_user}的转账{money}'
        tar_user_dic['flow'].append(tar_user_flow)

        db_handler.save(login_user_dic)
        db_handler.save(tar_user_dic)

        return True, login_user_flow

    else:
        return False, '您的余额不足'
#查看流水接口
def check_flow_interface(login_user):
    user_dic = db_handler.select(login_user)
    return user_dic.get('flow')
