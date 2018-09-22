# print("""\
# Menu:
# 1 - Apagar
# 2 - Editar
# 3 - Excluir
#                """)
#
# a = "Alex"
# b = "Emanuel"
#
# print(f"{a} {b}")

#máximo 79 caracteres por linha
#nomear claramente as funções e classes (Classes = PrimeiroNome) / (Função = primeiro_nome)

#while / break / else

# *args **kwargs

# """Funcion Doc""

# if not type(x) in [float, int] = assert TypeError("Erro no tipo ai")




class Calc:

    def add(self, x, y):
        """Add Function"""

        if y < 1:
            return None

        return x + y


    def sub(self, x, y):
        """Subtract Function"""

        return x - y



    def divi(self, x, y):
        """Divide Function"""

        if y == 0:
            raise ValueError("Can not divide by ZERO")

        return x / y













