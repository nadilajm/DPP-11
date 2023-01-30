



# sesi 6
umur = int(input('umur berapa:'))

if umur <= 2 :
    print('dilarang masuk!')
elif umur >= 2 or umur <= 4 :
    Tb = int(input('berapa tinggi badan :'))
    if Tb <= 70:
        print('30.000')
    else:
        print('40.000')
elif umur>= 4 or umur <= 7 :
    Tb = int(input('berapa tinggi badan :'))
    if Tb < 129:
        print('40.000')
    else:
        print('55.000')
elif umur >= 7 or umur <= 10 :
    Tb = int(input('berapa tinggi badan :'))
    if Tb <= 150:
        print('50.000')
    else:
        print('70.000')
else:
    print('80.000')        
print('='*50)



#------
print('''option olahraga :
a. pushup
b. lari
c. plank
d. pushup dan lari
e. pushup dan plank
f. lari dan plank
g. pushup, lari dan plank''')

lari = 12
pushup = 6.67
plank = 5

a = str(input('olahraga apa:'))
b = int(input('berapa menit:'))
if a == 'a':
    print (lari*b, 'kalori')
elif a == 'b':
    print(pushup* b,'kalori')
elif a == 'c':
    print(plank*b, 'kalori')
elif a == 'd':
    print((pushup*b)+(lari*b),'kalori')
elif a == 'e':
    print((pushup*b)+(plank*b),'kalori')
elif a == 'f':
    print((plank*b)+(lari*b),'kalori')
elif a == 'g':
    print((pushup*b)+(lari*b)+(plank*b),'kalori')
    
