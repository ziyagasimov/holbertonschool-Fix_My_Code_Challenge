def fizzbuzz(n):
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        # Check the combined condition FIRST
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    
    # Using print(*tmp_result) is also a neat way to print space-separated values
    print(" ".join(tmp_result))
