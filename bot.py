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
async def on_message(message):
    
    if message.author.bot:
        return None
    
    if message.content.startswith('저기, 명령어'):
        embed = discord.Embed(title="명령어에요~", description="`저기, [분야] 명령어`로 더 자세하게 보실수 있어요~\n# 분야 \n`기능,친목,게임,대화`", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 기능 명령어'):
        embed = discord.Embed(title="기능", description="# 역할 부여\n* 저기, 역할 추가 [역할 이름]\n* 저기, 역할 제거 [역할 이름]\n`나나봇의 역할보다 아래에 있는 역할들만 줄 수 있습니다!`\n\n# 알리미\n* 저기, 묵언수행\n* 저기, 잘꺼야\n`체팅을 치지 않은 시간을 카운트 합니다`\n\n# 추가 기능\n* 저기, 골라 [경우1 경우2ㆍㆍㆍ경우a]\n* 저기, 주사위\n* 저기, 사다리 [인원1 인원2 ㆍㆍㆍ 인원a/팀1 팀2ㆍㆍㆍ팀a]", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 친목 명령어'):
        embed = discord.Embed(title="기능", description="# 마감\n* 저기, 마감 [@맨션]\n`맨션당한 유저에게 일정량의 마감을 가감합니다`\n`처음엔 무조건 1개로 결정`\n\n# 전투\n* 저기, 싸우자 [@맨션]\n`맨션당한 유저를 공격합니다`\n`처음엔 스폰을 먼저 합니다`\n* 저기, 죽지마 [@맨션]\n`맨션당한 유저를 회복합니다`", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 게임 명령어'):
        embed = discord.Embed(title="기능", description="# 베스킨 라빈스 31\n* 저기, 시작 베스킨\n* 저기, 베스킨 [숫자]\n\n# 젠가(폭탄 돌리기)\n* 저기, 시작 젠가\n* 저기, 젠가", color=0xFC67E0)
        embed.set_footer(text = "문의는 `BeruA#7777`")
        await app.send_message(message.channel, embed=embed)
        
    if message.content.startswith('저기, 대화 명령어'):
        embed = discord.Embed(title="기능", description="# 소라고동님\n* 저기, 소라고동님 [할 말]\n\n# 따라쟁이\n* 저기, 나나\n`나나의 대답 후 할 말을 적으면 그대로 따라합니다`\n\n# 기타\n`거울, 히오스, 베루아, 업데이트, 베가스, 에펙, 에펠, 시포디, 안녕하살법`\n\n# 봇 정보\n`자기소개, 패치노트, 제작자`", color=0xFC67E0)
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
            
    if message.content.startswith('저기, 마감'):
        if message.content[6:].startswith(' <@'):
            mention_id = re.findall(r'\d+', message.content)
            mention_id = mention_id[0]
            mention_id = str(mention_id)
            if os.path.isfile(message.server.id + " _ " + mention_id + ".txt"):
                f = open(message.server.id + " _ " + mention_id + ".txt", 'r')
                past_warn = f.read()
                f.close()
                ram = random.randint(-5, 10)
                now_warn = int(past_warn) + int(ram)
                now_warn = str(now_warn)
                ram = str(ram)
                f = open(message.server.id + " _ " + mention_id + ".txt", 'w')
                f.write(now_warn)
                f.close()
                await app.send_message(message.channel, '두구두구두구두구~')
                time.sleep(0.5)
                if int(ram) == 0:
                    await app.send_message(message.channel, "0개가 나왔네요~")

                elif int(ram) > 0 and int(ram) < 7:
                    await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + mention_id + "> 님한테 마감 `" + ram + "`개를 선물해주셨어요~\n")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`을 `" + now_warn + "개`나 가지고 계시네요~")

                elif int(ram) >= 7:
                    await app.send_message(message.channel, "대박~!!!")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + mention_id + "> 님한테 엄청난 양의 마감 `" + ram + "`개를 선물로 주셨어요~!!\n")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`을 `" + now_warn + "개`나 가지고 계시네요~")

                elif int(ram) < 0:
                    await app.send_message(message.channel, "천사같은<@" + message.author.id + "> 님이 <@" + mention_id + "> 님한테 마감 `" + ram + "`개를 해결해주셨네요~\n")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`을 `" + now_warn + "개`나 가지고 계시네요~")
            else:
                f = open(message.server.id + " _ " + mention_id + ".txt", 'w')
                f.write("1")
                f.close()
                await app.send_message(message.channel,"축하드려요~!\n<@" + message.author.id + "> 님이 쑥쓰러워 하면서 <@" + mention_id + "> 님한테 첫 `마감`을 선물해주셨어요~\n<@" + mention_id + "> 님은 열심히 해주세요~!")
        else:
            await app.send_message(message.channel, "명령어를 정확히 써주세요~")

    if message.content.startswith("저기, 사다리"):
        await app.send_message(message.channel, '사다리를 타는 중이에요~')
        time.sleep(2)
        team = message.content[8:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await app.send_message(message.channel, "`" + person[i] + "`  ------>>  `" + teamname[i] + "`")
        
    if message.content.startswith('저기, 골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice)-1)
        choiceresult = choice[choicenumber]
        await app.send_message(message.channel, '흐음~')
        time.sleep(1)
        await app.send_message(message.channel, '나나는...')
        time.sleep(2)
        await app.send_message(message.channel, "`" + choiceresult + "`이게 더 좋은 것 같아요~")

    if message.content.startswith('저기, 소라고동님'):
        anser = "좋아요~ 잘모르겠어요~ 글쎄요~"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber-1]
        await app.send_message(message.channel, anserresult)
        
    if message.content.startswith('저기, 자기소개'):
        await app.send_message(message.channel, '사토리 나나에요~')
        
    if message.content.startswith('저기, 거울'):
        await app.send_message(message.channel, "<@" + message.author.id + ">")

    if message.content.startswith('저기, 히오스'):
        await app.send_message(message.channel, '시공조아~')
        
    if message.content.startswith('심심'):
        await app.send_message(message.channel, '저랑 놀아요~')
        
    if message.content.startswith('저기, 베루아'):
        await app.send_message(message.channel, "제작자에요~ `BeruA#7777`")

    if message.content.startswith('저기, 업데이트'):
        await app.send_message(message.channel, '주말에만 가능해요~')
        
    if message.content.startswith('저기, 베가스'):
        await app.send_message(message.channel, '응답없음')

    if message.content.startswith('저기, 에펙'):
        await app.send_message(message.channel, '응답없음')

    if message.content.startswith('저기, 리퍼'):
        await app.send_message(message.channel, '응답없음')

    if message.content.startswith('저기, 에펠'):
        await app.send_message(message.channel, '응답없음')

    if message.content.startswith('저기, 시포디'):
        await app.send_message(message.channel, '응답없음')
        
    if message.content.startswith('저기, 안녕하살법'):
        await app.send_message(message.channel, '안녕하살법 받아치기~!')

    if message.content.startswith('저기, 패치노트'):
        embed = discord.Embed(title="사토리 나나", description="즘봇의 순한 버전이에요~", color=0xFC67E0)
        embed.set_footer(text = "제작자 - 베루아[BeruA#7777]")
        embed.set_image(url="https://i.imgur.com/vT9PnlU.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('저기, 제작자'):
        embed = discord.Embed(title="베루아", description="고3인데 이런거나 만들고있어요~", color=0xFC67E0)
        embed.set_footer(text = "BeruA#7777")
        embed.set_image(url="https://i.imgur.com/bcgllBS.png")
        await app.send_message(message.channel, embed=embed)
        
    elif message.content.startswith('저기, 나나'):
        await app.send_message(message.channel, '네~?')
        msg = await app.wait_for_message(timeout=5.0, author=message.author)
 
        if msg is None:
            await app.send_message(message.channel, '왜 부르셨을까요~~')
            return
        else:
            await app.send_message(message.channel, msg.content)
            
    elif message.content.startswith('저기, 끝말잇기'):
        await app.send_message(message.channel, '저부터 할게요~ `핀셋`')
        msg = await app.wait_for_message(timeout=3.0, author=message.author)
 
        if msg is None:
            await app.send_message(message.channel, '저가 이겼네요~')
            return
        else:
            await app.send_message(message.channel, '저가 너무 심했나요~')

    elif message.content.startswith('저기, 묵언수행'):
        await app.send_message(message.channel, '인내심이 어느정도인지 봐드리죠~\n`체팅이 없는 시간대에는 도배처럼 보일수 있으니 조심하세요~`')
        msg = await app.wait_for_message(timeout=60.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, "와~ <@" + message.author.id + "> 1분 경과~!")
            msg = await app.wait_for_message(timeout=540.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, "와~ <@" + message.author.id + "> 10분 경과~!")
                msg = await app.wait_for_message(timeout=3000.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, "와~ <@" + message.author.id + "> 1시간 경과~!")
                    msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                    if msg is None:
                        await app.send_message(message.channel, "와~ <@" + message.author.id + "> 2시간 경과~!")
                        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                        if msg is None:
                            await app.send_message(message.channel, "와~ <@" + message.author.id + "> 3시간 경과~!")
                            msg = await app.wait_for_message(timeout=7200.0, author=message.author)

                            if msg is None:
                                await app.send_message(message.channel, "와~ <@" + message.author.id + "> 5시간 경과~!")
                                msg = await app.wait_for_message(timeout=7200.0, author=message.author)

                                if msg is None:
                                    await app.send_message(message.channel, "와~ <@" + message.author.id + "> 7시간 경과~!")
                                    msg = await app.wait_for_message(timeout=10800, author=message.author)

                                    if msg is None:
                                        await app.send_message(message.channel, "와~ <@" + message.author.id + "> 10시간 경과~! 대단하네요~")
                                        return

                                    else:
                                        await app.send_message(message.channel, '아쉽다~ 10시간은 못 버티셨네요~')
                                else:
                                    await app.send_message(message.channel, '아쉽다~ 7시간은 못 버티셨네요~')
                            else:
                                await app.send_message(message.channel, '아쉽다~ 5시간은 못 버티셨네요~')
                        else:
                            await app.send_message(message.channel, '아쉽다~ 3시간은 못 버티셨네요~')
                    else:
                        await app.send_message(message.channel, '아쉽다~ 2시간은 못 버티셨네요~')
                else:
                    await app.send_message(message.channel, '아쉽다~ 1시간은 못 버티셨네요~')
            else:
                await app.send_message(message.channel, '아쉽다~ 10분은 못 버티셨네요~')
        else:
            await app.send_message(message.channel, '1분도 못 버티셨네요~')
            
    elif message.content.startswith('저기, 잘꺼야'):
        await app.send_message(message.channel, '안녕히 주무세요~\n`체팅이 없는 시간대에는 도배처럼 보일수 있으니 조심하세요~`')
        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 1시간째...")
            msg = await app.wait_for_message(timeout=7200.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 3시간째...")
                msg = await app.wait_for_message(timeout=3600.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 4시간째...")
                    msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                    if msg is None:
                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 5시간째...")
                        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                        if msg is None:
                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 6시간째...")
                            msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                            if msg is None:
                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 7시간째...")
                                msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                                if msg is None:
                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 8시간째...")
                                    msg = await app.wait_for_message(timeout=3600, author=message.author)

                                    if msg is None:
                                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 9시간째...")
                                        msg = await app.wait_for_message(timeout=3600, author=message.author)

                                        if msg is None:
                                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 10시간째...")
                                            msg = await app.wait_for_message(timeout=3600, author=message.author)

                                            if msg is None:
                                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 11시간째...")
                                                msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                if msg is None:
                                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 12시간째...")
                                                    msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                    if msg is None:
                                                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 13시간째...")
                                                        msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                        if msg is None:
                                                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 14시간째...")
                                                            msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                            if msg is None:
                                                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 15시간째...")
                                                                msg = await app.wait_for_message(timeout=3600, author=message.author)
                                                                
                                                                if msg is None:
                                                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 16시간째...")
                                                                    msg = await app.wait_for_message(timeout=3600, author=message.author)
                                                                    
                                                                    if msg is None:
                                                                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 17시간째...")
                                                                        msg = await app.wait_for_message(timeout=3600, author=message.author)
                                                                        
                                                                        if msg is None:
                                                                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 18시간째...")
                                                                            msg = await app.wait_for_message(timeout=3600, author=message.author)
                                                                            
                                                                            if msg is None:
                                                                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 19시간째...")
                                                                                msg = await app.wait_for_message(timeout=3600, author=message.author)
                                                                                
                                                                                if msg is None:
                                                                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">님은 꿈나라에 간지 20시간째...더는 못 세겠어요~")
                                                                                    return
                                                                                
                                                                                else:
                                                                                    await app.send_message(message.channel, "<@" + message.author.id + "> 19시간 주무셨어요~")
                                                                            else:
                                                                                await app.send_message(message.channel, "<@" + message.author.id + "> 18시간 주무셨어요~")
                                                                        else:
                                                                            await app.send_message(message.channel, "<@" + message.author.id + "> 17시간 주무셨어요~")
                                                                    else:
                                                                        await app.send_message(message.channel, "<@" + message.author.id + "> 16시간 주무셨어요~")
                                                                else:
                                                                    await app.send_message(message.channel, "<@" + message.author.id + "> 15시간 주무셨어요~")
                                                            else:
                                                                await app.send_message(message.channel, "<@" + message.author.id + "> 14시간 주무셨어요~")
                                                        else:
                                                            await app.send_message(message.channel, "<@" + message.author.id + "> 13시간 주무셨어요~")
                                                    else:
                                                        await app.send_message(message.channel, "<@" + message.author.id + "> 12시간 주무셨어요~")
                                                else:
                                                    await app.send_message(message.channel, "<@" + message.author.id + "> 11시간 주무셨어요~")
                                            else:
                                                await app.send_message(message.channel, "<@" + message.author.id + "> 10시간 주무셨어요~")
                                        else:
                                            await app.send_message(message.channel, "<@" + message.author.id + "> 9시간 주무셨어요~")
                                    else:
                                        await app.send_message(message.channel, "<@" + message.author.id + "> 8시간 주무셨어요~")
                                else:
                                    await app.send_message(message.channel, "<@" + message.author.id + "> 7시간 주무셨어요~")
                            else:
                                await app.send_message(message.channel, "<@" + message.author.id + "> 6시간 주무셨어요~")
                        else:
                            await app.send_message(message.channel, "<@" + message.author.id + "> 5시간 주무셨어요~")
                    else:
                        await app.send_message(message.channel, "<@" + message.author.id + "> 4시간 주무셨어요~")
                else:
                    await app.send_message(message.channel, "<@" + message.author.id + "> 3시간 주무셨어요~")
            else:
                await app.send_message(message.channel, "<@" + message.author.id + "> 1시간 주무셨어요~")
        else:
            await app.send_message(message.channel, "<@" + message.author.id + "> 아직 안주무시네요~")
            
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
