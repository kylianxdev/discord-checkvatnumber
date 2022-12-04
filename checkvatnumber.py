import discord
import requests

# Replace with your own vatlayer API key
VATLAYER_API_KEY = "YOUR_VATLAYER_APIKEY"

client = discord.Client(
    intents=discord.Intents.all()
)

@client.event
async def on_message(message):
    # Do not respond to other bots
    if message.author.bot:
        return

    # Check if the message is a command to check a VAT number
    if message.content.startswith("!checkvat"):
        # Extract the VAT number from the command
        vat_number = message.content[9:].strip()

        # Use the vatlayer API to validate the VAT number and get the company name
        api_url = f"http://apilayer.net/api/validate?access_key={VATLAYER_API_KEY}&vat_number={vat_number}"
        response = requests.get(api_url)
        data = response.json()

        # Check if the VAT number is valid and get the company name
        if data["valid"]:
            company_name = data["company_name"]
            # Send the company name in the chat
            await message.channel.send(f"The company name for VAT number {vat_number} is {company_name}")
        else:
            # Send an error message if the VAT number is not valid
            await message.channel.send(f"Invalid VAT number: {vat_number}")

# Replace with your own Discord bot token


client.run("YOUR_BOT_TOKEN")




