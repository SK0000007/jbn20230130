from selenium import webdriver
import time
from dateEdit import * # 本来入力する数字等は全て別ファイル(user_data.py)へまとめ
from selenium.webdriver.support.select import Select # ドロップダウンリストの選択肢を触るためのSelectをimport、勤務パターン、種別選択の時に必要

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
for day in workday_list:
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