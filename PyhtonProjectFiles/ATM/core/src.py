from interface import user_interface
from interface import bank_interface
from lib import commen
#全局变量，记录用户是否已经登陆
login_user = None
# 1.注册功能
def register():
    while True:
        #1）输入用户名和密码进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        ##可输入自定义金额

        ##确认两次密码是否一致
        if password == re_password:
            #调用接口的注册接口，交给接口层处理
            # res----->(False, '用户存在')
            # res = user_interface.register_interface(username,password)
            flag, msg = user_interface.register_interface(
                username, password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('您输入的密码不正确，请重新输入')


        #利用flag来确定用户注册状态，是否成功

# 2.登录功能
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag, msg = user_interface.login_interface(
            username, password
        )
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)

# 3.查看余额
@commen.login_auth
def check_balance():
    balance = user_interface.check_bla_interface(
        login_user
    )
    print(f'用户{login_user} 您的余额为：{balance}')

# 4.提现功能
@commen.login_auth
def withdraw():
    while True:
        #输入提现金额
        input_money = input('请输入您提现金额：').strip()
        if not input_money.isdigit():
            print('您的输入有误，请重新输入')
            continue

        flag, msg = bank_interface.withdraw_interface(
            login_user, input_money
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 5.还款功能
@commen.login_auth
def repay():
    while True:
        input_money = input('请输入你需要还款的金额：').strip()
        if not input_money.isdigit():
            print('请输入正确的数字金额')
            continue
        input_money = int(input_money)
        if input_money > 0:
            #调用还款接口
            flag, msg = bank_interface.repay_interface(
                login_user, input_money
            )
            if flag:
                print(msg)
                break
        else:
            print('您输入的金额有误，请重新输入')

# 6.转账功能
@commen.login_auth
def transfer():
    while True:
        #输入转账用户，金额
        tar_username = input('请输入转行目标：').strip()
        money = input('请输入转行金额：').strip()
        if not money.isdigit():
            print('请输入正确的金额')
            continue

        money = int(money)
        if money > 0:
            # 调用转账接口
            flag, msg = bank_interface.transfer_interface(
            login_user, tar_username, money
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入正确的金额')

# 7.查看流水
@commen.login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(
        login_user
    )
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('当前用户没有流水')

# 8.购物功能
@commen.login_auth
def shopping():
    while True:
        pass
# 9.查看购物车
@commen.login_auth
def check_shop_car():
    pass


# 10.管理员功能
def admin():
    pass
#创建函数功能字典
func_dic={
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}

def run():
    while True:
        print('''
        1.注册功能
        2.登录功能
        3.查看功能
        4.提现功能
        5.还款功能
        6.转账功能
        7.查看流水
        8.购物功能
        9.查看购物车
        10.管理员功能
        '''
        )

        choice = input('请输入功能编号：').strip()
        if choice not in func_dic:
            print('请输入正确的功能编号')
            continue

        func_dic.get(choice)()
