
class Numeros:
    def __init__(self):
        self.numeros = []

    def pedirnum(self, cantidad):
        for _ in range(cantidad):
            numero = int(input("Ingrese un numero: "))
            self.numeros.append(numero)

    def ordena(self):
        self.numeros.sort()

    def mostrarpi(self):
        pares = []
        impares = []

        for num in self.numeros:
            if num % 2 == 0:
                pares.append(num)
            elif num % 2 != 0:
                impares.append(num)

        if pares:
            print("pares:", pares)

        if impares:
            print("impares:", impares)

    def mostrepetidos(self):
        repetidos = {}
        for num in self.numeros:
            if num in repetidos:
                repetidos[num] += 1
            else:
                repetidos[num] = 1

        for num, c in repetidos.items():
            if c > 1:
                print(f"Repetidos{num}={c}")

def main():
    cantidad_numeros = int(input("Cuantos numeros : "))
    obj = Numeros()
    obj.pedirnum(cantidad_numeros)
    obj.ordena()
    print("\nOrden:")
    print(obj.numeros)
    obj.mostrarpi()
    obj.mostrepetidos()

if __name__ == "__main__":
    main()
