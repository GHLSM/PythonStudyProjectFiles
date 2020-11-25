from interface import admin_interface


def register():
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    confirm_password = input("请确认您的密码")
    back_dic = admin_interface.register_interface(username, password, confirm_password)

def login():
    pass

def school_init():
    pass

def lessen_init():
    pass

def teacher_init():
    pass


status_func_dic = {
    "1": register,
    "2": login,
    "3": school_init,
    "4": lessen_init,
    "5": teacher_init
}
def run():
    while True:
        print("===========请选择功能，输入功能编号：==========\n"
              "              1.注册\n"
              "              2.登录\n"
              "              3.学校管理\n"
              "              4.课程管理\n"
              "              5.讲师管理\n"
              "输入'q'退出\n"
              "===========================================")
        choice = input("您的选择是：")
        if choice == 'q':
            break
        elif not choice.isdigit():
            print("请输入数字")
            continue
        elif int(choice) not in range(0, 3):
            print("您的输入不在选择内，请重新输入")
            continue
        else:
            status_func_dic.get(choice)()
