import os

os.chdir(r"C:\Users\student\startcamp\students") #  r(raw) 날것의 의미
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUMG_","SSAFY_"))