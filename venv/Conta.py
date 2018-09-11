class Conta():
    
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero;
        self.cliente = cliente;
        self.saldo = saldo;
        self.limite = limite;
    def depositar(self, deposito):
        self.saldo += deposito;
    
    def sacar(self, saque):
        if self.limite+self.saldo < saque:
            self.saldo -= saque
        else:
            return None
    
    def transferencia(self, valor):
        if self.limite + self.saldo < valor:
            self.saldo -= valor
            return valor
        else:
            return None
            
            
            
