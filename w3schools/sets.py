
#sets são coleções não ordenadas e imutáveis

thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2}
#true e 1 são considerados iguais
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


thisset = {"apple", "banana", "cherry"}
# pop remove um item aleatório
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)