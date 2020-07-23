def fibonacci_seq(n):
    
    prev_res = 0
    fib = 1
    print(fib)
    while n > 0:
        print(fib)
        prev_res = fib - prev_res
        fib = fib + prev_res
        n -= 1
        
    

fibonacci_seq(50)



