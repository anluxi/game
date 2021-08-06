print("hallo lovely")
print("游戏\t恋爱\t猜数字")
print("""欢迎来到千华月的小家
我是这里的主人千华月
请不要搞错,华月是姓千是名""")


import random#导入伪随机库
import decimal#导入十进制库
import os#导入清屏库


three = decimal.Decimal("0.1")#将十进制状态赋值给three变量
two = random.randint(0,9)#将伪随机库内的整数随机模块赋值给two变量
love=0#好感度值初始化
one = 10#循环执行的次数初始化
game=5#好感度系统的循环次数的初始化


while one >0:#当one变量大于0时执行循环
	temp = input("请输入一个数字:")#接收用户输入的数据
	guess = int(temp)#将temp变量内的字符串转化成整数赋值给guess变量
	if guess == two:#如果guess变量等于two变量那么执行本行
		print("对了")
		 
		while game>0:
			if guess == two:
				love += 100
				aubd="好感度提升:"
				print(aubd,love)
				 
				juzi="客人,你可以走了"
				agub=juzi.replace("客人","主人")
				print(agub)

				break
		break#本行条件为真时终止循环
	else:#如果guess不等于two那么执行本行
		def lovet():
					zuji="客人,你可以走了"
					chcdd=zuji.replace("客人","白痴")
					print(chcdd) 
		lovet()
		while game>0:
			love += 20
			aujd="好感度提升:"
			print(aujd,love)
			break
		if guess > two:
			print("你的数字大了")
		else:
			print("你的数字小了")
		while game>0:
			game-=1
			dhc="你还有第"
			chc="次机会"
			print(dhc,game,chc)
			break
	one -= 1#循环次数不断减1

 
print("游戏结束\nok\n我错了再见\n拜拜")
print(r"游戏路径:/sdcard/AND")
