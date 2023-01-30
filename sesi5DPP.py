# no 1
nama = input('Nama:')
Kelas = input('Kelas:')
nim= input ('NIM:')
print(f' biodata sederhana  {nama},{Kelas},{nim}')

#  no 2
a ='UNIVERSITAS NUSA PUTRA SUKABUMI'
# a. 
x = a.lower()
y = x.split()
print(y[2]+' '+y[1])
#b
print(a[1:11] +' ' + a[12]+a[14:16]+' '+a[17]+a[19:22]+' '+a[23]+a[25:28]+a[29:31])
# c
y = a.split()
z = list(y)
z.reverse()
for a in z:
    print(a,end=' ')
print()
# d
a ='UNIVERSITAS NUSA PUTRA SUKABUMI'
y = a.split()
z = list(y)
for i in z:
    print(i[0],end='')

print()
# e
y = a.split()
z = list(y)
print(z[0][-3:], z[1][-2:]+z[2][0:2],z[3][-4:],end=' ')