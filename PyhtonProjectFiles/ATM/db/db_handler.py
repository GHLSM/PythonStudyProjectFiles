import json
import os
from conf import settings

#查看数据
def select(username):
    #接受接口层传输的数据username，拼接用户json文件路径
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    #校验用户json文件是否存在
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic

    #用户不存在，默认返回None

#保存数据
def save(user_dic):
    # 用户数据，tank.json, 艾根.json,以用户名字名字命名，便于取数据
    ##4.2拼接用户的json数据路径
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
        # ensure_ascii = False  # 显示中文字符