def chocolate_piles(n):
    piles = []
    first = n
    first = piles.append(first)

    step = 2
    for i in range(1,n):
        piles.append(piles[-1]+step)
    return piles
n = int(input("Enter number of piles: "))
result = chocolate_piles(n)
print("Chocolates in pile:", result)