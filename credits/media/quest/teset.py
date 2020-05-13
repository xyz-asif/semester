'''
#list
def list():
    goods = ['asif','fulla','peerusab','shaik','khan','enna']
    nums = [1,2,3,4,5,7,6,876,5,22]
    a = goods.pop(2)
    b = goods.remove('asif')
    c = goods.append("well")
    d = goods.index('khan')
    e = len(goods)
    g = goods[2]
    f = nums + goods
    print(a,b,c,d,e,f,g)


#dicts ...these are all about keys
def dicts():
    pidlist = {"Smith,Mary":"P12345", "Doe,John":"P12346", "Jones,Charlie":"P12347"}
    #all about key..wanto acces ? [key],wanna del [key],add..? [key] and value
    a = pidlist["Smith,Mary"]
    del(pidlist["Doe,John"])
    pidlist["Jones,Charlie"] = "P55555"


#func
def name(name):
    print("my name is" , name)

#name('asif')

def age(age):
    x = 1 + age
    return x

msg = ''
 
while msg != 'quit':

    msg = input("What's your message? ")


class girl():
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def walk(self):
        print('walking...')

rashi = girl('rashika',21,'whiter')
print(rashi.age)
rashi.walk()
'''


lis = ["asif",12,"rool"]
lis.append(45)
lis.remove(12)
x = lis.pop(2)
print(lis)
