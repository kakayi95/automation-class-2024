# %%
# ====== 練習1 ======
'''
請設計1「行車測速紀錄程式」, 
讓使用者輸入五次紀錄, 數字到小數點第二位
請將該五筆紀錄從最高排至最低
ex: 使用者依序輸入: 100.58, 97.88, 100.14, 98.73, 99.81
正確輸出: [100.58, 100.14, 99.81, 98.73, 97.88]
提示: 需轉換為浮點數, 可使用 float() 函式
'''

speed_records = []

for i in range(5):
    while True:
        try:
            speed = float(input(f"請輸入行車速度 - 第 {i + 1} 筆: "))
            if speed < 0:
                print("速度不可為負數，請重新輸入")
                continue
            speed = round(speed, 2)
            speed_records.append(speed)
            break
        except ValueError:
            print("請輸入有效的數字！")
            
speed_records.sort(reverse=True)
print(speed_records)