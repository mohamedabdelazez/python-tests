import sys
import time
o = open("C:\\Users\Mohamed\Desktop\s.txt", encoding='utf8')
o2 = open("C:\\Users\Mohamed\Desktop\calp.txt", encoding='utf8')
names = o.readlines()
h = """
          ......       ......
        .:oOOOOo:.   .:oOOOOo:.
      .:oOO:'':Oo:. .:oO:'':OOo:.
     .:oO:      'Oo:oO'      :Oo:.
     :oO:         'o'         :Oo:
     :oO:                     :Oo:
     ':oO:     HAPPY EID      :Oo:'
      ':oO:                 :Oo:'
        ':oO.             .Oo:'
          ':oO.         .Oo:'
            ':oO.     .Oo:'
              ':oO. .Oo:'
               'oO:Oo'
                 'oOo'
                  'o'

"""

print(h)
v= o2.readlines()
print(v)
for i in names:
    time.sleep(3)
    print("عيد سعيد عليك يا "+i)


