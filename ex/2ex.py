import re

a = [
    'в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5',
    'градусов'
]

res_arr = []

for i in a:
  b = re.findall('(\d+)', i)
  if(len(b) > 0):

    res_arr.append('"')
    res_arr.append(i.replace(b[0], "0" + b[0] if int(b[0]) < 10 else "" + b[0]))
    res_arr.append('"')

  else:
    res_arr.append(i)  

print(res_arr)

print((" ".join(res_arr)))
