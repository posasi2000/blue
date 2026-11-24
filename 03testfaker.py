
from faker import Faker

print('faker실습')
my = Faker()

for k in range(10):
    print(my.name())
    
print()
for k in range(10):
    print(my.ipv4_private())
print()    
    
data = Faker('ko_KR')
for k in range(10):
    print(data.name())
    
print()
for k in range(10):
    print(data.address()) 