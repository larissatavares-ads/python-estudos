a='Hello,World!'
print(a[1],a[5],a[9])
print(a[1:4])
print(a[:5])
print(a[6:])
print(a[-4:-1])

for x in "banana":
    print(x)


a='hello world'
print(len(a))


txt="The best things in life are free!"
print("free" in txt)

if("free" in txt):
    print("presente")

if("frtt" not in txt):
    print("nao presente")

txt="   The best things in life are free!  "
print(txt.upper())
print(txt.strip())
print(txt.replace("b","wwww"))
print(txt.split(" "))


quantity = 40
itemno = 10
price = 23.6
order = "Quero {2} peças do item {0} de R$ {1}"
print(order.format(quantity,itemno,price))


vikings = "Somos \"Vikings\" do norte"
print(vikings)
vikings = "Somos \"Vikings\" \ndo norte"
print(vikings)
vikings = "Somos \"Vikings\" do \rnorte"
print(vikings)
vikings = "\tSomos \"Vikings\" do norte"
print(vikings)
vikings = "Somos \"Vikings\" do \bnorte"
print(vikings)
vikings = "Somos \"Vikings\" do n\forte"
print(vikings)
vikings = "\123\157\155\157\163\40\126\151\153\151\156\147\163\40\144\157\40\156\157\162\164\145"
print(vikings)
vikings = "\x53\x6f\x6d\x6f\x73\x20\x56\x69\x6b\x69\x6e\x67\x73\x20\x64\x6f\x20\x6e\x6f\x72\x74\x65"
print(vikings)