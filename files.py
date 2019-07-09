from faker import Faker
import os

f = Faker('ko_KR') # 한국어 버전

for i in range(100):
    filename = f"{i}_{f.name()}.txt"
    cmd = f"touch {filename}"
    os.system(cmd)