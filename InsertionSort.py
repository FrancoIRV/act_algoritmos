numbers = [13,15,4,2,8,9,6]
for i in range (1,len(numbers)):
    valorActual = numbers[i]
    index = i
    while index >    0 and valorActual < numbers[index-1]:
            numbers[index] = numbers[index-1] 
            index = index -1
    numbers[index] = valorActual

print(numbers)
