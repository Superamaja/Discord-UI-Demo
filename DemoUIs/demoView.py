import discord

from DemoUIs.demoModal import Modal
from DemoUIs.demoSelect import Select


class DemoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.select = Select()
        self.add_item(self.select)

    @discord.ui.button(label="Open Demo Modal", style=discord.ButtonStyle.blurple)
    async def open_demo_modal(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(Modal())

    @discord.ui.button(label="Remove from submitted list", style=discord.ButtonStyle.red)
    async def remove_user(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.select.submitted.discard(interaction.user.id)
        await interaction.response.edit_message(view=self)
