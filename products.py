products = []
while True:
	name = input("請輸入商品名稱： ")
	if name == "q":
		break
	price = input("請輸入商品價格： ")
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	products.append([name, price])
print(products)

products[0][0]

for p in products:
	print(p[0], "的價格是", p[1])

with open("products.csv", "w") as f:
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")
		#write 通常會跟著 \n