class Calculatrice:  
    o = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/'}  
    
    # Constructor  
    def __init__(self, a, b):  
        self.a = a  
        self.b = b  
        #self.o = o  

    def verif_float(self, x):  
        try:  
            x = float(x)  
            return True  
        except ValueError:  
            print(f"Error value '{x}' is not real member: type a real numeric variable no letters")  
            return False  

    def verif_0(self):
        try:
            x = float(self.a)/float(self.b)
            return True
        except ZeroDivisionError:  
            print("Error : Division by zero is not allowed. ")
            return False

    def verif_o(self, x):
        if x in self.o.values() :
            return True
        else :
            print("Error: Operation not found in Calculator list")
            return False

    
    
    def calcul(self, x) :
        try :
            if self.verif_float(self.a) == True & self.verif_float(self.b) == True :
                print('Check types validate')
        
                if self.verif_o(x) == True :
                    print('Verification operation validate', x)
            
                    if x == '/' :
                        print('Decision choice is /')
                        if self.verif_0() == True :
                            print('Division is possible second value different from 0')
                    
                    expression = f"{float(self.a)} {x} {float(self.b)}"
                    z = eval(expression)
                    print(z)
        except ZeroDivisionError :
            print('Error')