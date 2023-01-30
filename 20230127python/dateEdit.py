from selenium import webdriver
from selenium.webdriver.support.select import Select # ドロップダウンリストの選択肢を触るためのSelectをimport、勤務パターン、種別選択の時に必要
import tkinter as tk
from datetime import datetime, timedelta
import calendar, jpholiday, time

# ログイン情報
mail = 'kazama@jibun-note.co.jp'
password = 'kazama007'
# # 出勤日
# workday_list = []

# 勤務時間の区切り時間
job_time_lsit = ['8:30', '12:00', '13:00', '17:30']

today = datetime.today().date()
y = today.year
m = today.month
check_list = []
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

workday_list = sorted(list(set(all_date_list) ^ set(dns_date_list)))
workday_list = refac_list(workday_list) #先頭０なしのLISTへ変換
all_date_list = refac_list(all_date_list) #先頭０なしのLISTへ変換

###画面に描画するtkinterの記述###
window = tk.Tk()
window.geometry("300x850")
window.title("楽々勤怠入力")
# ラベル
label = tk.Label(text=f"今日は{today}")
# チェックボタンのラベルをリスト化する
chk_txt = all_date_list
# チェックボックスON/OFFの状態
chk_bln = {}

# チェックボタンを動的に作成して配置
for i in range(len(chk_txt)):
    text = chk_txt[i] #yyy-mm-ddのデータ
    chk_bln[i] = tk.BooleanVar()
    chk = tk.Checkbutton(window, variable=chk_bln[i], text=chk_txt[i], font=("", 9,)) 
    chk.place(x=50, y=30 + (i * 24))

    if text in workday_list: #全ての日(text=all_date_list)と出勤日(workday_list)を比較
        chk.select() #全てチェックON
    
# ボタンクリックイベント(チェック有無をセット)
def btn_click(bln):
    for i in range(len(chk_bln)):
        chk_bln[i].set(bln)
#ウインドウを閉じる        
def close_window():
    # window.destroy()
    window.quit()
    # exit()     

def get_check_list():
    #チェックリストへonとoffをappendする   
    for i in all_date_list:
        x =chk_bln[i].get()
        if(x == True):
            check_list.append(i)
    return check_list        
        
    new_list = dict(zip(all_date_list, check_list))#日付と:true or false
    #もしtrueだったらリストへ格納に変える
                    
    ###チェックボックスの状態をリストへ格納する
    ###all_date_listをキー、onoffをバリューにした辞書型listを作成
    #new_list = {}
    #for i in 
    ###       

#チェックボックスオプションURL
#https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/

# # 　実行ボタン
exe_button = tk.Button(window, command=close_window, text="実行する", font=("MSゴシック", "8", "bold"))
# exe_button = tk.Button(window, command=close_window, text="実行する", font=("MSゴシック", "8", "bold"))
# exe_button = tk.Button(window, command=lambda:[autoLogin(), quite_window()], text="実行する", font=("MSゴシック", "8", "bold"))
# exe_button = tk.Button(text="実行", command=lambda:main("ここへ受け渡すデータを入れるlist？"))
# exe_button = tk.Button(text="実行",font=("MSゴシック", "10", "bold"))#仮設置

label.pack() #今日の日付の表示反映
exe_button.pack(side=tk.BOTTOM, pady=20) #実行ボタン表示反映

window.mainloop()


get_check_list()

driver = webdriver.Chrome() # Seleniumを使ってGoogle Chromeを起動
driver.get("https://attendance.moneyforward.com/my_page") # URLへアクセス

# ログイン方法選択画面
time.sleep(2)
# ログインボタンのパスを取得しクリック
ID_LOGIN_BTN = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div/div/a') 
ID_LOGIN_BTN.click()
time.sleep(1)

# メールアドレス入力画面
MAIL_FORM = driver.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[2]/div/div[2]/div[1]/section/form/div[2]/div/input')
MAIL_FORM.send_keys(mail)
ID_LOGIN_BTN1 = driver.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[2]/div/div[2]/div[1]/section/form/div[2]/div/div[3]/input')
time.sleep(0.1)
ID_LOGIN_BTN1.click()
time.sleep(1)

# パスワード入力画面
PASS_FORM = driver.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[2]/div/div[2]/div[1]/section/form/div[2]/div/input[2]')
PASS_FORM.send_keys(password)
ID_LOGIN_BTN2 = driver.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[2]/div/div[2]/div[1]/section/form/div[2]/div/div[3]/input')
time.sleep(0.1)
ID_LOGIN_BTN2.click()
time.sleep(1)

# ログインが完了しホーム画面へ遷移
# ホーム画面の日時勤怠をクリック 
DAY_TIME_BTN = driver.find_element_by_xpath(
    '/html/body/div[1]/header/nav/ul/li[2]/a') 
DAY_TIME_BTN.click()
time.sleep(0.3)
# 日時勤怠画面の一括編集をクリック
ALL_EDIT_BTN = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div/section/section/section/div[4]/div[1]/a[1]/button') 
ALL_EDIT_BTN.click()
time.sleep(0.3)

# 編集画面でworkday_listに格納された日付の数だけ作業を繰り返す
for day in check_list:
    # 勤務パターン選択
    JOB_P_DROP = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{day}]/td[3]/select')
    select = Select(JOB_P_DROP)
    select.select_by_index(1)
    # 出勤時間を入力
    time_FORM = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{day}]/td[4]/div/input')
    time_FORM.send_keys(job_time_lsit[0])
    # 退勤時間を入力
    time_FORM = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{day}]/td[5]/div/input')
    time_FORM.send_keys(job_time_lsit[3])
    # 休憩開始時間を入力
    time_FORM = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{day}]/td[6]/div/input')
    time_FORM.send_keys(job_time_lsit[1])
    # 休憩終了時間を入力
    time_FORM = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/table/tbody/tr[{day}]/td[7]/div/input')
    time_FORM.send_keys(job_time_lsit[2])
# for文抜けたら保存ボタンをクリック
SAVE_BTN = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/input[2]')
SAVE_BTN.click()

# 基本的な作業手順#
# 要素のXpath取得は操作したいサイトでCtrl+shift+C→操作したい要素を選択→要素タブの・・・を押してコピーからXpathをコピーし.find_element_by_xpathの（""）内へ貼り付ける
# 完全なXpathもXpathも一緒の時がある。とりあえず完全でやっとけばおｋぽい
#  time.sleep入れないと入力されなかったりする
#  = driver.find_element_by_xpath('') 要素の指定''の中へパスを張り付ける
#  .send_keys('')   要素へ文字を入れる
#  .click()         でクリックを指定
# 　.submit()　　    要素を送る？
#  select.select_by_index(len(select.options)-1)  # ドロップダウン最後のoptionタグを選択状態に
