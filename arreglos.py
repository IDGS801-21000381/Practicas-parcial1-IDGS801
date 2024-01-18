class Arreglos:
    def imprimir(self, num):
        for i in range(1, num + 1):
            print('*' * i)

def main():
    obj = Arreglos()
    num = int(input("Ingrese un número: "))
    obj.imprimir(num)

if __name__ == "__main__":
    main()
