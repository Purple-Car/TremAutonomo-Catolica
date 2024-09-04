class Train:
    def __init__(self):
        self.position = 0
        self.movements = 0
        self.consecutive_movements = 20
        self.last_command = None

    def move(self, command_list):
        for command in command_list:
            if self.movements >= 50:
                print("Limite de 50 movimentos.")
                break

            if command == self.last_command:
                self.consecutive_movements += 1
                if self.consecutive_movements > 20:
                    print("Limite de 20 movimentos consecutivos atingido")
                    break
            else:
                self.consecutive_movements = 1

            if command == "ESQUERDA" and self.position >= 1:
                self.position -= 1
            if command == "DIREITA":
                self.position += 1

            self.movements += 1
            self.last_command = command

        print(f"O trem está na posição {self.position}")
        return self.position


def get_commands():
    run_input = True
    commands_list = []

    while run_input == True:
        # Receber comando [ESQUERDA, DIREITA, ENVIAR, CANCELAR]
        user_input = input("Insira um comando válido: ")

        match user_input:
            # Definir quantidade de movimento, caso comando seja uma direção
            case "ESQUERDA" | "DIREITA":
                quantity = quantity_input()
                commands_list.extend([user_input] * quantity)

            # Validar caso comando seja 'ENVIAR'
            case "ENVIAR":
                # print(commands_list)
                return commands_list

            # Validar caso comando seja 'CANCELAR'
            case "CANCELAR":
                return "Movimentação cancelada."

            # Caso comando inválido
            case _:
                print("Comando inválido, tente escrever um dos comandos a seguir:")
                print("'ESQUERDA' ou 'DIREITA' para selecionar uma direção;")
                print(
                    "'ENVIAR' para enviar a lista atual de comandos para o sistema do trem;"
                )
                print("'CANCELAR' para descartar a lista atual de comandos.")


# Função que exige um input the int e retorna apenas um valor válido
def quantity_input():
    while True:
        quantity = input(
            "Insira a quantidade de vezes seguidas que o Trem deverá virar essa direção: "
        )

        try:
            quantity = int(quantity)

            if quantity < 0:
                print("Insira um valor positivo! O Trem não deve andar para trás!")
            else:
                return quantity

        except ValueError:
            print("O número inserido não é um número, insira um número válido!")


def main():
    print("'ESQUERDA' ou 'DIREITA' para selecionar uma direção;")
    print("'ENVIAR' para enviar a lista atual de comandos para o sistema do trem;")
    print("'CANCELAR' para descartar a lista atual de comandos.")
    train = Train()
    run_finished = True
    while run_finished:
        commands = get_commands()
        train.move(commands)

        continuar = input("Deseja enviar mais uma lista de movimentos? (S/N): ").upper()
        if continuar == "N":
            run_finished = False
            print("Encerrando o programa.")
        elif continuar != "S":
            print("Entrada inválida. Encerrando o programa por segurança.")
            run_finished = False


if __name__ == "__main__":
    main()
