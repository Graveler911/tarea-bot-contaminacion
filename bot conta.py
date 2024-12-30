import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send("hola")
    elif message.content.startswith('como te llamas'):
        await message.channel.send("me llamo bot>-9\U0001f642")
    elif message.content.startswith('que sabes hacer'):
        await message.channel.send("VAriAs CoSAs")
    elif message.content.startswith('quiero ver'):
        await message.channel.send("ok")
        await message.channel.send("selecciona alguna de estas opciones:" 
    "1 Saber sobre la contaminacion "

    "2 saber como prevenir la contaminacion"

    "3 tips para tu hogar ")
    elif message.content.startswith('1'):
        await message.channel.send("ok")
        await message.channel.send("La contaminación ambiental es la presencia de sustancias o energía nocivas en el medio ambiente, como el agua, el aire o el suelo, que afectan negativamente a los seres vivos y al entorno.\U0001f642")
    elif message.content.startswith('2'):
        await message.channel.send("ok")
        await message.channel.send("Para prevenir la contaminación ambiental, puedes: reciclar ,dejar de ir en auto e ir en bici, hacer compost con desechos aprovechables")
    elif message.content.startswith('3'):
        await message.channel.send("ok")
        await message.channel.send("Reducir residuos Reciclar y separar los residuos para usar los recursos naturales de manera más eficiente. También puedes evitar los plásticos de un solo uso y comprar productos con envases rellenables.  Consumir agua responsablemente .No arrojar desechos sólidos por el inodoro, usar poco detergente y no abusar de la lejía. Cuidar el aire .Evitar quemar basura, hojas, llantas y otros objetos. Tampoco debes usar fuegos artificiales. "\U0001f642 ")           
    else:
        await message.channel.send(message.content)

client.run("")
