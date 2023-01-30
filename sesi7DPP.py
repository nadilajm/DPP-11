# 1.
a = 'LUPA-LUPA INGAT'[::-1]
print(a)
print('=='*50)
# 2.
b = 'Universitas Nusa Putera'
print('Universitas Nusa Putera')
va = 0
vi = 0
ve = 0
vu = 0
vo = 0

for i in b:
    if i =='A' or i =='a':
        va += 1
    elif i == 'I' or i =='i':
        vi += 1
    elif i == 'E' or i =='e':
        ve += 1
    elif i == 'U' or i =='u':
        vu +=1
    elif i == 'O' or i =='o':
        vo += 1
    
print(f'jumlah vokal a: {va}')
print(f'jumlah vokal i: {vi}')
print(f'jumlah vokal u: {vu}')
print(f'jumlah vokal e: {ve}')
print(f'jumlah vokal o: {vo}')
print('jumlah huruf vokal:',(va)+(vi)+(vu)+(ve)+(vo))