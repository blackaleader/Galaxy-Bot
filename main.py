#from multiprocessing.sharedctypes import Value
from time import sleep
from tkinter import Y
import discord
from discord.ext import commands
from discord.ui import Button , View
import datetime
import sys
from discord.utils import get
import requests
from urllib.request import urlopen
import json
from datetime import datetime
from discord.ext import tasks, commands
import asyncio

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = '>', case_insensitive = True, intents = intents)

msgs = []




# @tasks.loop(seconds=10)
# async def count():
#   players = members()
#   # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" {shirmoz}/64 Players"))
#   if shirboz != players :
#     await channel.edit(name=f"🟢┇{players}/64 Players")
#     shirboz.replace(shirboz, players)
#   else :
#     pass

def members():
    with urlopen("http://185.126.10.241:30120/players.json") as response:
        source = response.read()

    data = json.loads(source)
    # print(json.dumps(data,indent=2))
    print(len(data))
    # shirmoz= (len(data))
    return len(data)

def checkserver():
    with urlopen("http://185.126.10.241:30120/players.json") as response:
        source = response.read()

    data = json.loads(source)
    # print(json.dumps(data,indent=2))
    print(len(data))

    for item in data:
        steam = item["identifiers"]
        id = item["id"]
        name = item["name"]
        ping = item["ping"]
        for i in steam :
            if "discord:" in i : 
                discord = i.replace("discord:" , "")   
                print ( id , name,ping, discord)
                embed2.add_field(name=f"({id}) {name}", value=f" <@{discord}> Ping in Server : {ping} ms ", inline=True)


msgs = []
@client.event
async def on_ready():
  # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="New year💘 "))
  print ("starting the loop")
  try:
      synced = await client.tree.sync()
      print(f"{len(synced)} commands(s)")
  except Exception as e :
      print(e)
  print("loop has been started")




# @client.event
# async def on_ready():
#     print('Bot is Ready.')
#     try:
#         synced = await client.tree.sync()
#         print(f"{len(synced)} commands(s)")
#     except Exception as e :
#         print(e)

# @client.event
# async def on_voice_state_update(member: discord.Member ,befor,after):

#   L1=["📯┇Staff Channel I","📯┇Staff Channel II","📯┇Staff Channel III"]
#   l2=["⭐┇Staff on duty","🔋┇Helper","🏅┇Admin"]

#   if str(after.channel) in L1:
#     print("true")
#     print(after.channel)
#     # role_id = 1025330913715965962
#     # role = get(guild.roles, id=role_id)
#     # await client.add_roles(member,role)
#     roleVer = 'V1' #role to add
#     role = roleVer

#     await member.add_roles(discord.utils.get(member.guild.roles, name=role)) #add the role
#   elif str(after.channel) in l2:
#     roleVer2 = 'V2' #role to add
#     role2 = roleVer2
#     await member.add_roles(discord.utils.get(member.guild.roles, name=role2)) #add the role

#   else:
#     print("fasle")
#     role_get = get(member.guild.roles, id=1025330913715965962) #Returns a role object.
#     role_get2 = get(member.guild.roles, id=1025331099670429737) #Returns a role object.
#     await member.remove_roles(role_get2) #Remove the role (object) from the user.
#     await member.remove_roles(role_get) #Remove the role (object) from the user.




@client.event
async def on_member_join(member):
    channel = client.get_channel(1015944761099690024)
    # await channel.send("https://cdn.discordapp.com/attachments/1018961454638043177/1019675783104565269/Galaxy_welcome.jpg")
    #await channel.send(f"<@{member.id}> ")
    embed=discord.Embed(description=f"<@{member.id}> Be server Galaxy Community khosh omadid... \n Ghabl az harch faramosh nakonid ghavanin server ra dar channel <#700974892459229272> motalee farmaiid" ,  color=0x02aae1 ) # F-Strings!
    embed.set_thumbnail(url=member.avatar.url)
    #embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/700974894921547833/1016676226234077204/Untitled-1_copy.png")
    # embed.set_image(url="https://cdn.discordapp.com/attachments/1021739140519313408/1054464636579217509/Welcome.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1021739140519313408/1061638568797274133/discord_2.png")
    button=Button(label="Website!", style=discord.ButtonStyle.green , url = "https://gcommunity.ir/")
    view=View()
    view.add_item(button)
    await channel.send(f"|| <@{member.id}> ||")
    await channel.send(embed=embed,view=view)

