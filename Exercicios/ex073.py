""" Crie uma tupla preenchida com os 20 primeiros colocados
    da Tabela do Campeonato Brasileiro de Futebol, na ordem de 
    colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da São Paulo. """

times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo',
         'Palmeiras', 'Santos', 'Grêmio', 'Fluminense',
         'Bahia', 'Sport', 'Corinthians', 'Fortaleza',
         'Ceará', 'Atlético-GO', 'Bragantino', 'Vasco',
         'Athletico-PR', 'Coritiba', 'Botafogo', 'Goiás')

print(f'Times do Brasileirão: {times}')
print('=-' * 50)
print(f'Os 5 primeiros times: {times[0:5]}')
print('=-' * 50)
print(f'Os 4 ultimos times: {times[16:21]}')
print('=-' * 50)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('=-' * 50)
print(f'O Time {times[2]} está na posição {times.index("São Paulo") + 1}º posição')
