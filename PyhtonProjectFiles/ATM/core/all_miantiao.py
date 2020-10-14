'''
def register():
    while True:
        #1）输入用户名和密码进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()

        ##确认两次密码是否一致
        if password==re_password:
            import json
            import os
            from conf import settings
            user_path = os.path.join(
                settings.USER_DATA_PATH, f'{username}.json'
            )
            # 2.查看用户是否存在
            if os.path.exists(user_path):
                with open(user_path,'r',encoding='utf-8') as f:
                    user_dic = json.load(f)

                if user_dic:
                    print('用户存在，重新输入')
                    continue
                #3.如存在，让用户重新输入
            #4.不存在，保存用户数据
            ##4.组织用户的数据的字典信息
            user_dic={
                'username': username,
                'password': password,
                'balance': 15000,
                #用于记录用户流水的列表
                'flow': [],
                #用于记录用户的购物车
                'shop_car': {},
                #用户被管理状态
                'locked': False
            }
            #用户数据，tank.json, 艾根.json,以用户名字名字命名，便于取数据
            ##4.2拼接用户的json数据路径
            with open(user_path, 'w', encoding='utf-8') as f:
                json.dump(user_dic, f, ensure_ascii=False)
                # ensure_ascii = False  # 显示中文字符

'''