# @client.event 
# async def on_voice_state_update(member, before, after):
#     guild = await client.fetch_guild(700974891930746910)  # guilde
#     #role = discord.utils.get(guild.roles, id=912605720476786688) #role not verfifed
#     general=member.guild.voice_channels
#     # @client.event
#     sleep(1)
    
#     #print(after.channel.id)
#     #print(before.voicestate.self_mute)
#     #print(after.voicestate.self_mute)



#     voice_channel= discord.utils.get(general, name='🔽〙Move To Staff') #esm channele (name)
#     va = await client.fetch_channel(700974895433252910) #vc verify
#     if member.id != 707643552406044763:
#         if voice_channel == after.channel:
#             arad = await va.connect()
#             for x in range(2):
#                 arad.play(discord.FFmpegPCMAudio(executable=r"C:/Users/Administrator/Desktop/bot/ffmpeg/bin/ffmpeg.exe", source=r"C:/Users/Administrator/Desktop/bot/gc.mp3"))
#                 while arad.is_playing():
#                     sleep(1)
                    
            
#                 await arad.disconnect()
#             channel2 = client.get_channel(700974895433252910)
#             text =  client.get_channel(1020359516644180058)

#             #print(msgs)
#             embed=discord.Embed(title="Connect to Staff Warning"  , description=f" <@{member.id}> dar connect to staff montazere shoma hastnad. <@&700974891939266606> <@&700974891939266604>" ,  color=0x02aae1 ,timestamp=datetime.utcnow() ) 
#             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
#             embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
#             await text.send( f"==================== \n User <@{member.id}> is waiting for <@&700974891939266606> <@&700974891939266604>")
#             message = await text.send( embed=embed )
#             msgs.append(message.id)
#             await message.add_reaction("✅")


#             channel = None

            
            

#             #sleep(2)

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel :
      if after.channel.id == 700974895433252910:
        if member.id != 707643552406044763:
            if after.channel and not before.channel:
                # User has joined a voice channel
                channel = after.channel
                text =  client.get_channel(1020359516644180058)

                #print(msgs)
                embed=discord.Embed(title="Connect to Staff Warning"  , description=f" <@{member.id}> dar connect to staff montazere shoma hastnad. <@&700974891939266606> <@&700974891939266604>" ,  color=0x02aae1 ,timestamp=datetime.utcnow() ) 
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
                embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
                await text.send( f"==================== \n User <@{member.id}> is waiting for <@&700974891939266606> <@&700974891939266604>")
                message = await text.send( embed=embed )
                msgs.append(message.id)
                await message.add_reaction("✅")
                voice_client = await channel.connect()
                # source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("C:/Users/Black Leader/Desktop/New folder (4)/vc.m4a"))
                voice_client.play(discord.FFmpegPCMAudio(executable="C:/Users/Administrator/Desktop/bot/ffmpeg/bin/ffmpeg.exe", source="C:/Users/Administrator/Desktop/bot/gc.mp3"))
                # voice_client.play(source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()

