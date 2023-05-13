import discord


class Modal(discord.ui.Modal, title="Demo Modal"):
    color = discord.ui.TextInput(
        label="What is your favorite color?",
    )
    reason = discord.ui.TextInput(
        label="Why is this your favorite color?",
        style=discord.TextStyle.paragraph,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Your favorite color is `{self.color}` and your reason is `{self.reason}`!"
        )
