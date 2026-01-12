import discord
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('Secret_key')

# Initialize Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        else :
            response = model.generate_content(message.content)
            await message.channel.send(response.text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)



#   1460258516726972528
#    fecd82a433f7695ed107cdab46493d514a35faf1d524e66a31608157a4386671