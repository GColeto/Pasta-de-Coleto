print("Esse programa é uma calculadora básica com as seguintes operações:")

print("Soma.............+")
print("Subtração........-")
print("Multiplicação....*")
print("Divisão........../")
 
while True:
    op = input("Digite 0 para sair, ou escolha uma das operações (+, -, * /): ")
     
    if op.lower() == '0':
        break
 
    if op not in '+-*/0':
        print('Inválido')        
        continue
 
    n1 = float(input('Digite o primeiro  número: ')) 
    n2 = float(input('Digite o segundo número: ')) 
  
    if op == '+': 
        soma = n1 + n2
        print('A soma de ',n1, ' e ', n2,' é ', soma)
  
    elif op == '-': 
        sub = n1-n2
        print('A subtração de', n1, 'e', n2, 'é', sub)
  
    elif op == '*':  
        mult = n1*n2  
        print('A multiplicação de', n1, 'e', n2, 'é', mult)
  
    elif op == '/': 
  
        if n2 == 0: 
            print('Você não pode dividir um número por zero.')
  
        else: 
            div = n1/n2 
            divis = format(div, '.2f') 
            print('A divisão de', n1, 'por', n2, 'é', div)
  
  
  
    else:
        print('Operação inválida.')
 

    


           
