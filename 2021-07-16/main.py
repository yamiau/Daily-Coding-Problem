from random import randint

deck = [( str(i + 1) + chr(j+35) ) for i in range(13) for j in range(4)]
print("Ordered deck:")
print(deck)
k = len(deck) - 1

while k > 0:
    j = randint(1, k)
    cardK = deck[k]
    deck[k] = deck[j]
    deck[j] = cardK
    k -= 1

print("Shuffled deck:")
print(deck)