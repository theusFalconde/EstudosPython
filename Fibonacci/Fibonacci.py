#Fibonacci.py

def calculaFibonacci(num,nterms):
    try:
        n1 = 0
        n2 = num
        count = 0
        if nterms <= 0:
           print("Digite apenas numeros Positivos")
        elif nterms == 1:
           print("Sequencia de ",nterms,": ")
           print(n1)
        else:
           print("Sequencia de ",nterms,": ")
           while count < nterms:
               print(n1,end=' , ')
               nth = n1 + n2
               n1 = n2
               n2 = nth
               count += 1
    except :
        print("Apenas numeros :)")