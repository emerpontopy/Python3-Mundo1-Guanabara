# Desafio 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 4 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Sport Clube do Recife.
teams_tuple = ('Santos','Mirassol','Sport Recife','Ceará SC','Novohorizontino','Goiás','Operário','América-MG','Vila Nova','Avaí','Amazonas FC','Coritiba','Paysandu','Botafogo SP','Chapecoense','CRB','Ponte Preta','Ituano','Brusque','Guarani')
print('-='*32)
print(f'Lista de times do Brasileirão Série B 2024: {teams_tuple}')
print('-='*32)
print(f'Foram classificados para a primeira divisão {teams_tuple[:4]}')
print('-='*32)
print(f'Estão rebaixados para a série C {teams_tuple[-4:]}')
print('-='*32)
print(f'Nesse ano, o time do coração, Sport Clube do Recife, ficou na {teams_tuple.index('Sport Recife')+1}ª posição')