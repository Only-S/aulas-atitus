class CaixaRegistradora:
    def __init__(self):
        self._total_venda = 0
        self._numero_itens = 0

    @property
    def total_venda(self):
        return self._total_venda

    @total_venda.setter
    def total_venda(self, valor):
        print("Proibido alterar o total venda!")

    @property
    def numero_itens(self):
        return self._numero_itens

    @numero_itens.setter
    def numero_itens(self, valor):
        print("Proibido alterar o numero itens!")

    def add_item(self, preco, quantidade):
        self._total_venda += preco * quantidade
        self._numero_itens += quantidade

    def finalizar_venda(self):
        print("Obrigado por comprar conosco!")
        print(f"Foram comprados {self._numero_itens} itens")
        print(f"TOTAL: R${self._total_venda:.2f}")
        print("=" * 50)

        self._total_venda = 0
        self._numero_itens = 0
        self.itens_vendas += self.numero_itens

## Programa Principal
mercado = CaixaRegistradora()

mercado.add_item(1.5, 5)

print(mercado.total_venda)
print(mercado.numero_itens)
mercado.total_venda = -0.5
mercado.numero_itens = -10

