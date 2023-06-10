
#uma tupla é uma coleção ordenada e imutável

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)



fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(type(green))
print(yellow)
print(red)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])