# @client.event
# async def on_voice_state_update(member, before, after):
#     if after.channel and not before.channel:
#         # User has joined a voice channel
#         channel = after.channel
#         voice_client = await channel.connect()
#         # source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("C:/Users/Black Leader/Desktop/New folder (4)/vc.m4a"))
#         voice_client.play(discord.FFmpegPCMAudio(executable="C:/Users/Leader/Desktop/galaxy community project/ffmpeg/bin/ffmpeg.exe", source="C:/Users/Leader/Desktop/galaxy community project/gc.mp3"))
#         # voice_client.play(source)
#         while voice_client.is_playing():
#             await asyncio.sleep(1)
#         await voice_client.disconnect()



          
# staffs = [ 767351619594747956 ,733861681335107634 , 808779892396785785 ,453619288641634324, 918852486406766603 , 488408309343191061 , 774193100561580044 ,545515947021303818,475215293065461771 ,631055558257934346,1016253785439477850]
# @client.tree.command(name="whitelist" , description="Jahat dadan role whitelist be user📗")
# async def ticket(interaction:discord.Integration ,  user:discord.User):
#     my_server= await client.fetch_guild(700974891930746910)
#     rele = role_id = 1015948382713425991
#     role = my_server.get_role(role_id)
#     embed2=discord.Embed( color=0x00ff04 ) # F-Strings!
#     await user.add_roles(role)
#     embed2.set_author(name=f"{user.name} aziz shoma ba  movafaghiat Whitelist shodid omidvaram oghat khoshi ra dar server separi konid ", icon_url="{user.avatar}")
#     #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
#     await interaction.response.send_message(embed=embed2)


     
# @client.command()
# async def list(ctx):
@client.tree.command(name="list" , description="lorem ispum")
async def list(interaction:discord.Integration ):
  global embed2
  vaght = datetime.now().strftime("%H:%M:%S")
  print("ok wait")
  try:
        r = requests.get('https://status.cfx.re/api/v2/status.json', timeout=10)
        e = requests.get('https://status.cfx.re/metrics-display/1hck2mqcgq3h/day.json', timeout=10)
        data = r.json()
        data_2 = e.json()
        MS = round(data_2['summary']['mean'], 0)
        DESC = data['status']['description']
        #CAUSES = data['status']['indicator']
        time.sleep(5)
        if DESC != "All Systems Operational":
            print("====== OUTAGE DETECTED ======")
            print(datetime.now().strftime("%H:%M:%S"), " | FiveM // CFX.re Server Status: " + DESC)
           # print("Possible Root Issues: " + CAUSES)
            print("\t\tAverage CnL self-test time " + str(MS) + ' ms')
        else:
            time = (datetime.now().strftime("%H:%M:%S"))
            shirmoz =f" {time } | CFX.re is live and working (Iran) { str(MS) }   ms ✅ " 

            embed2=discord.Embed(title=" <a:outputonlinegiftools2:1054075819682697297> LIVE Cfx.re status ", description= f" {shirmoz} \n test") 
            embed2.set_footer(text=  f"Coded by Arman Leader#0117 | Last update : {vaght} ")
            checkserver()
            await interaction.response.send_message(embed=embed2)
  except Exception as e :
    time = (datetime.now().strftime("%H:%M:%S"))
    shirmoz =f" {time } | CFX.re is unavailable (Iran) ❌ " 

    embed2=discord.Embed(title=" <a:outputonlinegiftools2:1054075819682697297> LIVE Cfx.re status ", description= f" {shirmoz} ") 
    embed2.set_footer(text=  f"Coded by Arman Leader#0117 | Last update : {vaght} ")
    checkserver()
    await interaction.response.send_message(embed=embed2)
    print(e)
    print("[Err]: Couldn't get request in enough time.")

@client.tree.command(name="b1" , description="Backstory accept ( staff only ) 🟩")
async def b1(interaction:discord.Integration ,  user:discord.User):
    if 1018627140868112414 in [ y.id for y in interaction.user.roles]:
      aks = user.avatar.url
      channel = await client.fetch_channel(1060155712757579817)
      my_server= await client.fetch_guild(700974891930746910)
      rele = role_id = 1015948382713425991
      role = my_server.get_role(role_id)
      embed2=discord.Embed( color=0x00ff04 ) # F-Strings!
      await user.add_roles(role)
      embed2.set_author(name=f"{user.name} aziz shoma ba  movafaghiat Whitelist shodid omidvaram oghat khoshi ra dar server separi konid ", icon_url=aks)
      #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
      # await interaction.response.send_message(embed=embed2)
      await interaction.response.send_message("Fard ba movafaghiat whitelist shod ! <a:1134verifiedanimated:1060165061202694154> ")
      await channel.send(f"<@{user.id}>")
      await channel.send(embed=embed2)
    else :
      vaght = datetime.now().strftime("%H:%M")
      embed2=discord.Embed( color=0xff0000 ) # F-Strings!
      embed2.set_author(name=f"Shoma back story support nistid !", icon_url="https://cdn.discordapp.com/attachments/1062485398779080754/1069345548290760877/Galaxy.png")
      embed2.set_footer(text=  f"Coded by Arman Leader#1211 |  {vaght} ")
      await interaction.response.send_message(embed=embed2)


