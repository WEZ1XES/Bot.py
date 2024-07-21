import discord
import os
import random
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send('Я демонстрационный бот! Вот мои комманды 1. Weather 2. plus 3.mem')

@bot.command('weather')
async def command_weather(ctx:commands.Context):
    await ctx.send('Погода сегодня класс!')
@bot.command('plus')
async def command_plus(ctx:commands.Context, a, b):
    a = int(a)
    b = int(b)
    result = a + b
    await ctx.send(result)

@bot.command('mem')
async def command_mem(ctx):
    image = os.listdir('image')
    image_name = random.choice(image)
    with open('image/'+image_name, 'rb') as file:
        image = discord.File(file)
    await ctx.send('Лови Мем!', file=image)

@bot.command('steklo')
async def command_steklo(ctx):
    await ctx.send('Для начала стоит знать: не стоит выкидывать стекло вместе с другим мусором. При транспортировке оно бьется на осколки и превращается в стеклобой, который потом нельзя будет переработать из-за того, что он перемешается с мусором. Стеклобой причиняет даже больший вред природе, чем цельное изделие из стекла.')


@bot.command('sortirovka')
async def command_sortirovka(ctx):
    await ctx.send('Раздельный сбор отходов позволяет решить сразу несколько проблем. Во-первых, благодаря этому меньше мусора захоранивают на полигонах. Старые свалки растут медленнее, новые открываются реже. Кроме того, разлагаясь под открытым небом на полигонах, вещи могут выделять ядовитые вещества в атмосферу, грунт или воду')

@bot.command('pripoda')
async def command_pripoda(ctx):
    await ctx.send('Основные причины беречь природу: Обеспечение кислородом: Деревья и растения выделяют кислород, которым мы дышим. * Чистая вода: Природные экосистемы фильтруют и очищают воду. * Плодородная почва: Природные процессы создают и поддерживают плодородие почвы, необходимое для выращивания продуктов питания')






bot.run("ВАШ ТОКЕН")
