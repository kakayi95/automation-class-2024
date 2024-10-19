# %%
# ====== 練習2: 難度-中高 ======
'''
responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]
# 以下程式可依橫列順序執行
for responses in responses_new:
    for response in responses:
        print(response)

# 請撰寫一程式, 改為依直排順序執行, 意即按以下順序輸出
# 200 400 500 201 401 502 404 503
'''

# Version 1
responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]

current_col = 0
row_count = len(responses_new)
last_row_index = row_count - 1
last_row_col_index = len(responses_new[last_row_index]) - 1

while True:
    for row in range(row_count):
        last_col_index = len(responses_new[row]) - 1
        if current_col <= last_col_index:
            print(responses_new[row][current_col])
    if current_col == last_row_col_index:
        break
    current_col += 1
    
# Version 2   
responses = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]

col = 0
rows = len(responses)
max_col = len(responses[-1]) - 1

while col <= max_col:
    for row in range(rows):
        if col < len(responses[row]):
            print(responses[row][col], end=' ')
    col += 1