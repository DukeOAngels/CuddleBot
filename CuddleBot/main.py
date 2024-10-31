import discord
from discord.ext import commands
import random
import os
import socket
import time
import threading
            
def run_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Socket server is running...")
    
    while True:
        try:
            conn, addr = server_socket.accept() 
            print(f"Connection accepted from {addr}")
            conn.close()  
            time.sleep(1) 
        except Exception as e:
            print(f"Socket error: {e}")
            break

    server_socket.close()
    print("Socket closed.")

socket_thread = threading.Thread(target=run_socket_server)
socket_thread.daemon = True
socket_thread.start()

def load_api_key(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        
        return file.read().strip()

api_key_path = 'api.txt'

API_KEY = load_api_key(api_key_path)
GUILD_ID = 1301299561012265081

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

        try:
            guild = discord.Object(id=GUILD_ID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing command: {e}')
         
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.presences = True
intents.members = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name="links", description="Link tree!", guild=discord.Object(id=GUILD_ID))
async def saylinks(interaction: discord.Interaction):
    await interaction.response.send_message(" https://linktr.ee/ChaoticCuddlez")
    
@client.tree.command(name="throne", description="Throne!", guild=discord.Object(id=GUILD_ID))
async def saythrone(interaction: discord.Interaction):
    await interaction.response.send_message("  https://throne.com/chaoticcuddlez ")
    
@client.tree.command(name="lurk", description="Start lurking!", guild=discord.Object(id=GUILD_ID))
async def saylurk(interaction: discord.Interaction):
    await interaction.response.send_message("{interaction.user} Is now lurking!")
    
@client.tree.command(name="merch", description="Link tree!", guild=discord.Object(id=GUILD_ID))
async def saymerch(interaction: discord.Interaction):
    await interaction.response.send_message("Yes we do have merchandize ^^ from hoodies, coffee mugs, mouse pads and more! head on over to chaoticcuddlez-shop.fourthwall.com  for more <3 ")

@client.tree.command(name="dice", description="Roll dice up to number of your choosing! 🎲", guild=discord.Object(id=GUILD_ID))
async def saydice(interaction: discord.Interaction, number: int):
    if number < 1:
        await interaction.response.send_message("You can't roll dice with no sides!", ephemeral=True)
        return
    await interaction.response.send_message(f"{interaction.user.mention} rolled a {random.randint(1, number)} out of {number}! 🎲")

@client.tree.command(name="wet", description="Are ya wet?", guild=discord.Object(id=GUILD_ID))     
async def saywet(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"{user.mention} is {random.randint(0, 100)}% wet! 💦")
    
@client.tree.command(name="serious", description="seriously?", guild=discord.Object(id=GUILD_ID))     
async def sayserious(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"Why is {user.mention} {random.randint(0, 100)}% serious. Seriously?")
    
@client.tree.command(name="capture", description="Capture Cuddlez!", guild=discord.Object(id=GUILD_ID))     
async def saycapture(interaction: discord.Interaction, user1: discord.Member = None, user2: discord.Member = None):
    if user1 is None and user2 is None:
        await interaction.response.send_message(f"{interaction.user.mention} throws a Pokeball and tries to capture Cuddlez with {random.randint(0, 100)}% success")
    
    elif user2 is None:
        user1 = interaction.user
        await interaction.response.send_message(f"{user1.mention} throws a Pokeball and tries to capture Cuddlez with {random.randint(0, 100)}% success")
    else:
        await interaction.response.send_message(f"{user1.mention} throws a Pokeball and tries to capture {user2.mention} with {random.randint(0, 100)}% success")
    
@client.tree.command(name="sleepy", description="Are ya sleepy?", guild=discord.Object(id=GUILD_ID))     
async def saysleepy(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"{user.mention} is {random.randint(0, 100)}% sleepy! 😴")
    
@client.tree.command(name="sus", description="Feeling sus?", guild=discord.Object(id=GUILD_ID))     
async def saysus(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"{user.mention} is {random.randint(0, 100)}% SUS today. Hmmmm, suspicious....")

@client.tree.command(name="pp", description='How "avarage" is it?', guild=discord.Object(id=GUILD_ID))     
async def saypp(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"{user.mention}'s pp is {random.randint(0, 100)}% smaller than the avarage! 🍆 ")

@client.tree.command(name="cuddle", description="Want to Cuddle?", guild=discord.Object(id=GUILD_ID))     
async def sayhug(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(f"{user.mention} is {random.randint(0, 100)}% sure, that wants a cuddle!")
    
@client.tree.command(name="bonk", description="Wanna bonk someone?", guild=discord.Object(id=GUILD_ID))
async def saybonk(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        await interaction.response.send_message("You can't bonk Nothing; Nothing is too strong!!", ephemeral=True)
        return
        
    else:
        await interaction.response.send_message(f"{interaction.user.mention} bonked {user.mention}!")
        
@client.tree.command(name="rizz", description="mr.Rizzler", guild=discord.Object(id=GUILD_ID))
async def sayrizz(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        await interaction.response.send_message("You can't Rizz Nothing; He is the Rizzler!", ephemeral=True)
        return
        
    else:
        await interaction.response.send_message(f"{interaction.user.mention} has {random.randint(0, 100)}% chance to rizz up {user.mention}!")

@client.tree.command(name="date", description="Date huh?", guild=discord.Object(id=GUILD_ID))
async def saydate(interaction: discord.Interaction, user1: discord.Member = None, user2: discord.Member = None):
    if user1 is None and user2 is None:
        user = interaction.user
        await interaction.response.send_message(f"{user.mention} has a {random.randint(0, 100)}% chance to go on a date with Cuddlez! 💖")
        
    elif user2 is None:
        await interaction.response.send_message(f"{interaction.user.mention} has a {random.randint(0, 100)}% chance to go on a date with {user1.mention}! 💖")
    
    else:
        await interaction.response.send_message(f"{user1.mention} has a {random.randint(0, 100)}% chance to go on a date with {user2.mention}! 💖")
        
@client.tree.command(name="downbad", description="Downbad?", guild=discord.Object(id=GUILD_ID))
async def saydownbad(interaction: discord.Interaction, user1: discord.Member = None, user2: discord.Member = None):
    if user1 is None and user2 is None:
        user = interaction.user
        await interaction.response.send_message(f"{user.mention} is {random.randint(0, 100)}% downbad for Cuddlez! 🫢")
        
    elif user2 is None:
        await interaction.response.send_message(f"{interaction.user.mention} is {random.randint(0, 100)}% downbad for {user1.mention}! 🫢")
    
    else:
        await interaction.response.send_message(f"{user1.mention} is {random.randint(0, 100)}% downbad for {user2.mention}! 🫢")

@client.tree.command(name="marry", description="Marry huh?", guild=discord.Object(id=GUILD_ID))
async def saydmarry(interaction: discord.Interaction, user1: discord.Member = None, user2: discord.Member = None):
    if user1 is None and user2 is None:
        user = interaction.user
        await interaction.response.send_message(f"{user.mention} has a {random.randint(0, 100)}% chance to go on a marry Cuddlez! 💖")
        
    elif user2 is None:
        await interaction.response.send_message(f"{interaction.user.mention} has a {random.randint(0, 100)}% chance to marry {user1.mention}! 💖")
    
    else:
        await interaction.response.send_message(f"{user1.mention} has a {random.randint(0, 100)}% chance to marry {user2.mention}! 💖")

@client.tree.command(name="hug", description="Wanna hug?", guild=discord.Object(id=GUILD_ID))
async def saydhug(interaction: discord.Interaction, user1: discord.Member = None, user2: discord.Member = None):
    if user1 is None and user2 is None:
        user = interaction.user
        await interaction.response.send_message(f"{user.mention} has hugged Cuddlez! 💖")
        
    elif user2 is None:
        await interaction.response.send_message(f"{interaction.user.mention} has hugged {user1.mention}! 💖")
    
    else:
        await interaction.response.send_message(f"{user1.mention} has hugged {user2.mention}! 💖")
    
@client.tree.command(name="scare", description="Scare someone!", guild=discord.Object(id=GUILD_ID))
async def sayscare(interaction: discord.Interaction, user: discord.Member = None):
    members = interaction.guild.members

    if user is None:
        await interaction.response.send_message("You can't scare Nothing; Nothing isn't scared of itself!", ephemeral=True)
        return
    
    if user in members:
        random_user = random.choice([member for member in members if member != user and not member.bot])
        await interaction.response.send_message(f"{random_user.mention} scared {user.mention}! 😱")
    else:
        await interaction.response.send_message("That user is not in the guild!", ephemeral=True)


@client.tree.command(name="makeout", description="Saw someone making out?! Who? Where?", guild=discord.Object(id=GUILD_ID))
async def saymakeout(interaction: discord.Interaction):
    locations = [   
    "the bedroom",
    "a car",
    "the park",
    "the beach",
    "the kitchen",
    "a movie theater",
    "a rooftop",
    "the library",
    "a coffee shop",
    "the backyard",
    "a hotel room",
    "a forest",
    "a concert venue",
    "a train station",
    "the gym",
    "a rooftop terrace",
    "a hidden alley",
    "the shower",
    "a picnic spot",
    "a carnival"
    ]
    
    members = [member for member in interaction.guild.members if not member.bot]

    user1, user2 = random.sample(members, 2)

    location = random.choice(locations)

    await interaction.response.send_message(f"{user1.mention} and {user2.mention} were caught making out in {location}! Our love birds :3 ")

client.run(API_KEY)