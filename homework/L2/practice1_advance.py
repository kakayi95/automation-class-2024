#%%
'''
===================== L2作業 =====================
以練習題為基礎, 調整功能如下
0. 鍾QA發現有時主管會調整排名標準, 請將此程式從"前3名pass"改為一個"前n名pass"的函式, n為參數
1. 程式步驟調整如下
    a. 使用者輸入數據
    b. 數據新增到csv
    c. 查看新數據是否符合前n名標準
2. csv須保留所有舊數據, 不做任何刪除
3. 加分題: 查看前n名的邏輯時, 嘗試不使用sort()來達成. 請參考氣泡排序法檔案 (Bubble.zip)
'''

import csv
import os

def initialize_csv(filename, initial_data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for time in initial_data:
            writer.writerow([time])

def validate_input(input_data):
    if input_data.lower() == 'exit':
        return 'exit'
    try:
        process_time = int(input_data)
        if process_time < 0:
            return None
        return process_time
    except ValueError:
        return None

def add_to_csv(filename, new_time):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([new_time])

def read_from_csv(filename):
    times = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        times = [int(row[0]) for row in reader]
    return times

def is_top_n(new_time, times, n):
    sorted_times = sorted(times + [new_time])
    return sorted_times.index(new_time) < n

csv_filename = 'execution_times.csv'
initial_data = [385, 400, 395, 375, 401]
initialize_csv(csv_filename, initial_data)

n = int(input("請輸入前幾名為通過標準 (n): "))

while True:
    input_data = input("請輸入測試結果（或輸入 'exit' 以結束程式）：")
    validated_input = validate_input(input_data)
    
    if validated_input == 'exit':
        print("程式已終止。")
        break
    elif validated_input is None:
        print("錯誤：請輸入有效的正整數！")
        continue
    
    process_time = validated_input
    add_to_csv(csv_filename, process_time)
    
    all_times = read_from_csv(csv_filename)
    
    if is_top_n(process_time, all_times, n):
        print(f"PASS：新的執行時間 {process_time} 毫秒排名前 {n} 名。")
    else:
        print(f"Fail：新的執行時間 {process_time} 毫秒未能排名前 {n} 名。")
    
    print(f"更新後的執行時間列表：{all_times}")
    print(f"目前前 {n} 名執行時間：{sorted(all_times)[:n]}")
