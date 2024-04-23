import os

def change_text_color(color_code):
    color_codes = {
        1: "blue",
        2: "purple",
        3: "white",
        4: "pink"
    }

    if color_code in color_codes:
        color = color_codes[color_code]
        os.system(f'termux-style -c {color}')
        print(f"Cor do texto alterada para {color}")
    else:
        print("Opção inválida. Escolha um número de 1 a 4 para selecionar a cor.")

def main():
    print("Escolha uma cor para o texto:")
    print("1- Blue")
    print("2- Purple")
    print("3- White")
    print("4- Pink")

    color_choice = int(input("Digite o número da cor desejada: "))

    change_text_color(color_choice)

if __name__ == "__main__":
    main()