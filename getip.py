import asyncio
import random
import discord
from discord import app_commands
from discord.ext import commands

LOCATIONS = [
    ("Warszawa", "Mazowieckie", "Poland", "🇵🇱", "Orange Polska"),
    ("Kraków", "Małopolskie", "Poland", "🇵🇱", "Play"),
    ("Wrocław", "Dolnośląskie", "Poland", "🇵🇱", "T-Mobile Polska"),
    ("Gdańsk", "Pomorskie", "Poland", "🇵🇱", "Netia"),
    ("Poznań", "Wielkopolskie", "Poland", "🇵🇱", "Polkomtel"),
    ("Łódź", "Łódzkie", "Poland", "🇵🇱", "UPC Polska"),
    ("Katowice", "Śląskie", "Poland", "🇵🇱", "Multimedia Polska"),
    ("Lublin", "Lubelskie", "Poland", "🇵🇱", "Orange Polska"),
    ("Białystok", "Podlaskie", "Poland", "🇵🇱", "Play"),
    ("Rzeszów", "Podkarpackie", "Poland", "🇵🇱", "T-Mobile Polska"),
    ("Berlin", "Brandenburg", "Germany", "🇩🇪", "Deutsche Telekom"),
    ("Munich", "Bavaria", "Germany", "🇩🇪", "Vodafone Germany"),
    ("Hamburg", "Hamburg", "Germany", "🇩🇪", "O2 Germany"),
    ("Paris", "Île-de-France", "France", "🇫🇷", "Orange France"),
    ("Lyon", "Auvergne-Rhône-Alpes", "France", "🇫🇷", "SFR"),
    ("London", "England", "United Kingdom", "🇬🇧", "BT Group"),
    ("Manchester", "England", "United Kingdom", "🇬🇧", "Virgin Media"),
    ("Amsterdam", "North Holland", "Netherlands", "🇳🇱", "KPN"),
    ("Rotterdam", "South Holland", "Netherlands", "🇳🇱", "Ziggo"),
    ("Madrid", "Community of Madrid", "Spain", "🇪🇸", "Movistar"),
    ("Barcelona", "Catalonia", "Spain", "🇪🇸", "Vodafone Spain"),
    ("Rome", "Lazio", "Italy", "🇮🇹", "TIM"),
    ("Milan", "Lombardy", "Italy", "🇮🇹", "Fastweb"),
    ("Prague", "Bohemia", "Czech Republic", "🇨🇿", "O2 Czech Republic"),
    ("Vienna", "Vienna", "Austria", "🇦🇹", "A1 Telekom"),
    ("Stockholm", "Stockholm County", "Sweden", "🇸🇪", "Telia"),
    ("Oslo", "Oslo", "Norway", "🇳🇴", "Telenor"),
    ("Copenhagen", "Capital Region", "Denmark", "🇩🇰", "TDC"),
    ("Brussels", "Brussels", "Belgium", "🇧🇪", "Proximus"),
    ("Zurich", "Zurich", "Switzerland", "🇨🇭", "Swisscom"),
]

def fake_ip():
    return f"{random.randint(5,185)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"


class GetIP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="get-ip", description="...")
    @app_commands.describe(user="...")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def get_ip(self, interaction: discord.Interaction, user: discord.User):

        embed = discord.Embed(color=0x2b2d31)
        embed.description = f"Target Trojan: `{user.name}`\n\n⏳ Initializing..."
        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()

        await asyncio.sleep(1.2)

        steps = [
            ("🔌 Connecting to ISP gateway...", 1.0),
            ("🔑 Bypassing ISP authentication layer...", 1.4),
            ("✅ ISP credentials obtained!", 0.8),
            ("📡 Tracing Discord handshake packets...", 1.2),
            ("🔎 Scanning network nodes...", 1.5),
            ("🌐 Resolving target IP address...", 1.3),
            ("📍 Locating geolocation data...", 1.0),
            ("🗺️ Mapping ISP infrastructure...", 1.2),
            ("✅ Scan complete!", 0.6),
        ]

        log = ""
        for text, delay in steps:
            log += f"{text}\n"
            embed.description = f"Target trojan: `{user.name}`\n\n```\n{log}```"
            await msg.edit(embed=embed)
            await asyncio.sleep(delay)

        ip = fake_ip()
        city, region, country, flag, isp = random.choice(LOCATIONS)
        lat = round(random.uniform(49.0, 54.5), 6)
        lon = round(random.uniform(14.0, 24.0), 6)

        result_embed = discord.Embed(color=0xff0000)
        result_embed.set_thumbnail(url=user.display_avatar.url)
        result_embed.description = (
            f"-# 🌐 IP Lookup Result\n"
            f"### `{ip}`\n"
            f"```ansi\n"
            f"\u001b[1;32m  User    \u001b[0m  {user.name}\n"
            f"\u001b[1;32m  Country \u001b[0m  {flag} {country}\n"
            f"\u001b[1;32m  City    \u001b[0m  {city}\n"
            f"\u001b[1;32m  Region  \u001b[0m  {region}\n"
            f"\u001b[1;32m  ISP     \u001b[0m  {isp}\n"
            f"\u001b[1;32m  Coords  \u001b[0m  {lat}, {lon}\n"
            f"```"
        )

        await msg.edit(embed=result_embed)


async def setup(bot):
    await bot.add_cog(GetIP(bot))
