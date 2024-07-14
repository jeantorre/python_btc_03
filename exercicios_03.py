### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# try:
#     quantidade = int(input('Digite o valor de quantidade: '))
#     preco = int(input('Digite o valor do preço: '))

#     if quantidade > 0 and preco > 0:
#         print('Valores válidos!')
#     else:
#         print('Valores inválidos!')
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

'''
Exercício 2 - Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'.
Considerando que:
- Temperatura < 18°C é 'Baixa'
- Temperatura >= 18°C e <= 26°C é 'Normal'
- Temperatura > 26°C é 'Alta' 
'''
# temperatura = float(input('Digite uma temperatura: '))
# if temperatura < 18:
#     print('Essa temperatura é considerada baixa!')

# elif 18 <= temperatura <= 26:
#     print('Essa temperatura é considerada normal!')

# else:
#     print('Essa temperatura é considerada alta!')

'''
Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
Dado um registro de log em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
'''
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(log['message'])

'''
Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos
e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou
o erro específico encontrado.
'''
# import re

# try:
#     idade = int(input('Digite sua idade: '))
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# def checar_email(email):
#     if(re.fullmatch(regex, email)):
#         print('Dados de usuários válidos')
#     else:
#         print('Email inválido')

# if 18 <= idade <= 65:
#     email = input('Digite seu e-mail: ')
#     checar_email(email)
# else:
#     print('Idade inválida')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

'''
Exercício 11. Leitura de Dados até Flag
Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
'''
entrada = input('Digite um valor de entrada: ')

while entrada.lower() != 'sair':
    entrada = input('Digite um valor qualquer ou "sair" para terminar: ')

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

'''
Exercício 14. Tentativas de Conexão
Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
'''
# tentativa_maxima = 8
# tentativa = 1
# while tentativa <= tentativa_maxima:
#     print(f'Tentativa {tentativa} de {tentativa_maxima}')

#     # if True:
#     #     print('Conexão bem sucedida!')
#     #     break
#     tentativa += 1

# else:
#     print(f'Falha ao conectar após {tentativa_maxima} tentativas!')


'''
Exercício 15. Processamento de Dados com Condição de Parada
Processar itens de uma lista até encontrar um valor específico que indica a parada.
'''
# item = [1, 2, 3, 4, 5, 6, 'parar', 7, 8, 9]
# i = 0

# while i < len(item):
#     print(f'Processando item {item[i]}')
#     i += 1

#     if item[i] == 'parar':
#         print('Item de parada encontrado. Encerrando o processamento!')
#         break