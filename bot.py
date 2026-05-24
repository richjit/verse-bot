import os
import pathlib

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

BANNER_PATH = pathlib.Path(__file__).parent / "assets" / "banner.png"

EMBED_COLOR = 0x7C3AED

WHAT_IS_VERSE = (
    "Verse is building the next generation of AI employees.\n\n"
    "Instead of simple chatbots or basic automations, Verse lets anyone create fully autonomous AI workers "
    "from a single prompt — with their own memory, tools, workflows, computer access, wallets, email, "
    "and the ability to actually execute tasks.\n\n"
    "Think of it like building a digital team member, not just an assistant.\n\n"
    "**🚀 What Makes Verse Different**\n"
    "Most AI tools can only answer questions or run tiny automations. Verse agents work persistently, "
    "make decisions, and execute across real tools — without you lifting a finger.\n\n"
    "**🧠 What Verse Agents Can Do**\n"
    "• Run marketing campaigns\n"
    "• Manage customer support\n"
    "• Research competitors\n"
    "• Handle business operations\n"
    "• Automate workflows across apps\n"
    "• Manage crypto-native operations\n"
    "• Personal assistants\n"
    "• And anything else a human can do\n\n"
    "**🔥 Where We're At**\n"
    "Fully incorporated startup. Full-time team. Platform in active development. "
    "Early community forming right now. This server is where we build in public.\n\n"
    "**🌎 Our Mission**\n"
    "We believe every person and business will have teams of AI employees working alongside them. "
    "Verse exists to make that accessible to everyone.\n\n"
    "👉 **[runwiseai.app](https://runwiseai.app/)**"
)

HOW_TO_CONTRIBUTE = (
    "Verse is being built in public.\n"
    "The best ideas, workflows, agents, and features will come from the community.\n\n"
    "You don't need to be a developer to contribute.\n\n"
    "**🧠 Share Agent Ideas**\n"
    "Have an idea for an AI employee or workflow?\n"
    "Post it in:\n"
    "💡 <#1507589532512419890>\n"
    "⚙️ <#1507589550904705156>\n\n"
    "Good examples:\n"
    "> Marketing agents · Trading agents · Research agents · Customer support workflows · Automation systems · Web3 operations\n\n"
    "**🛠️ Suggest Features**\n"
    "Want something added to Verse?\n"
    "Post detailed suggestions in:\n"
    "📌 <#1507589377486885004>\n\n"
    "The more detailed the idea, the better.\n"
    "Helpful feature requests include:\n"
    "✅ The problem\n"
    "✅ The use case\n"
    "✅ Why it matters\n"
    "✅ How it should work\n\n"
    "**🐛 Report Bugs**\n"
    "Found a bug or issue?\n"
    "Post it in:\n"
    "🚨 <#1507589339373240382>\n\n"
    "Include:\n"
    "> What happened · Screenshots if possible · Steps to reproduce it · Device/browser info\n\n"
    "**📢 Spread The Vision**\n"
    "One of the biggest ways to help right now:\n\n"
    "Post about Verse on X/Twitter\n"
    "Invite smart builders & creators\n"
    "Share ideas and feedback\n"
    "Be active in the community\n\n"
    "Early communities shape great products.\n\n"
    "**🤝 Help Other Members**\n"
    "Answer questions. Give feedback. Collaborate on ideas.\n"
    "We want this server to become a place where builders explore the future of AI employees together."
)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class LinksView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(
            label="🌐 Website",
            url="https://runwiseai.app/",
            style=discord.ButtonStyle.link,
        ))
        self.add_item(discord.ui.Button(
            label="𝕏 Verse",
            url="https://x.com/useverseai",
            style=discord.ButtonStyle.link,
        ))
        self.add_item(discord.ui.Button(
            label="𝕏 Thomas (Founder)",
            url="https://x.com/realthomasgu",
            style=discord.ButtonStyle.link,
        ))


@client.event
async def on_ready():
    try:
        await tree.sync()
        print(f"Logged in as {client.user} — commands synced globally (may take up to 1 hour to appear).")
    except discord.HTTPException as e:
        print(f"Command sync failed: {e}")


@tree.command(name="whatisverse", description="Learn what Verse is")
async def whatisverse(interaction: discord.Interaction):
    try:
        embed = discord.Embed(
            title="🔮 WHAT IS VERSE?",
            description=WHAT_IS_VERSE,
            color=EMBED_COLOR,
        )
        file = discord.File(BANNER_PATH, filename="banner.png")
        embed.set_image(url="attachment://banner.png")
        await interaction.response.send_message(file=file, embed=embed, view=LinksView())
    except (discord.HTTPException, FileNotFoundError, OSError):
        await interaction.response.send_message(
            "Something went wrong. Try again in a moment.", ephemeral=True
        )


@tree.command(name="howtocontribute", description="Learn how to contribute to Verse")
async def howtocontribute(interaction: discord.Interaction):
    try:
        embed = discord.Embed(
            title="🤝 HOW TO CONTRIBUTE",
            description=HOW_TO_CONTRIBUTE,
            color=EMBED_COLOR,
        )
        file = discord.File(BANNER_PATH, filename="banner.png")
        embed.set_image(url="attachment://banner.png")
        await interaction.response.send_message(file=file, embed=embed, view=LinksView())
    except (discord.HTTPException, FileNotFoundError, OSError):
        await interaction.response.send_message(
            "Something went wrong. Try again in a moment.", ephemeral=True
        )


if __name__ == "__main__":
    client.run(os.environ["DISCORD_TOKEN"])
