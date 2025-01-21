class computador:
    def __init__(self, placa_mae, processador, memoria):
        self.placa_mae = placa_mae
        self.processador = processador
        self.memoria = memoria

    def ligar(self):
        print("Ligando...")

    def desligar(self):
        print("Desligando...")

    def mostrar_na_tela(self):
        print(f"Placa Mãe: {self.placa_mae}, Processador: {
              self.processador}, Memoria: {self.memoria}")


computador1 = computador("H110", "I5", "32GB")
computador1.ligar()
computador1.desligar()
computador1.mostrar_na_tela()
