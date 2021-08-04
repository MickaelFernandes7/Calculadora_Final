import re
class Calculadora :
    def __init__(self):
        self.first = 0
        self.second = 0
        print('\n ------ Calculadora ------ \n')
        self.operacao = int(input(' \n Qual operação matemática deseja realizar? \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Raiz \n 6 - Potência \n 7 - Função Matemática '))
    
        def insere_numeros():
                self.first  =  int(input('Digite o 1° Número : '))
                self.second =  int(input('Digite o 2° Número : '))

        def soma(self):
                    insere_numeros()
                    print('Soma :', self.first + self.second, '\n')
                            
        def subtracao(self):
                    insere_numeros()
                    print('Subtração : ', self.first - self.second, '\n')
                            
        def divisao(self):
                    insere_numeros()
                    print('Divisão : ', self.first / self.second , '\n')

        def multiplicacao(self):
                    insere_numeros()
                    print('Multiplicação : ', self.first * self.second, '\n')
                        
        def raiz(self):
                    insere_numeros()
                    print('Raiz Quadrada : ', self.first ** 0.5)
                    print('Raiz Quadrada : ', self.second ** 0.5, '\n')
                                
        def potencia(self):
                    insere_numeros()
                    print('Potencia :', self.first ** self.second, '\n')

        def funcaoMatematica(self):
                questao = int(input('Quantas varíaveis você deseja usar? \n 1 - Para uma \n 2 - Para duas '))
                if questao == 1 :
                        print('\n Descrição dos Operadores : \n + Soma | - Subratação | * Multiplicação | / Divisão \n')
                        print('Modelos de 1 Variável : \n (x) = x + numero\n (x) = x - numero \n (x) = x / numero \n (x) = x * numero \n')
                        
                        base = input('Digite sua função com base no modelo Que deseja : ')
                        x = int(input('Digite o valor de X : '))
                        X = str(x)
                        
                        if base[8] == '+':
                                print('(x) = x + n')
                                print(base)
                                subx = (re.sub(r'x', X, base, flags=re.I))
                                print(subx)
                                n = int(base[10:])
                                print('(x) =',x + n, '\n')

                        elif base[8] == '-':
                                print('(x) = x - n')
                                print(base)
                                subx = (re.sub(r'x', X, base, flags=re.I))
                                print(subx)

                                n = int(base[10:])
                                print('(x) = ',x - n , '\n')

                        elif base[8] == '*':
                                print('(x) = x * n')
                                print(base)
                                subx = (re.sub(r'x', X, base, flags=re.I))
                                print(subx)

                                n = int(base[10:])
                                print('(x) =',x * n, '\n')

                        elif base[8] == '/':
                                print('(x) = x / n')
                                print(base)
                                subx = (re.sub(r'x', X, base, flags=re.I))
                                print(subx)

                                n = int(base[10:])
                                print('(x) =',x / n, '\n')
                elif questao == 2:        
                        print('Modelo de 2 Variáveis : \n (x,y) = (x + y) * numero \n (x,y) = (x - y) * numero \n (x,y) = (x / y) * numero  \n (x,y) = (x * y) * numero \n' )
                        
                        base = input('Digite sua função com base no modelo Que deseja : ')
                        x = int(input('Digite o valor de X : '))
                        y = int(input('Digite o valor de Y : '))
                        X = str(x)
                        Y = str(y)

                        if base[11] == '+':
                                print('(x,y) = (x + y) * numero')
                                print(base)

                                subx = (re.sub(r'x', X, base, flags=re.I))
                                suby = (re.sub(r'y', Y, subx, flags=re.I))
                                print(suby)

                                n = int(base[18:])
                                print('(x,y) = ', (x + y) * n)
                                
                        elif base[11] == '-':
                                print('(x,y) = (x - y) * numero')
                                print(base)
                                
                                subx = (re.sub(r'x', X, base, flags=re.I))
                                suby = (re.sub(r'y', Y, subx, flags=re.I))
                                print(suby)

                                n = int(base[18:])
                                print('(x,y) = ', (x - y) * n)
                                
                        elif base[11] == '/':
                                print('(x,y) = (x / y) * numero')
                                print(base)

                                subx = (re.sub(r'x', X, base, flags=re.I))
                                suby = (re.sub(r'y', Y, subx, flags=re.I))
                                print(suby)
                                
                                n = int(base[18:])
                                print('(x,y) = ', (x / y) * n)
                                
                        elif base[11] == '*':
                                print('(x,y) = (x * y) * numero')
                                print(base)

                                subx = (re.sub(r'x', X, base, flags=re.I))
                                suby = (re.sub(r'y', Y, subx, flags=re.I))
                                print(suby)
                                
                                n = int(base[18:])
                                print('(x,y) = ', (x * y) * n)
                else:
                        print('Opção Inválida. Digite 1 ou 2')        


        if self.operacao == 1:
                soma(self)
        elif self.operacao == 2:
                subtracao(self)
        elif self.operacao == 3:
                divisao(self)
        elif self.operacao == 4:
                multiplicacao(self)
        elif self.operacao == 5:
                raiz(self)
        elif self.operacao == 6:
                potencia(self)
        elif self.operacao == 7:
                funcaoMatematica(self)
