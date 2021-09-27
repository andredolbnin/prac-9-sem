input_number = eval(input())
divisor = 2
while divisor ** 2 <= input_number:
    processing_number = input_number
    while processing_number % divisor == 0:
        processing_number //= divisor
    if processing_number == 1:
        print('YES')
        break
    divisor += 1
else:
    print('NO')

