from gerenciador_produtos import*
from product import*
from itempedido import*


class Carrinho:
    serial_pedido = 0
    def __init__(self):
        self.carrinho = {}
        Carrinho.serial_pedido+= 1
        self.id_pedido = Carrinho.serial_pedido
    

    def adicionar_itens(self,gerenciador,id,quant):
        itens = gerenciador.pesquisar(id)

        if carrinho:
            self.carrinho[id]= itemPedido(id,quant)
            print(f"{quantidade} unidade(s) de '{produto.descricao}' adicionada(s) ao carrinho.")
        else:
            (f'Produto não encontrado!')
        return self.carrinho

    