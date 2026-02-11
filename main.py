from calculadora import soma

#print(soma(-10,20))
#print(soma(0.5,9.5))
try:
    print(soma('1',10))
except AssertionError as e:
    print(f'Conta inválida, {e}')

