from datetime import datetime

now= datetime.now()
birthday=datetime(1997,12,6,3,0)
while True:
    print("Та хэзээ төрснөө мэдмээр байна уу?")
    if input("Таний хариулт: ") =='Y':
        break
print(birthday)
print(birthday.weekday())
print("Таны амьдарсан цаг: "+str(now-birthday)+'\n'+"та 23 хүрэхэд "+ str(datetime(2020,12,6)-now)+" хугацаа үлдсэн байна.")