@client.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        if new_role.name in ('Gold Sub', 'Platinum Sub','Diamond Sub'):
          channel= await client.fetch_channel(1088824203630874624)
          await channel.send(f"||@here|| \n {after.name}#{after.discriminator} , {new_role.name} ra kharidari kard ! <a:outputonlinegiftools:1054071786913923102> ")


@client.tree.command(name="pend" , description="To pend a ticket (staff only) ⭕")
async def pend(interaction:discord.Integration , role:discord.Role ):
    if "ticket" in interaction.channel.name  :
      if "Management" in role.name :
         
        A = discord.utils.get(interaction.guild.channels, name="📧⟫ Mgmt Ticket")
        await interaction.channel.edit(category=A)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Developer Team" in role.name :
        B = discord.utils.get(interaction.guild.channels, name="📧⟫ Dev Ticket")
        await interaction.channel.edit(category=B)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Moderator" in role.name  :
        C = discord.utils.get(interaction.guild.channels, name="📧⟫ Mod Ticket")
        await interaction.channel.edit(category=C)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Report" in role.name  :
        D = discord.utils.get(interaction.guild.channels, name="📧⟫ Report Ticket")
        await interaction.channel.edit(category=D)
        await interaction.response.send_message(f"karbar aziz ticket shoma be Vahede marbote erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Refund" in role.name  :
        E = discord.utils.get(interaction.guild.channels, name="📧⟫ Refund Ticket")
        await interaction.channel.edit(category=E)
        await interaction.response.send_message(f"karbar aziz ticket shoma be Vahede marbote erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "BackStory Support" in role.name  :
        F = discord.utils.get(interaction.guild.channels, name="📧⟫ BS Ticket")
        await interaction.channel.edit(category=F)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Game Master" in role.name  :
        G = discord.utils.get(interaction.guild.channels, name="📧⟫ game master")
        await interaction.channel.edit(category=G)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "Staff Supervisor" in role.name  :
        H = discord.utils.get(interaction.guild.channels, name="📧⟫ Staff Supervisor")
        await interaction.channel.edit(category=H)
        await interaction.response.send_message(f"karbar aziz ticket shoma be <@&{role.id}> erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      elif "More" in role.name  :
        I = discord.utils.get(interaction.guild.channels, name="📧⟫ More Ticket")
        await interaction.channel.edit(category=I)
        await interaction.response.send_message(f"karbar aziz ticket shoma be Vahede marbote erja dade shod <a:1134verifiedanimated:1060165061202694154>")
      else:
        # await interaction.response.send_message("Role M")
        vaght = datetime.now().strftime("%H:%M")
        embed2=discord.Embed( color=0xff0000 ) # F-Strings!
        embed2.set_author(name=f"Emkan pend kardan be in role vojod nadarad !!", icon_url="https://cdn.discordapp.com/attachments/1062485398779080754/1069345548290760877/Galaxy.png")
        embed2.set_footer(text=  f"Coded by Arman Leader#1211 |  {vaght} ")
        await interaction.response.send_message(embed=embed2)
    else : 
        vaght = datetime.now().strftime("%H:%M")
        embed2=discord.Embed( color=0xff0000 ) # F-Strings!
        embed2.set_author(name=f"In text channel ticket nemibashad !!", icon_url="https://cdn.discordapp.com/attachments/1062485398779080754/1069345548290760877/Galaxy.png")
        embed2.set_footer(text=  f"Coded by Arman Leader#1211 |  {vaght} ")
        await interaction.response.send_message(embed=embed2)







@client.tree.command(name="b2" , description="Backstory decline ( staff only ) 🟥")
async def b2(interaction:discord.Integration ,  user:discord.User):
    if 1018627140868112414 in [ y.id for y in interaction.user.roles]:
      aks = user.avatar.url
      channel = await client.fetch_channel(1060155712757579817)
      my_server= await client.fetch_guild(700974891930746910)
      rele = role_id = 1015948382713425991
      role = my_server.get_role(role_id)
      embed2=discord.Embed( color=0xff0000 ) # F-Strings!
      await user.remove_roles(role)
      embed2.set_author(name=f"{user.name} aziz backstory shoma decline shod baray etelaat bishtar be website moraje konid !", icon_url=aks)
      #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
      # await interaction.response.send_message(embed=embed2)
      await interaction.response.send_message("Fard ba movafaghiat decline shod ! <a:1134verifiedanimated:1060165061202694154> ")
      # button=Button(label="Website!", style=embed2.ButtonStyle.green , url = "https://gcommunity.ir/%D9%86%D8%AA%DB%8C%D8%AC%D9%87-%D8%AA%DB%8C%DA%A9%D8%AA/")
      # view=View()
      # view.add_item(button)
      await channel.send(f"<@{user.id}>")
      await channel.send(embed=embed2 )
    else :
      vaght = datetime.now().strftime("%H:%M")
      embed2=discord.Embed( color=0xff0000 ) # F-Strings!
      embed2.set_author(name=f"Shoma back story support nistid !", icon_url="https://cdn.discordapp.com/attachments/1062485398779080754/1069345548290760877/Galaxy.png")
      embed2.set_footer(text=  f"Coded by Arman Leader#1211 |  {vaght} ")
      await interaction.response.send_message(embed=embed2)




# hr = [918852486406766603 , 742798693123752078 , 888526993778438175 , 731756815787753502 , 733861681335107634 ]
wl = [ 1036285075798634586 , 1018820861437943830 , 1018820728377843712 , 1057016535807430676 , 1019708500076662915 , 700974891985403944 , 1059141299455926284 , 1019707960722731029 , 1019706534445461514 , 1043916495782150194, 1051506976225493074 , 1051506976225493074 , 1019708790704185395 , 1019707559671771216 , 1051500231776284722 , 1051500363666161684 , 1019709443241431050 , 1043911298422939759 , 1051505088490897569 , 1057071291611488306 , 1057232010625683467 , 1057232042561114202 , 1058873409209126913 , 1057071165622980669 , 1042783346465456148 , 1051504018679140364 , 1051504799465615481 , 1018825551710011413 , 1018825294175535165 , 1018825166119260242 , 1018825036347478076 , 1018824868655018054 , 1018824688413192282 , 1019704459443576892 , 1018824517323329576 , 1018824408908963860 , 1018824307528441856 , 1018824203442597969 , 1018824084538261534 , 1018823959485104148 , 1019706045502857270 , 1018821398082367488 , 1018823580399718460 , 1018823424526798941 , 1018823266296676403 , 1018823105990365215 , 1018822941942747159 , 1018822751718486067 , 1018822608273289267 , 1018822354173960213 , 1019706261484339200 , 1018820585465335829 , 1018820407958192228 , 1018820234116878366 , 1018820059868704819 , 700974891985403948 , 700974891985403949 , 1018819592937820180 , 700974891993923657 , 700974891993923658 , 700974891993923655 , 700974891993923654 , 700974891985403953 , 700974891985403952 , 700974891985403951 , 1053262498264006697 , 700974891985403947 , 700974891985403946 , 700974891985403945 , 700974891993923656 , 700974891972690039 , 700974891972690038 , 700974891972690037 , 700974891972690036 , 1019706454489436230 , 1018808888734265354 , 700974891993923660 , 700974891993923661 , 700974891993923663 , 700974891993923662 , 700974892002050048 , 700974892002050049 ]
@client.tree.command(name="giverole" , description="jahat dadan role be employee HR only🟢")
async def giverole(interaction:discord.Integration , user:discord.User , role:discord.Role ):
    aks = user.avatar.url
    if interaction.channel.id == 1046471263444533328:
        if 1060158728533463080 in [ y.id for y in interaction.user.roles]:
            if role.id in wl:
                aks = user.avatar.url
                # if role.id in rl :
                embed2=discord.Embed( color=0x00ff04 ) # F-Strings!
                await user.add_roles(role)
                embed2.set_author(name=f"{role.name} ba movafaghiat be {user.name} dade shod", icon_url=aks)
                #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
                await interaction.response.send_message(embed=embed2)
            else:
                embed3=discord.Embed( color=0xff0000 ) # F-Strings!
                embed3.set_author(name=f"In role , job role nemibashad !", icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061650550736834632/128.png")
                #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
                await interaction.response.send_message(embed=embed3)
        else:
            embed2=discord.Embed( color=0xff0000 ) # F-Strings!
            embed2.set_author(name=f"Shoma Vahed HR nistid ", icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061650550736834632/128.png")
            #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
            await interaction.response.send_message(embed=embed2)

@client.tree.command(name="removerole" , description=" jahat gereftan role az employee HR only🔴")
async def removerole(interaction:discord.Integration , user:discord.User , role:discord.Role):
    if interaction.channel.id == 1046471263444533328:
        if 1060158728533463080 in [ y.id for y in interaction.user.roles]:
            if role.id in wl:
                aks = user.avatar.url
                # if role.id in rl :
                embed2=discord.Embed( color=0xe6df0a ) # F-Strings!
                await user.remove_roles(role)
                embed2.set_author(name=f"{role.name} ba movafaghiat az {user.name} gerefte shod ! ", icon_url=aks)
                #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
                await interaction.response.send_message(embed=embed2)
            else:
                embed3=discord.Embed( color=0xff0000 ) # F-Strings!
                embed3.set_author(name=f"In role job role nemibashad !", icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061650550736834632/128.png")
                #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
                await interaction.response.send_message(embed=embed3)
        else:
            embed2=discord.Embed( color=0xff0000 ) # F-Strings!
            embed2.set_author(name=f"Shoma Vahed HR nistid ", icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061650550736834632/128.png")
            #await user.add_roles(role.utils.get(user.guild.roles, name=role2)) #add the role
            await interaction.response.send_message(embed=embed2)

@client.tree.command(name="ip" , description="ipv4 look up")
async def ip(interaction:discord.Integration , ip:str):
    if not ip:
        await interaction.response.send_message('<@{}>, Please Specify A IP Address!'.format(interaction.author.id))
        return
    rsp = requests.get('http://ip-api.com/json/'+ip).json()
    if rsp['status'] == 'fail':
        #await ctx.send('Error !\nAPI Respond: '+rsp['message']+'\nQuery: '+rsp['query'])
        embed=discord.Embed(color=0xFF0000)
        embed.add_field(name="❌ Query Failed", value="❓ Reason: "+rsp['message'])
        embed.set_footer(text="Query: "+ip)
        await interaction.response.send_message(embed=embed)
        return
    embed=discord.Embed(color=0x00FFFF)
    embed.add_field(name="✅Status: "+rsp['status'], value=f"\n\n🌍Country: {rsp['country']} \n\n🌏CountryCode: {rsp['countryCode']} \n\n🔷Region: {rsp['region']} \n\n🔷Region Name: {rsp['regionName']} \n\n🔷City: {rsp['city']} \n\n🕑TimeZone: {rsp['timezone']} \n\n🏢ISP: {rsp['isp']}\n\n🏢ISP OrgName: {rsp['org']}\n\n🏢ISP MoreInfo: {rsp['as']}", inline=False)
    embed.set_footer(text="Coded by Arman Leader | Requested IP: "+ip)
    await interaction.response.send_message(embed=embed)


    
# @client.event
# async def on_voice_state_update(member, before, after):
#   sleep(1)
#   channel2 = client.get_channel(700974895433252910)
#   text =  client.get_channel(1020359516644180058)
#   #print(after.channel.id)
#   #print(before.voicestate.self_mute)
#   #print(after.voicestate.self_mute)
#   embed=discord.Embed(title="Connect to Staff Warning"  , description=f" <@{member.id}> dar connect to staff montazere shoma hastnad. <@&700974891939266606> <@&700974891939266604>" ,  color=0x8000ff ,timestamp=datetime.datetime.utcnow() ) 
#   embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700974894921547833/1016676226234077204/Untitled-1_copy.png")
#   embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/700974894921547833/1016676226234077204/Untitled-1_copy.png")
#   if after.channel.id == 700974895433252910 : 
#     if before.channel.id != after.channel.id:
#       await text.send( f"==================== \n User <@{member.id}> is wating for <@&700974891939266606> <@&700974891939266604>")
#       message = await text.send( embed=embed )
#       await message.add_reaction("✅")
#       msgs.append(message.id)
#       #print(msgs)
#   else : 
#     pass


# @client.event
# async def on_reaction_add(reaction,user):
#   payam = reaction.message.id
#   kanal = client.get_channel(1020359516644180058)
#   if payam in msgs :
#     if reaction.emoji == '✅' :
#       if user.id != 920241788227313664 :
#         #print("true")
#         #now = datetime.now()
#         #now2 = now.strftime("%H:%M")
#         vaght=datetime.datetime.utcnow()
#         embed=discord.Embed(title=f"Responded by {user.name}✅"  , description=f" Dar Saat va tarikh {vaght} tavasot <@{user.id}> Respond Shod" ,  color=0x8000ff ) 
#         embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/700974894921547833/1016676226234077204/Untitled-1_copy.png")
#         embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/700974894921547833/1016676226234077204/Untitled-1_copy.png")
#         payam2 = await kanal.fetch_message(payam)
#         await payam2.edit(embed=embed)
#         #print(msgs)
#         #print(payam)
#   else:
#     pass

@client.event
async def on_message(msg):
    payam = msg.id
    if msg.channel.id == 1099090502185402511 : 
        if msg.author.id == 375805687529209857 :
            channel = await client.fetch_channel(1103782550167633981)
            await msg.add_reaction("🔻")
    if msg.author.id ==557628352828014614:
        if msg.channel.category.id == 1016283663870201898:
              if "تیکت شما ثبت گردید، لطفا شکیبا باشید تا در اولین فرصت تیکت شما توسط تیم استف پاسخ داده شود" in msg.content :
                response = await msg.channel.send("ba salam, lotfan jahate sor\'at bakhshidan be ravande barresie backstorye, motmaen shavid backstorye shoma az ghavanine ma peyravi mikonad.\ndar soorate niaz, mitavanid ba click rooye ✅ nemooneye backstorye ghabele ghabool ra moshahede konid.\n\nbackstory rules:\n```1. backstory bayad farsi neveshte shavad va faqed qalat emlayi bashad.\n2. backstory bayad hadaghal 200 kalame bashd.\n3. backstory bayad kamelan IC bashad va be shekle sevom shakhs neveshte shavad.\n4. backstory bayad sharhe hal character shoma bashad va paresh zamani nadashte bashad. (doran kodaki va nojavani va javani va ... zekr shavad.)\n5. dar backstory ya bayad dar Los Santos be donya amade bashid ya ba yek dalile manteghi be Los Santos mohajerat karde bashid.\n6. dar backstory bayad tarikh tavalod be surat kamel va miladi neveshte shavad.(yyyy/mm/dd)\n7. dar backstory nemitavanid dar Los Santos shoqli dashte bashid.\n8. dar payan e backstory bayad hadaqal 2 noqteye qovat va 2 noghteye za\'af character ra zekr konid.\n9. nam pedar ic va madar ic zekr shavad.```\n\n\nhamchenin lazem ast dar payan, forme zir ra takmil konid:\n```IC Name:\nDiscord Id:\nSteam hex:\nBirth date IC: (yyyy/mm/dd)\nEmail:```\n\nDar sorati ke niaz be yek backstory sample darid roye reaction 💬 click konid.")
                await response.add_reaction("💬")

@client.event
async def on_reaction_add(reaction,user):
    payam = reaction.message.id
    kanal = client.get_channel(1020359516644180058)
    if 700974891956174879 in [ y.id for y in user.roles]:
        if payam in msgs :
            if reaction.emoji == '✅' :
                if user.id != 920241788227313664 :
                    #print("true")
                    #now = datetime.now()
                    #now2 = now.strftime("%H:%M")
                    vaght = datetime.now().strftime("%H:%M:%S")
                    embed=discord.Embed(title=f"Responded by {user.name}✅"  , description=f" Dar Saat {vaght} tavasot <@{user.id}> Respond Shod" ,  color=0x02aae1 ) 
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
                    embed.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/attachments/1021739140519313408/1061639376049811569/Untitled-1_copy_copy.png")
                    payam2 = await kanal.fetch_message(payam)
                    await payam2.edit(embed=embed)
                    #print(msgs)
                    #print(payam)
    if reaction.emoji == '🔻' :
      # if payam in stream :
        channel = await client.fetch_channel(1103782550167633981)
        await channel.send(reaction.message.content)
    if reaction.emoji == "💬":
        if user.id != 707643552406044763:
            await reaction.message.channel.send("آکانه ماتسودا متولد سال ۱۹۹۹ از توکیو ژاپن در یک خانواده نسبتاً ثروتمند با مادر و پدری ژاپنی-امریکایی به نام آسامی و هارو چشم به جهان بیکران گشود. او تنها فرزند خانواده ماتسودا بود که کودکی اش سرشار از محبت مادری و عشق پدری بود. اکانه از همان کودکی با کتاب خودش را سرگرم میکرد و اکثر اوقات فراغت خود را به درست کردن نوشیدنی های مختلف با مادرش میگذراند. او دختری با نشاط و شاد بود که در جامعه و خانواده مورد محبت قرار میگرفت. پدر اکانه قاچاقچی موادمخدر بود و مادر وی در کلاب مشغول به کار بارتندر بود. اکانه فردی بسیار باهوش و در عین حال بازیگوش بود و کودکی مهیجی داشت. او اکثرا اوقات فراغت خود را مثل اغلب کودکان با بازی کردن و مطالعه میگذراند. او را از کودکی با فرمول های مختلف نوشیدنی ها آشنا کرده بودند و از دوران نوجوانی اش هسته علاقه مندی را در دلش نهادند. اکانه دوران دبستان را مثل بقیه افراد به خوبی سپری کرد و همچنین نوجوانی اش با روحیه ای خونسردانه و در عین حال استوار سپری می شد. او که از همان موقع تصمیمش را برای ادامه تحصیل در رشته میکسولوژی گرفته بود، برای تحصیل در رشته میکسولوژی به صورت تخصصی به سن دیگو امریکا اپلای کرد و با توجه به نمرات و استعداد عالی اش به سرعت آفر تحصیلی را دریافت کرده و عازم سن دیگو میشود. او در سن ۱۸ سالگی دوره عمومی میکسولوژی را شروع کرده و با پشتکار و کوشایی به موفقیت های زیادی دست یافت. او از آنجایی که دختری خود ساخته بود همزمان با تحصیل، در یک کلاب هم به عنوان بارتندر همانند مادرش مشغول به کار شده و در کنار کسب مهارت و تجربه، درآمد اندکی هم به دست میاورد. اکانه ۲۱ ساله بود که دوره عمومی میکسولوژی را به اتمام رساند و برای ادامه تحصیل در مقطع تخصصی میکسولوژی در دانشگاه سندیگو اقدام کرد. سرانجام اکانه ماتسودا ۲۳ ساله از دانشگاه سندیگو با مدرک تخصصی میکسولوژی فارغ التحصیل شد، به دلیل پیشنهاد کاری به لوس سانتوس مهاجرت کرد ، زندگی خود را شروع کرده و برگ جدیدی از نعمت الهی را ورق بزنند.\nنقاط ضعف: عجول بودن، زود باور بودن،فردگرا، واکنش پذیر،مغرور.\nنقاط قوت: خلاق، تمرکز بالا، خونسرد، باهوش، پشتکار،پایداری،مطالعه گر، مهربان، اجتماعی.")


client.run('')