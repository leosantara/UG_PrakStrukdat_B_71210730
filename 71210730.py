nilai = input()
while nilai != 'Q' :
    if '+' in nilai :
        nilai.split('+')
        z = int(nilai[0])+int(nilai[2])
        print(z)
    if '-' in nilai :
        nilai.split('-')
        z = int(nilai[0])-int(nilai[2])
        print(z)
    if '/' in nilai :
        nilai.split('/')
        z = int(nilai[0])/int(nilai[2])
        print(z)
    if '*' in nilai :
        nilai.split('*')
        z = int(nilai[0])*int(nilai[2])
        print(z)
    nilai = input()
exit()