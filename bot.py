import discord
import os
import requests
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # Carga las variables del archivo .env
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')


# Prefijo de comandos (puedes usar lo que quieras)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

@bot.command()
async def roll(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'🎲 Has sacado un {number}!')

@bot.command()
async def clima(ctx, *, ciudad: str):
    # Muestra el clima actual de la ciudad indicada
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        nombre = data['name']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humedad = data['main']['humidity']
        await ctx.send(f"🌤️ Clima en **{nombre}**:\nTemperatura: {temp}°C\nDescripción: {desc}\nHumedad: {humedad}%")
    else:
        await ctx.send("❌ No pude obtener el clima para esa ciudad. ¿Está bien escrita?")

@bot.command()
async def cancion(ctx):
    # Sugiere una canción recomendada por el desarrollador
    canciones = [
        {"Titulo": "Harambe The Pirate Gorilla",
         "Enlace": "https://www.youtube.com/watch?v=rkOPv626Nn4&list=RDrkOPv626Nn4&start_radio=1&ab_channel=NapalmRecords"
        },
        {"Titulo": "When My Train Pulls In",
         "Enlace": "https://youtu.be/gYXMDCNjl8M?si=gCCaX1dYABjflPdH&t=109"
        },
        {"Titulo": "Candy And Her Friends",
         "Enlace": "https://www.youtube.com/watch?v=Wf-vJ-oZTM8&list=RDWf-vJ-oZTM8&start_radio=1&ab_channel=TheBlackKeys"
        },
        {"Titulo": "The Evil Has Landed",
         "Enlace": "https://www.youtube.com/watch?v=Exa0CzlCb3Y&list=RDExa0CzlCb3Y&start_radio=1&ab_channel=QueensOfTheStoneAge"
        },
        {"Titulo": "I Turn My Camera On",
         "Enlace": "https://www.youtube.com/watch?v=OUpP02enWgU&list=RDOUpP02enWgU&start_radio=1&ab_channel=MrJanoon"
        },
        {"Titulo": "Laser-Shooting Dinosaur",
         "Enlace": "https://www.youtube.com/watch?v=CRIwJRutl4Q&list=RDCRIwJRutl4Q&start_radio=1&ab_channel=NapalmRecords"
        },
        {"Titulo": "Rollin",
         "Enlace": "https://www.youtube.com/watch?v=RYnFIRc0k6E&list=RDRYnFIRc0k6E&start_radio=1&ab_channel=LimpBizkitVEVO"
        },
        {"Titulo": "Kickapoo",
         "Enlace": "https://www.youtube.com/watch?v=hvvjiE4AdUI&list=RDhvvjiE4AdUI&start_radio=1&ab_channel=NewLine"
        },
        {"Titulo": "Lust",
         "Enlace": "https://www.youtube.com/watch?v=jQvUBf5l7Vw&list=RDjQvUBf5l7Vw&start_radio=1&ab_channel=IggyPopOnVEVO"
        },
        {"Titulo": "Proud",
         "Enlace": "https://www.youtube.com/watch?v=c79L7CT2Fqs&list=RDc79L7CT2Fqs&start_radio=1&ab_channel=WelshlyArmsBand"
        }
        ]
    cancion_recomendada = random.choice(canciones)
    await ctx.send(f'🎶 Te recomiendo: {cancion_recomendada["Titulo"]}. Enlace: {cancion_recomendada["Enlace"]}🎶')

# Aquí va el token (mejor usar variable de entorno)
Token = os.getenv('DISCORD_TOKEN')
bot.run(Token)