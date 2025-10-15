class Validar():
    def  __init__(self):
        self.con = 0

    def ValidarNumeros(self, num):
        if   self.con >= len(num):
            self.con = 0
            return True
        if ord(num[self.con]) >= 47 and ord(num[self.con]) <= 58:
            self.con += 1
            return self.ValidarNumeros(num)
        else:
            self.con = 0
            return False