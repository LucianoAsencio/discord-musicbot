import discord
import os
import yt_dlp
import openai

from discord.ext import commands
from dotenv import load_dotenv


description = 'Los comandos que se pueden utilizar son:'
client = commands.Bot(command_prefix='.', description=description, intents=discord.Intents.all())


@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Conectate a un canal...")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)


@client.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()


@client.command()
async def play(ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
    YDL_OPTIONS = {'format' : 'bestaudio'}
    voice_chat = ctx.voice_client

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][4]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, executable=r"c:\program files\ffmpeg\bin\ffmpeg.exe", **FFMPEG_OPTIONS)
        voice_chat.play(source)


@client.command()
async def pause(ctx):
    await ctx.voice_client.pause()
    await ctx.send("Pausado, .resume para volver a escuchar")


@client.command()
async def resume(ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resumido :P")


@client.command()
async def bot(ctx):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ctx.message.content}])
    await ctx.send(completion.choices[0].message.content)


@client.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles", description="Aquí están los comandos disponibles para este bot.", color=discord.Color.brand_green())
    embed.add_field(name=".join", value="Ingresa al bot a tu canal", inline=False)
    embed.add_field(name=".play 'url'", value="Comienza a reproducir un video de Youtube", inline=False)
    embed.add_field(name=".pause", value="Pausa lo que se está reproduciendo", inline=False)
    embed.add_field(name=".resume", value="Resume lo que se estaba reproduciendo", inline=False)
    embed.add_field(name=".disconnect", value="Desconecta al bot del canal", inline=False)
    embed.add_field(name=".bot 'mensaje'", value="Te contesto tu mensaje", inline=False)
    await ctx.send(embed=embed)



load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('MY_ORGANIZATION')
client.run(os.getenv('BOT_TOKEN'))
