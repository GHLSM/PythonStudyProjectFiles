from src import admin, student, teacher


status_func = {
    "1": admin.run,
    "2": student.run,
    "3": teacher.run
}

def run():
    while True:
        print(
            "================请输入你的身份编号===============\n"
            "               1.管理员\n"
            "               2.学员\n"
            "               3.老师\n"
            "=============================================="
        )
        choice = input("您的选择是：")
        if not choice.isdigit():
            print("请输入数字")
            continue
        elif int(choice) not in range(0,3):
            print("您的输入不在选择内，请重新输入")
            continue
        else:
            status_func.get(choice)()


