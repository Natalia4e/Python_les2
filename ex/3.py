staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in staff:
 words = i.split(" ")
 name = words[len(words)-1]
 print("Привет, " + name.capitalize())
