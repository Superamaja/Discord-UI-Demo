import discord

from DemoUIs.demoModal import Modal
from DemoUIs.demoSelect import Select


class DemoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Select())

    @discord.ui.button(label="Open Demo Modal", style=discord.ButtonStyle.blurple)
    async def open_demo_modal(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(Modal())
