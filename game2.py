import random#导入伪随机库
import decimal#导入十进制库,未使用
import os#导入清屏库,未使用
import time#导入时间库


print("你好")
time.sleep(1)
print("游戏\t恋爱\t猜数字")
time.sleep(1)
print("以上，就是游戏的大概内容。那么，欢迎光临")
time.sleep(1)


suijizhi,lovezhi,shuruci,loveci,gongwei=random.randint(0,9),50,10,5,"客人，你可以走了"
print(suijizhi,lovezhi,shuruci,loveci,gongwei)


def lovezhen():
 quanju=gongwei.replace("客人","主人")
 print(quanju)
 time.sleep(1)

def lovejia():
 erquanju=gongwei.replace("客人","白痴")
 print(erquanju)
 time.sleep(1)

def lovexitongjia():#暂时用不上此函数在
 while loveci>0:
  lovezhi-=10
  tishier="好感度提升"
  print(tishier,lovezhi)
  time.sleep(1)
  break

def lovetixing():
 while loveci>0:
  loveci-=1
  tixing0="你还有第"
  tixibg1="次机会"
  print(tixing0,loveci,tixing1)
  time.sleep(1)
  break


while shuruci>0:
 shuruzhi=input("请输入一个数字")
 zhengsu=int(shuruzhi)
 if zhengsu==suijizhi:
  print("回答正确")
  time.sleep(1)
  while loveci>0:
   if zhengsu==suijizhi:
    lovezhi+=100
    tishi="好感提升"
    print(tishi,lovezhi)
    time.sleep(1)
    lovezhen()
    break
  break
 else:
  lovejia()
  while loveci>0:
   lovezhi-=10
   tishier="好感度提升"
   print(tishier,lovezhi)
   time.sleep(1)
   break
  if zhengsu>suijizhi:
   print("数字大了哦")
   time.sleep(1)
  else:
   print("数字小了哦")
   time.sleep(1)
   lovetixing()
shuruci-=1


print("游戏结束\nok\n我错了再见\n拜拜")
time.sleep(1)
print(r"游戏路径:/sdcard/AND")