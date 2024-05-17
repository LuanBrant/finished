import math

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcular_volume_cubo(lado):
    return lado ** 3

def calcular_volume_esfera(raio):
    return (4 / 3) * math.pi * raio ** 3

def main():
    print("Bem-vindo ao calculador de áreas e volumes de formas geométricas!")
    print("Escolha a forma que deseja calcular:")
    print("1. Retângulo")
    print("2. Triângulo")
    print("3. Círculo")
    print("4. Cubo")
    print("5. Esfera")

    escolha = int(input("Digite o número correspondente à forma desejada: "))

    if escolha == 1:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = calcular_area_retangulo(base, altura)
        print(f"A área do retângulo é: {area}")
    elif escolha == 2:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"A área do triângulo é: {area}")
    elif escolha == 3:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo é: {area}")
    elif escolha == 4:
        lado = float(input("Digite o lado do cubo: "))
        volume = calcular_volume_cubo(lado)
        print(f"O volume do cubo é: {volume}")
    elif escolha == 5:
        raio = float(input("Digite o raio da esfera: "))
        volume = calcular_volume_esfera(raio)
        print(f"O volume da esfera é: {volume}")
    else:
        print("Escolha inválida. Por favor, selecione um número entre 1 e 5.")

if __name__ == "__main__":
    main()