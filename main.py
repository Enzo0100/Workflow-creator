from graphviz import Digraph
from IPython.display import Image

# Cria um novo gráfico direcionado
dot = Digraph()

# Configuração geral
dot.attr(rankdir='LR')

# Adiciona nós com diferentes formas e rótulos em português
dot.node('1', 'Cliente', shape='ellipse')

# Interações com o Atendente Virtual no WhatsApp
dot.node('2', 'Atendente Virtual no WhatsApp', shape='ellipse')
dot.node('3', 'Receber Mensagem do Cliente', shape='box')
dot.node('4', 'Enviar Resposta', shape='box')

# Interações com o Painel de Pedidos
dot.node('5', 'Painel de Pedidos', shape='ellipse')
dot.node('6', 'Receber Pedido JSON', shape='box')
dot.node('7', 'Processar Pedido', shape='box')
dot.node('8', 'Confirmar Pedido', shape='box')

# Interações com o Frontend do Cardápio Digital
dot.node('9', 'Frontend do Cardápio Digital', shape='ellipse')
dot.node('10', 'Enviar Pedido JSON', shape='box')
dot.node('11', 'Receber Confirmação', shape='box')

# Segurança
dot.node('12', 'Segurança', shape='ellipse')
dot.node('13', 'Autenticação JWT', shape='box')
dot.node('14', 'Criptografar Dados', shape='box')

# Define as conexões entre os nós
dot.edge('1', '2', label='Envia Mensagem')
dot.edge('2', '3', label='Recebe Mensagem')
dot.edge('3', '4', label='Processa Mensagem')
dot.edge('4', '1', label='Envia Resposta')

dot.edge('1', '9', label='Acessa Cardápio')
dot.edge('9', '10', label='Seleciona Itens')
dot.edge('10', '5', label='Envia Pedido JSON')
dot.edge('5', '6', label='Recebe Pedido')
dot.edge('6', '7', label='Processa Pedido')
dot.edge('7', '8', label='Confirma Pedido')
dot.edge('8', '11', label='Envia Confirmação')
dot.edge('11', '1', label='Recebe Confirmação')

dot.edge('5', '12', label='Verifica Segurança')
dot.edge('12', '13', label='Autenticação JWT')
dot.edge('12', '14', label='Criptografar Dados')

# Renderiza o gráfico como PNG e PDF
dot.render('fluxograma_requisicoes', format='png', cleanup=False)
dot.render('fluxograma_requisicoes', format='pdf', cleanup=False)

# Exibe a imagem
Image(filename='fluxograma_requisicoes.png')
