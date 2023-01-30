import tkinter as tk
from datetime import datetime, timedelta
# import datetime
import calendar, jpholiday
# import pandas
import main ##tkinterのウインドウで実行ボタン押したときに走るようにする時にimport必要

# ログイン情報
mail = ''
password = ''
# 出勤日
workday_list = []
# Cworkday_list = []

# 勤務時間の区切り時間
job_time_lsit = ['8:30', '12:00', '13:00', '17:30']

today = datetime.today().date()
y = today.year
m = today.month
###メソッド###
###特定の日付の日を1にリプレイス###
def get_first_date(dt):
    return dt.replace(day=1)

###ｙ年ｍ月の土日祝を取得listで返すメソッド###dns_date_list=土日祝
def get_dns_date_list_dates(y, m):
    # 祝日を取得
    holidays = list(map(lambda d: d[0], jpholiday.month_holidays(y, m)))
    # 土日を取得
    c = calendar.Calendar()
    donichi = list(filter(lambda d: d.month == m and d.weekday() in [5,6], c.itermonthdates(y,m)))
    # マージして昇順にソート
    dns_date_list = sorted(list(set(holidays + donichi)), key=lambda d: d.day)
    return dns_date_list

#受け取った日付リストの日だけをリストへ入れなおすメソッド(年月の情報削除して日の数字だけのリストにする)
def refac_list(l):
    for i in range(len(l)):
        # print(i.day)
        l[i] = l[i].day
    return l

# 今月の全日付のリスト生成()　任意の月の日数を取得calendar.monthrange(y, m)[1]
all_date_list = [get_first_date(today) + timedelta(days=i) for i in range(calendar.monthrange(y, m)[1])]
#今月の土日祝のリスト
dns_date_list=get_dns_date_list_dates(y,m)#ｙとｍにはデフォで今月が入る
# print(refac_list(all_date_list))
# print(refac_list(dns_date_list))
# new_list = (set(all_date_list + dns_date_list))
# print(workday_list)
# print(all_date_list)
# print("________________変換___________________")

workday_list = sorted(list(set(all_date_list) ^ set(dns_date_list)))
workday_list = refac_list(workday_list) #先頭０なしのLISTへ変換
all_date_list = refac_list(all_date_list) #先頭０なしのLISTへ変換
# print(workday_list)
# print(all_date_list)


# #先頭の0を消すメソッドremoveZero
# A = ['0001234','01000','1000',]
# def removeZero(A):
#     Alist = []
#     for x in A:
#      while x[0] == "0":
#       x = x[1:]
#      Alist.append(x)
#     return Alist
# print(removeZero(A))

#画面に描画するtkinter
window = tk.Tk()
window.geometry("300x850")
window.title("楽々勤怠入力")
# today = datetime.date.today()
# ラベル
label = tk.Label(text=today)
# チェックボタンのラベルをリスト化する
chk_txt = all_date_list
# チェックボックスON/OFFの状態
chk_bln = {}
# chk_bln = Cworkday_list
# variable = None

# チェックボタンを動的に作成して配置
for i in range(len(chk_txt)):
    text = chk_txt[i] #yyy-mm-ddのデータ
    # text_r =refac_list(chk_txt[i])
    chk_bln[i] = tk.BooleanVar()
    chk = tk.Checkbutton(window, variable=chk_bln[i], text=chk_txt[i], font=("", 9,)) 
    chk.place(x=50, y=30 + (i * 24))
    
    # text_r = text.strftime('%d')
    # workday_list = ["{:%02d}".format(i) for i in workday_list]
    # # workday_list = list(map(lambda x: "{:02d}".format(x), workday_list))
    # for i in str(workday_list):
    #     str(workday_list).append("{:02d}".format(i))
    # text_r = text_r.lstrip("0") #stringの先頭の文字列0を消す
    # # text_r = int(text_r)

    if text in workday_list:
        # print(True)   
        chk.select() #全てチェックON
    # print(text)
    # print(workday_list)
    # print(dns_date_list)
    # ir = i + 1
    # for i in workday_list:
    #     ir == i
    #     chk.select()
    
    
# ボタンクリックイベント(チェック有無をセット)
def btn_click(bln):
    for i in range(len(chk_bln)):
        chk_bln[i].set(bln)
        
#チェックボックスオプションURL
#https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/




# # 　実行ボタン
exe_button = tk.Button(window,command=main, text="実行", font=("MSゴシック", "10", "bold"))
# exe_button = tk.Button(text="実行", command=lambda:main("ここへ受け渡すデータを入れるlist？"))
# exe_button = tk.Button(text="実行",font=("MSゴシック", "10", "bold"))#仮設置


#.pack()コーナー画面描画の締めの手続き
# frame.pack(padx=20,pady=10)##スクロールバー実装の残骸
# canvas.pack()##スクロールバー実装の残骸


label.pack() #今日の日付の表示反映
exe_button.pack(side=tk.BOTTOM, pady=20) #実行ボタン表示反映

window.mainloop()
# btn_click(0)

# # スクロールバー関連開始
# # メインフレームの作成と設置
# # Listboxの選択肢
# days = all_date_list
# lists = tk.StringVar(value=days)

# canvas = tk.Canvas(window, listvariable=lists, height=20, bg='white')
# frame = tk.Frame(canvas)
# canvas.create_window((4,4),window=frame, anchor="nw")
# # 各種ウィジェットの作成
# # canvas = tk.Canvas(frame, listvariable=lists, height=20)
# # スクロールバーの作成
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
# # スクロールバーをcanvasに反映
# canvas["yscrollcommand"] = scrollbar.set
# # 各種ウィジェットの設置
# canvas.grid(row=0, column=0)
# scrollbar.grid(row=0, column=0, sticky=(tk.N, tk.S))
# #スクロールバー関連終わり


#
#date_text = datetime.strptime(text, '%Y-%m-%d %H:%M:%S')
    # tdate = datetime.date(date_text.year, date_text.month, date_text.day)
    # text_r=refac_list(tdate)
#
#