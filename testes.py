from pessoa import Pessoa
from cadastro import Cadastro

p1 = Pessoa('Erick','Valparaíso',12234,'16/12/2000')
p2 = Pessoa('José','Junco',43211,'23/10/1998')

c = Cadastro()

c.cadastra(p1)
c.cadastra(p2)

p1.imprimir_pessoa()

c.impriLis()