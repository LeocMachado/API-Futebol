import requests
from requests import RequestException

API_KEY = "ce6ee87dcbbf49b7b85b319aa82235a0"

Liga = input('Qual liga voce deseja acessar: ')
url = "https://api.football-data.org/v4/competitions/"
url3 = ''
# Cabeçalhos da requisição
headers = {
    "X-Auth-Token": API_KEY
}

# Fazendo a requisição
response = requests.get(url, headers=headers)

data = response.json()
dataCompetitions = data["competitions"]

for competition in dataCompetitions:
    if competition['name'] == Liga:
        competitionUser = competition
        url3 = url + competition['code']

print(f'Liga Selecionada: {competitionUser['name']}')
print('selecione uma das Opcoes: ')
print('1 -  Partidas em andamentos')
print('2 - classificacao')
print('3 - Artilheiros')
choice = input(':')

def AoVivo():
        r1 = url3 + '/matches'
        r2 = requests.get(r1, headers=headers)
        dados= r2.json()

        Lives = dados.get('matches', [])
        InProgress = [jogo for jogo in Lives if jogo['status'] == 'LIVE']
        Finished = [jogo for jogo in Lives if jogo['status'] == 'FINISHED']

        if InProgress:
            print("Partidas em andamento:")
            for jogo in InProgress:
                casa = jogo["homeTeam"]["name"]
                visitante = jogo["awayTeam"]["name"]
                placar_casa = jogo["score"]["fullTime"]["home"]
                placar_visitante = jogo["score"]["fullTime"]["away"]
                print(f"{casa} {placar_casa} x {placar_visitante} {visitante}")
        else:
            print('Nenhuma partida ao vivo, rodada se encerrou')
        



def classificacao():
    CL = url3 + '/standings'
    CL2 = requests.get(CL, headers=headers)
    data = CL2.json()

    Tabela = data.get('standings', [])


    if Tabela:
        print("Colocação do campeonato")
        for posicionamento in Tabela:
            for equipe in posicionamento['table']:
                posicao = equipe['position']
                time = equipe['team']['shortName']
                print(f'{posicao}: {time}')
    else:
        print('erro')

            
def strikers():
    ST = url3 + '/scorers'
    ST2 = requests.get(ST, headers=headers)
    data = ST2.json()

    Scorers = data.get('scorers', [])

    if Scorers:
        print('   Artilheiros do campeonato: \n')
        for players in Scorers:
            Jogador = players['player']['name']
            time = players['team']['shortName']
            gols = players['goals']
            assistencias = players['assists']
            print(f'   {Jogador}  X   Gols: {gols}   x   Assistencias: {assistencias}   X   {time}   \n')


if choice == '1':
    AoVivo()
elif choice == '2':
    classificacao()
elif choice == '3':
    strikers()
else:
    print('voce nao selecionou uma opcao')
