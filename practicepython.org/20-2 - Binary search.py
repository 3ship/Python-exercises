def elementSearch(numbers, element):
    if len(numbers) <= 2:
        if element in numbers:
            print('Number found.')
            exit()
        else:
            print('Not found.')
            exit()
    half = int(len(numbers) / 2)
    if element == numbers[half]:
        print('Number found.')
    else:
        cutInHalf(numbers, half, element)
        
def cutInHalf(numbers, half, element):
    if element < numbers[half]:
        numbers = numbers[:half]
    else:
        numbers = numbers[half:]
    elementSearch(numbers, element)
        

if __name__=="__main__":
    numbers = [2, 3, 5, 6, 9, 10, 14, 16, 56]
    element = int(input('Insert number: '))
    elementSearch(numbers, element)