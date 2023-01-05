import math
pi = math.pi
print("DESCUBRA O QUE QUISER DE UM CÍRCULO")
while True:
    print("\nDigite o número que antecede a opção que deseja saber ")
    resposta = str(input("[ 0 ] Raio \n[ 1 ] Diâmetro \n[ 2 ] Circunferência \n[ 3 ] Área\n"))


    if resposta[0] in '0':
        print("Descobrir o raio? Através de que forma deseja descobrir o valor do raio? Digite a letra que antecede a opção desejada: ")
        resraio = str(input("[ D ] Diâmetro \n[ C ] Circunferência \n[ A ] Área \n ")).upper()
        if resraio[0] in 'D':
            diametro = float(input("Digite o valor do diâmetro para descobrir o raio: "))
            raio = diametro/2
            print(f"O valor do raio é igual a {raio}")
            print("Dica: Para descobrir o raio, divida o valor da circunferência por 2")
        if resraio[0] in 'C':
            circunferencia = float(input("Digite o valor da circunferência para descobrir o raio: "))
            raio = circunferencia/(2*pi)
            print(f"Se a circunferência do círculo vale {circunferencia}, o valor do raio é {raio:.2f}")
        if resraio[0] in 'A':
            area = float(input("Digite o valor da área: "))
            raio =   math.sqrt(area/pi)
            print(f"Se a área vale {area}, o valor do raio é igual a {raio:.2f}")


    if resposta[0] in '1':
        print("Descubra o valor do diâmetro! Através de qual medida quer descobrir o diâmetro? Digite a letra que antecede a opção desejada: ")
        resdia = str(input("[ R ] Raio\n[ C ] Circunferência\n[ A ] Área\n")).upper()
        if resdia[0] in 'R':
            raio = float(input("Digite o valor do raio: "))
            diametro = raio*2
            print(f"O Diâmetro vale {diametro}, uma vez que o raio vale {raio}")
        if resdia[0] in 'C':
            circunferencia = float(input("Digite a circunferência do círculo: "))
            diametro = circunferencia/pi
            print(f"O diâmetro vale {diametro:.3f}, já que a circunferência vale {circunferencia}")
        if resdia[0] in 'A':
            area = float(input("Digite o valor da área: "))
            diametro = (math.sqrt(area/pi)) * 2
            print(f"Uma vez que a área é igual {area}, o diametro é igual a {diametro:.2f}")


    if resposta[0] in '2':
        print("Escolha a opção que deseja para descobrir a medida da circunferência: ")
        rescir = str(input("[ R ] Raio\n[ D ] Diâmetro\n[ A ] Área\n")).upper()
        if rescir[0] in 'R':
            raio = float(input("Digite o valor do raio: "))
            circunferencia = 2*raio*pi
            print(f"O valor da circunferência é {circunferencia:.2f}, baseando-se que o raio tenha o valor de {raio}")
        if rescir[0] in 'D':
            diametro = float(input("Digite o valor do diâmetro: "))
            circunferencia = diametro*pi
            print(f"Se o diâmetro vale {diametro}, a circunferência valerá {circunferencia:.2f}")
        if rescir[0] in 'A':
            raio = 0
            area = float(input("Digite o valor da área do círculo: "))
            raio = math.sqrt(area/pi)
            print(f"O raio vale {raio:.4f}")
            circunferencia = 2*pi*raio
            print(f"Se a área vale {area}, o raio será igual a {raio:.4f} e consequentemente a circunferência medirá {circunferencia:.3f}")


    if resposta[0] in '3':
        print("Através de qual opção quer descobrir o valor da área? Digite a letra que antecede a opção desejada: ")
        resarea = str(input("[ R ] Raio\n[ D ] Diâmetro\n[ C ] Circunferência\n")).upper()
        if resarea[0] in 'R':
            raio = float(input("Digite o valor do raio: "))
            area = pi * math.pow(raio, 2)
            print(f"Com o raio sendo {raio}, a área será igual a {area:.3f}")
        if resarea[0] in 'D':
            diametro = float(input("Digite o diâmetro: "))
            raio = diametro/2
            area = pi * math.pow(raio, 2)
            print(f"Se o diâmetro é {diametro}, a área será {area:.3f}")
        if resarea[0] in 'C':
            circunferencia = float(input("Digite o valor da circunferência: "))
            raio = circunferencia/(2*pi)
            area = pi * math.pow(raio, 2)
            print(f"Se a circunferência vale {circunferencia}, o raio será {raio:.3f} e a área será igual a {area:.3f}")


    sim = str(input("Quer contiunuar? [S/N] ")).upper()
    while sim[0] not in 'NS':
        sim = str(input("Quer continuar? [S/N] ")).upper()
    if sim[0] in 'N':
        break
    if sim[0] in 'S':
        True
print("FIM DO PROGRAMA")
