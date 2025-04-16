import discord
from discord.ext import commands
import asyncio
from app.config import TOKEN, COMMAND_PREFIX

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

semaphore = asyncio.Semaphore(10)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

async def rename_member(member):
    async with semaphore:
        try:
            if member.nick != member.name:
                await member.edit(nick=None)
                await asyncio.sleep(0.9)
                return True
        except Exception as e:
            print(f"❌ Erro ao renomear {member.display_name}: {e}")
        return False

@bot.command(name="renameall")
@commands.has_permissions(administrator=True)
async def rename_all(ctx):
    guild = ctx.guild
    members = guild.members
    renamed_total = 0

    await ctx.send(f"🔄 Iniciando renomeação de {len(members)} membros...")

    for i in range(0, len(members), 10):
        chunk = members[i:i+10]
        results = await asyncio.gather(*[rename_member(member) for member in chunk])
        renamed_total += sum(results)

        if renamed_total % 1000 == 0 and renamed_total != 0:
            await ctx.send(f"✅ {renamed_total} membros renomeados até agora...")

    await ctx.send(f"🏁 Finalizado! Total de renomeações: {renamed_total}")

bot.run(TOKEN)
