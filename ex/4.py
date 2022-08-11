price = [57.08, 46.51, 97, 112, 100.00, 66.78, 99.22, 567, 789.99, 1000.89 ]
for g in price:
  e = int(g)
  d = round((g - int(g))*100)
  print(e,"руб","0" + str(d) if d<10 else ""+str(d),"коп")
