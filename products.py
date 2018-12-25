from datetime import date

today = str(date.today())

print("這是個記帳軟體，請依照指示輸入，或輸入q離開。")
products = []
products.append(["日期", "商品", "價格", "\n"])
while True:
	date = input("請輸入日期(EX, 2018-01-01)，或按Enter直接取得今天日期： ")
	if date == "q":
		break
	elif date == "":
		date = today
	print("你輸入的是 ", date)
	name = input("接著請輸入商品名稱： ")
	if name == "q":
		break
	elif name == "":
		name = "未購買"
	print("你輸入的是 ", date, ":", name)
	price = input("最後請輸入商品價格： ")
	if price == "q":
		break
	elif price == "":
		price = 0
	price = int(price)
	products.append([date, name, price])
	print("你輸入的是 ", date, ":", name, "的價格是", price, "元")
	print("\n")

print(products)

for p in products:
	print(p[0], p[1], "的價格是", p[2], "元")

with open("products.csv", "w") as f:
	for p in products:
		f.write(p[0] + "," + p[1] + "," + str(p[2]) + "\n")
		#write 通常會跟著 \n