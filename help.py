import discord
from discord.ext import commands

EMBED_COLOR = 0xFF6B14
SITE_URL    = "https://astrobotapi.github.io/astro"

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["h", "commands"])
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Astro — Local Files Music Bot",
            description=(
                "> Browse the full command list, changelog, and bot info at the link below."
            ),
            color=EMBED_COLOR,
        )
        embed.add_field(
            name="📖 Documentation",
            value=f"[**astrobotapi.github.io/astro**]({SITE_URL})",
            inline=False,
        )
        embed.add_field(
            name="💬 Support",
            value="[discord.gg/localfiles](https://discord.gg/localfiles)",
            inline=True,
        )
        embed.add_field(
            name="Prefix",
            value="`，`",
            inline=True,
        )
        embed.set_footer(text="discord.gg/localfiles")
        view = discord.ui.View()
        view.add_item(discord.ui.Button(
            label="View Commands",
            url=SITE_URL,
            style=discord.ButtonStyle.link,
            emoji="📖",
        ))
        view.add_item(discord.ui.Button(
            label="Support Server",
            url="https://discord.gg/localfiles",
            style=discord.ButtonStyle.link,
            emoji="💬",
        ))
        await ctx.reply(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))
