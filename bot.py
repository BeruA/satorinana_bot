import discord
import asyncio
import random
import time
import os
import re

app = discord.Client()

@app.event
async def on_ready():
    print('Logged in as')
    print(app.user.name)
    print(app.user.id)
    await app.change_presence(game=discord.Game(name="도움말 = 저기, 명령어"))

@app.event
async def on_member_join(member):
    fmt = '{0.mention}님! 어서오세요~'
    channel = member.server.get_channel("495166582113173506")
    await app.send_message(channel, fmt.format(member, member.server))
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("495166582113173506")
    fmt = '{0.mention}님! 언젠가 다시 만나요~'
    await app.send_message(channel, fmt.format(member, member.server))

@app.event
async def on_message(message):
    
    if message.author.bot:
        return None
    
    if message.content.startswith('저기, 명령어'):
        embed = discord.Embed(title="명령어에요~", description="`저기, [분야] 명령어`로 더 자세하게 보실수 있어요~\n# 분야 \n`기능,친목,게임,대화`", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 기능 명령어'):
        embed = discord.Embed(title="기능", description="# 역할 부여\n* 저기, 역할 추가 [역할 이름]\n* 저기, 역할 제거 [역할 이름]\n`나나봇의 역할보다 아래에 있는 역할들만 줄 수 있습니다!`\n\n# 알리미\n* 저기, 묵언수행\n* 저기, 잘꺼야\n`체팅을 치지 않은 시간을 카운트 함`\n\n# 추가 기능\n* 저기, 골라 [경우1 경우2ㆍㆍㆍ경우a]\n* 저기, 주사위\n* 저기, 사다리 [인원1 인원2 ㆍㆍㆍ 인원a/팀1 팀2ㆍㆍㆍ팀a]", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 역할 추가'):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(app.get_all_members(), id=message.author.id)
        for i in message.server.roles:
            if i.name == rolename[3]:
                role = i
                break
        await app.add_roles(member, role)
        await app.send_message(message.channel, '추가해드렸어요~')

    if message.content.startswith('저기, 역할 제거'):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(app.get_all_members(), id=message.author.id)
        for i in message.server.roles:
            if i.name == rolename[3]:
                role = i
                break
        await app.remove_roles(member, role)
        await app.send_message(message.channel, '제거해드렸어요~')

    if message.content.startswith('저기, 주사위'):
        await app.send_message(message.channel, '데구르르르르르르~')
        time.sleep(2)
        dice = 0
        dice = dice + random.randint(1, 6)
        dice = str(dice)
        await app.send_message(message.channel, "" + dice + "가 나왔네요~")

    if message.content.startswith('저기, 시작 베스킨'):
        if os.path.isfile(message.server.id + "baskin.txt"):
            await app.send_message(message.channel, "이미 시작 했어요~")

        else:
            f = open(message.server.id + "baskin.txt", 'w')
            f.write("31")
            await app.send_message(message.channel,"네네~ 시작합니다~")

    if message.content.startswith('저기, 베스킨'):
        f = open(message.server.id + "baskin.txt", 'r')
        past_warn = f.read()
        f.close()
        team = message.content[7:]
        if  int(team) >= 1 and int(team) <= 3:
            now_warn = int(past_warn) - int(team)
            now_warn = str(now_warn)
            f = open(message.server.id + "baskin.txt", 'w')
            f.write(now_warn)
            f.close()
            if  int(now_warn) <= 0:
                await app.add_roles(member, role)
                await app.send_message(message.channel, "<@" + message.author.id + ">")
                embed = discord.Embed(title="탈락이에요~", description="저런~", color=0xFC67E0)
                embed.set_footer(text = "다시 해보세요~")
                await app.send_message(message.channel, embed=embed)
                os.remove(message.server.id + "baskin.txt")
            else:
                await app.send_message(message.channel, "다음 차례~")

        else:
            await app.send_message(message.channel, "<@" + message.author.id + "> 1~3사이의 숫자를 말해주세요~")
            

    if message.content.startswith('저기, 시작 젠가'):
        if os.path.isfile(message.server.id + "jenga.txt"):
            await app.send_message(message.channel, "이미 시작 했어요~")

        else:
            f = open(message.server.id + "jenga.txt", 'w')
            f.write("100")
            await app.send_message(message.channel,"네네~ 시작합니다~")


    if message.content.startswith('저기, 젠가'):
        f = open(message.server.id + "jenga.txt", 'r')
        past_warn = f.read()
        f.close()
        ram = random.randint(0, 20)
        now_warn = int(past_warn) - int(ram)
        now_warn = str(now_warn)
        f = open(message.server.id + "jenga.txt", 'w')
        f.write(now_warn)
        f.close()
        if  int(now_warn) <= 0:
            await app.add_roles(member, role)
            await app.send_message(message.channel, "<@" + message.author.id + ">")
            embed = discord.Embed(title="탈락이에요~", description="저런~", color=0xFC67E0)
            embed.set_footer(text = "다시 해보세요~")
            await app.send_message(message.channel, embed=embed)
            os.remove(message.server.id + "jenga.txt")

        else:
            await app.send_message(message.channel, "다음 차례~")
            
    if message.content.startswith('저기, 싸우자'):
        if message.content[7:].startswith(' <@'):
            vmention_id = re.findall(r'\d+', message.content)
            vmention_id = vmention_id[0]
            vmention_id = str(vmention_id)
            if os.path.isfile(" v " + message.server.id + " _ " + vmention_id + ".txt"):
                f = open(" v " + message.server.id + " _ " + vmention_id + ".txt", 'r')
                past_warn = f.read()
                f.close()
                ram = random.randint(0, 30)
                now_warn = int(past_warn) - int(ram)
                now_warn = str(now_warn)
                ram = str(ram)
                f = open(" v " + message.server.id + " _ " + vmention_id + ".txt", 'w')
                f.write(now_warn)
                f.close()
                await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + vmention_id + "> 님에게 `" + ram + "`데미지를 입히셨어요~")
                time.sleep(0.5)
                if int(now_warn) <= 0:
                    await app.send_message(message.channel, "<@" + vmention_id + ">")
                    embed = discord.Embed(title="사망하셨어요~", description="저런~", color=0xFC67E0)
                    embed.set_footer(text = "다음엔 잘 하실꺼에요~")
                    await app.send_message(message.channel, embed=embed)
                    os.remove(" v " + message.server.id + " _ " + vmention_id + ".txt")
                    
                else:
                    await app.send_message(message.channel, "<@" + vmention_id + "> 님의 남은 체력은 `" + now_warn + "`~")
            else:
                f = open(" v " + message.server.id + " _ " + vmention_id + ".txt", 'w')
                f.write("100")
                f.close()
                await app.send_message(message.channel,"<@" + vmention_id + "> 는 필드에 스폰되셨어요~")
        else:
            await app.send_message(message.channel, "명령어를 정확히 써주세요~")

    if message.content.startswith('저기, 죽지마'):
        if message.content[7:].startswith(' <@'):
            vmention_id = re.findall(r'\d+', message.content)
            vmention_id = vmention_id[0]
            vmention_id = str(vmention_id)
            if os.path.isfile(" v " + message.server.id + " _ " + vmention_id + ".txt"):
                f = open(" v " + message.server.id + " _ " + vmention_id + ".txt", 'r')
                past_warn = f.read()
                f.close()
                ram = random.randint(-15, 30)
                now_warn = int(past_warn) + int(ram)
                now_warn = str(now_warn)
                ram = str(ram)
                f = open(" v " + message.server.id + " _ " + vmention_id + ".txt", 'w')
                f.write(now_warn)
                f.close()
                await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + vmention_id + "> 님에게 `" + ram + "`의 체력을 회복하주셨어요~")
                time.sleep(0.5)
                if int(now_warn) > 150:
                    await app.send_message(message.channel, "<@" + vmention_id + "> 님은 체력이 과다해서 폭팔했네요~")
                    time.sleep(1)
                    await app.send_message(message.channel, "<@" + vmention_id + ">")
                    embed = discord.Embed(title="사망하셨어요~", description="저런~", color=0xFC67E0)
                    embed.set_footer(text = "다음엔 잘 하실꺼에요~")
                    await app.send_message(message.channel, embed=embed)
                    os.remove(" v " + message.server.id + " _ " + vmention_id + ".txt")

                if int(now_warn) <= 0:
                    await app.send_message(message.channel, "<@" + vmention_id + ">")
                    embed = discord.Embed(title="사망하셨어요~", description="저런~", color=0xFC67E0)
                    embed.set_footer(text = "다음엔 잘 하실꺼에요~")
                    await app.send_message(message.channel, embed=embed)
                    os.remove(" v " + message.server.id + " _ " + vmention_id + ".txt")
                    
                else:
                    await app.send_message(message.channel, "<@" + vmention_id + "> 님의 남은 체력은 `" + now_warn + "`~")
            else:
                await app.send_message(message.channel,"<@" + vmention_id + "> 님을 먼저 스폰해주세요~")
        else:
            await app.send_message(message.channel, "명령어를 정확히 써주세요~")

access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
