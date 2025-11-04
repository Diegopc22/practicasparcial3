class validar():
    def __init__(self):
        self.con = 0
    def ValidarNumeros(self,num):
        if self.con >= len(num):
            self.con = 0
            return True
        if ord(num[self.con])>=47 and ord(num[self.con])<=58:
            self.con +=1
            return self.ValidarNumeros(num)
        else:
            self.con = 0
            return False
    def ValidarLetra(self, dato):
        if dato == "":
            return True
        if ord(dato[0])>=65 and ord(dato[0])<=90 or ord(dato[0])>=97 and ord(dato[0])<=122 or ord(dato[0]) == 32:
            return self.ValidarLetra(dato[1:])
        else:
            return False
        
    def ValidarEntradas(self,dato):
        if dato=="":
            return False
        
        if len(dato) == 2:
            return True
        else:
            return False