def fibonacci(n):
    fib = [0, 1] # Começa com os dois primeiros números da sequência
    
    for i in range(2,n):
        
        # Soma os dois números anteriores para formar o próximo
        fib.append(fib[i - 1] + fib[i - 2]) 
        
    return fib


#retonar os 10 primeiros numeros da sequencia fibonacci
print(fibonacci(50)) 
