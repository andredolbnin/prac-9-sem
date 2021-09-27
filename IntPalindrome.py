input_number = eval(input())
processing_number = input_number
result_number = 0
if input_number % 10 == 0:
    print('NO')
else:
    while processing_number != 0:
        result_number *= 10
        result_number += processing_number % 10
        processing_number //= 10
    if result_number == input_number:
        print("YES")
    else:
        print("NO")
