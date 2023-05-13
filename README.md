# Discord Bot with Demo UIs

This is a simple Discord bot that allows users to test out different UIs by clicking on items.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Copy the `.env.example` file in the root directory of the project and rename it to `.env`.
4. Add your Discord bot token as `DISCORD_TOKEN=your_token_here`.
5. Run the bot using the command python main.py.

## Usage

Once the bot is running, you can use the `!demo` command in any Discord server that the bot is a member of to test out the different UIs. Simply click on the items to interact with them.

## Notes
Make sure the bot has all the intents enabled in the Discord developer portal. You can find the intents under the "Bot" section of your application.
