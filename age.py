#年齡判斷程式
driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過駕照測驗了')
    else:
        print('未滿法定駕駛年齡,不應該開車')
elif driving == '沒有':
    if age >= 18:
        print('可以考駕照了,祝你順利考到駕照')
    else:
        print('等滿18歲就可以考駕照了^^')