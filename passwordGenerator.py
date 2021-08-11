from secrets import choice, randbelow
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
charList=[]
for l in range(0, len(chars)):
    charList.append(chars[l])
del(chars)
minLength=int(input('Min. Length >>>'))
maxLength=int(input('Max. Length >>>'))
length=randbelow(maxLength-minLength)
del(maxLength)
del(minLength)
password=''
for l in range(0, length):
    password+=choice(charList)
del(length)
print('Password: '+password)
del(password)