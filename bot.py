#Imports
global cenouraBaiano

import discord
import random
import time
client= discord.Client()
variavel=True
#Variaveis 
xingamentos=['xexelento','arrombado','fdp','SUA PUTA','vadia','gostosa','lixo','gordo','Bebum','pipi','popo','seu desempregado','cachorro','AUUUUU','ME PAGA UM LITRAO AI ','SEU SULISTA','Bebum']
janta=['cuscuz com linguiça','nada','Pão com salame e queijo mossarela','arroz carreteiro com mandioca suquinho de bergamota','2 pães francês com carne de hambúrguer e queijo','cereal','um garfo de bolo de chocolate',' arroz, feijão e frango','café','Café preto com torrada de pão queijo salaminho presunto alface e manteiga','Arroz, feijão preto, farofa, carne de porco, carne de sol, linguiça, vinagrete e alface','arroz, 1 bife de carne de boi e 5 pedaços de frango(foi 11 reais)','pão com ovo','pão integral','hambúrguer com maionese']
cobaias=['LEITE','Queijo','Ste','Theo','Cenoura','GM SEU','Foster','Luques','Honk']
cuzcuzlista=['cuzcuz (1).jpg','cuzcuz (2).jpg','cuzcuz (3).jpg','cuzcuz (4).jpg','cuzcuz (5).jpg','cuzcuz (6).jpg','cuzcuz (7).jpg','cuzcuz (8).jpg','cuzcuz (9).jpg','cuzcuz (10).jpg','cuzcuz (11).jpg','cuzcuz (12).jpg','cuzcuz (13).jpg','cuzcuz (14).jpg','cuzcuz (15).jpg']




#bot on
@client.event
async def on_ready():
    print('---------')
    print('Bot Ta on')
    print('---------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('$cuzcuz'):
        cuzcuzvariavel=random.choice(cuzcuzlista)
        await message.channel.send(file=discord.File(cuzcuzvariavel))


    if message.content.startswith('$aleatorio'):
        await message.channel.send('https://picsum.photos/200/300')


#chingamentos
    if message.content.startswith('$settimerstozero'):
        while variavel==True:
            await message.channel.send('Tic tac, tic tac')
            time.sleep(3600)
            
            xingamentos1=random.choice(xingamentos)
            cobaias1=random.choice(cobaias)
            await message.channel.send(cobaias1)
            await message.channel.send(xingamentos1)
    
    if message.content.startswith('$mexinga'):
        xingamentos1=random.choice(xingamentos)
        cobaias1=random.choice(cobaias)
        await message.channel.send(cobaias1)
        await message.channel.send(xingamentos1)

#janta de hoje
#deixado de lado por falta de conhecimento 

#    if message.content.startswith('janta:'):
#        with open("janta.txt","a") as arquivo:
#           for valor in message.content:
#               arquivo.write(str(valor))
#            arquivo.write(str(','))

#janta de hore resposta 
    
    if message.content.startswith('$janta'):
        janta1=random.choice(janta)
        await message.channel.send(janta1)
        await message.channel.send('Pode ser ?')
#oi

    if message.content.startswith('$oi'):
        await message.channel.send('OI PORRA!')
#horas

    if message.content.startswith('$horas'):
        await message.channel.send(time.strftime('%H:%M', time.localtime()))  
#numeros
    if message.content.startswith('$batata'):
        
        a=1010
        while a < 100000:
            a+=1
            await message.channel.send(str(a))

        










client.run('NzYzNzc5MDMyMDE3MjcyODQ0.X38qpw.4R18oZqGz_hFwhoHjFk6BtS5qeo')