import tkinter as tk
from datetime import datetime, timedelta
# import datetime
import calendar, jpholiday
# import pandas
# import main ##tkinterのウインドウで実行ボタン押したときに走るようにする時にimport必要

# ログイン情報
mail = '@jibun-note.co.jp'
password = ''
# 出勤日
workday_list = []
Cworkday_list = []

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
    """
    y年m月の土日祝日のリストを返却する
    """
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
workday_list = sorted(list(set(all_date_list) ^ set(dns_date_list)))
Cworkday_list = refac_list(workday_list)
print(Cworkday_list)


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

# #画面に描画するtkinter
# window = tk.Tk()
# window.geometry("300x555")
# window.title("楽々勤怠入力")
# # today = datetime.date.today()
# # ラベル
# label = tk.Label(text=today)
# # チェックボタンのラベルをリスト化する
# chk_txt = all_date_list
# # チェックボックスON/OFFの状態
# chk_bln = {}

# # チェックボタンを動的に作成して配置
# for i in range(len(chk_txt)):
#     chk_bln[i] = tk.BooleanVar()
#     chk = tk.Checkbutton(window, variable=chk_bln[i], text=chk_txt[i], font=("", 9,)) 
#     chk.place(x=50, y=30 + (i * 24))
    
# # ボタンクリックイベント(チェック有無をセット)
# def btn_click(bln):
#     for i in range(len(chk_bln)):
#         chk_bln[i].set(bln)
# #チェックボックスオプションURL
# #https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/


# # スクロールバー
# # メインフレームの作成と設置
# frame = tk.Frame(window)
# frame.pack(padx=20,pady=10)
# # Listboxの選択肢
# days = all_date_list
# lists = tk.StringVar(value=days)
# # 各種ウィジェットの作成
# Listbox = tk.Listbox(frame, listvariable=lists, height=31)
# # スクロールバーの作成
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=Listbox.yview)
# # スクロールバーをListboxに反映
# Listbox["yscrollcommand"] = scrollbar.set
# # 各種ウィジェットの設置
# Listbox.grid(row=0, column=0)
# scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
#　ボタン
# button = tk.Button(window,command=main, text="実行", font=("MSゴシック", "10", "bold"))
# button = tk.Button(text="実行", command=lambda:main("ここへ受け渡すデータを入れるlist？"))
# button = tk.Button(text="実行",font=("MSゴシック", "10", "bold"))#仮設置


# label.pack()
# button.pack(side=tk.BOTTOM, pady=20)

# window.mainloop()
