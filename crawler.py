import csv
import requests
from bs4 import BeautifulSoup

# TODO: 多行內容在CSV不適用
# TODO: 有多筆網址匹配不到內容，待檢查
with open('tbrain_train_final_0610.csv', newline='', encoding="utf-8") as csvfile:
    
    rows = csv.reader(csvfile)
    for row in rows:
        head = row
        break 
# load csv
## 開啟 CSV 檔案
with open('tbrain_train_final_0610.csv', newline='', encoding="utf-8") as csvfile:

    # 建立自己的 CSV 檔
    new_csv_path = "after_crawler.csv"
    with open(new_csv_path,'w', newline='', encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_head = head
        csv_write.writerow(csv_head)

    # 讀取 CSV 檔案內容
    rows = csv.DictReader(csvfile)

    # 以迴圈輸出每一列
    i = 0
    for row in rows:
        i += 1

        news_ID = row['news_ID']
        hyperlink = row['hyperlink']
        content = row['content'].split(' ### 省略內文 ### ')
        name = row['name']

        r = requests.get(hyperlink) #將此頁面的HTML GET下來
        # print(r.text) #印出HTML
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser        

        text =  ''.join([tag.text for tag in soup.find_all("p")])

        start_index = text.find(content[0])
        end_index = text.find(content[1])

        if start_index != -1 and end_index != -1:
            content = text[start_index:end_index] + content[1]
        else:
            content = row['content']

        news_ID,hyperlink,content,name
        with open(new_csv_path,'a+', newline='', encoding="utf-8") as f:
            csv_write = csv.writer(f)
            data_row = [news_ID, hyperlink, content, name]
            csv_write.writerow(data_row)

        if i == 5:
            break
