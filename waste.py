import discord
from discord.ext import commands
import time
import threading
import asyncio

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)



waste_sorting = {
    "bottiglia di plastica": True,
    "lattina di alluminio": True,
    "cartone della pizza": False,  # Se sporco di cibo, altrimenti riciclabile
    "bicchiere di vetro": True,
    "giornale": True,
    "sacchetto di plastica": True,
    "batteria": False,  # Da smaltire nei punti di raccolta specifici
    "lampadina": False,  # Da smaltire nei RAEE
    "tappo di sughero": True,
    "scatola di cartone": True,
    "piatto di ceramica": False,
    "contenitore di yogurt": True,
    "bottiglia di vetro": True,
    "busta di patatine": False,  # Contiene alluminio e plastica insieme
    "posate di plastica": False,
    "tubo di dentifricio": False,  # Troppo difficile da separare
    "scatoletta di tonno": True,
    "fazzoletto di carta usato": False,  # Non può essere riciclato
    "stoffa": True,
    "pannolini": False,
    "cartone del latte": True,  # Tetra Pak, va riciclato se previsto dal comune
    "flacone di detersivo": True,
    "bottiglia di olio": False,  # Olio da smaltire in centri appositi
    "tappi di plastica": True,
    "cassette di legno": True,
    "bustine del tè": True,
    "gusci di uova": True,  # Se la raccolta organica è disponibile
    "mele marce": True,  # Rifiuti organici
    "carta stagnola": True,
    "carta da forno": False,  # Trattata con siliconi
}


@bot.command()
async def poster(ctx):
    with open('C:\\Users\\monia\\Desktop\\python\\python pro corso\\bot ecologico\\poster.png', "rb") as img:
        picture = discord.File(img)
    
        await ctx.send(file = picture)






@bot.command()
async def riciclaggio(ctx, *args):
    if not args:
        await ctx.send("Il comando riciclaggio ha bisogno di un parametro aggiuntivo, esempio: `/riciclaggio bottiglia di plastica`")
        return
    else:
        oggetto = " ".join(args).lower()  
    if "info" in args:
        await ctx.send(f"Questo comando serve a farti sapere se i tuoi prodotti sono riciclabili, l'uso corretto del comando è `/riciclaggio [una delle cose nella seguente lista]` questa è la lista di oggetti riconosciuti: \n `{',' "\n".join(waste_sorting.keys())}`")    
    if oggetto in waste_sorting:
        if waste_sorting[oggetto]:
            await ctx.send(f"✅ `{oggetto}` è riciclabile.")
        else:
            await ctx.send(f"❌ `{oggetto}` non è riciclabile.")
    elif oggetto not in waste_sorting and "info" not in args:
        await ctx.send(f"⚠️ `{oggetto}` non è presente nell'elenco. Ecco gli oggetti disponibili:\n `{',' "\n".join(waste_sorting.keys())}`")


async def rt():
    while True:
        await asyncio.sleep(7200)  
        for guild in bot.guilds: 
            for channel in guild.text_channels:  
                with open('C:\\Users\\monia\\Desktop\\python\\python pro corso\\bot ecologico\\poster.png', "rb") as img:
                    picture = discord.File(img)
                try:
                    await channel.send(file=picture)
                except discord.Forbidden:  
                    continue

@bot.event
async def on_ready():
    print({bot.user}, "ha effettuato l'accesso!")
    bot.loop.create_task(rt())  


@bot.command()
async def info(ctx):
    await ctx.send("Ciao questi sono i comandi che puoi fare: \n `/info` \n `riciclaggio info` \n `/poster`")



# non usare(ci sono problemi di rate limit)
####################################################################################################################################
'''@bot.command()
async def clear(ctx):
    if ctx.author.guild_permissions.manage_messages:  # Verifica se l'utente ha il permesso di gestire i messaggi
        # Elimina messaggi in un ciclo
        async for message in ctx.channel.history(limit=9999):  # Modifica limit a seconda del numero di messaggi da eliminare
            await message.delete()
        await ctx.send("Tutti i messaggi sono stati eliminati.", delete_after=5)  # Risposta che scompare dopo 5 secondi
    else:                                                                                                                          
        await ctx.send("Non hai i permessi per fare questo.", delete_after=5)'''                                                   
####################################################################################################################################

bot.run("")