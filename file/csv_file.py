import csv

lunch = {
    "BBQ" : "123123",
    "중국집" : "544658",
    "교촌" : "157538"
}


with open("lunch.csv", 'w', encoding="utf-8", newline="") as f : # 인코딩은 파일형식을 바꿔주는것. 우리는 utf를 많이 씀
    csv_writer = csv.writer(f)    # 파일을 연걸 너가 write

    for item in lunch.items():
        csv_writer.writerow(item)   #csv_writer야 item좀 write
        