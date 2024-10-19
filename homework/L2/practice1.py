'''
鍾QA正在測試某程式不同版本執行時間,
他有一個串列:process_time_latest, 存放A程式執行毫秒的數據(最新一筆置於最後)
ex: process_time_latest = [385, 400, 395, 375, 401]
分別代表近五次A程式執行時間, 最新一次為401毫秒
請設計程式步驟:
1. 您的程式開始時, 能讓使用者再輸入一筆最新測試結果, 例如 389
2. 若該結果與最新5筆數據相比排前三名(時間越短, 排名越高), 則顯示pass, 否則顯示fail
3. 顯示完成後, 這筆數據須加入process_time_latest串列, 並置放於最新的一筆
其他功能: 若於程式步驟1, 使用者輸入exit, 則終止本程式
'''

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

process_time_latest = [385, 400, 395, 375, 401]     
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
    sorted_process_time_latest = sorted(process_time_latest)
    if process_time < sorted_process_time_latest[2]:
        print(f"PASS：新的執行時間 {process_time} 毫秒排名前三。")
    else:
        print(f"Fail：新的執行時間 {process_time} 毫秒未能排名前三。")
    process_time_latest.append(process_time)
    print(f"更新後的執行時間列表：{process_time_latest}")
    print(f"目前前三名執行時間：{sorted(process_time_latest)[:3]}")
