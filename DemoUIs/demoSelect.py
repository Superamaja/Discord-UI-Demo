import discord


class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Choice A", description="The first choice"),
            discord.SelectOption(label="Choice B", description="The second choice"),
            discord.SelectOption(label="Choice C", description="The correct choice"),
            discord.SelectOption(label="Choice D", description="The fourth choice"),
        ]
        super().__init__(placeholder="Choose the correct answer...", options=options)
        self.submitted = set()

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id in self.submitted:
            await interaction.response.send_message(
                "You already submitted an answer", ephemeral=True
            )
            return

        self.submitted.add(interaction.user.id)

        if self.values[0] == "Choice C":
            await interaction.response.send_message("Correct!", ephemeral=True)
        else:
            await interaction.response.send_message("Incorrect!", ephemeral=True)
