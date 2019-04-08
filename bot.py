import discord
import asyncio
import random
import time
import os, discord, asyncio, re

a = "asdf"

app = discord.Client()

@app.event
async def on_ready():
    print('Logged in as')
    print(app.user.name)
    print(app.user.id)
    await app.change_presence(game=discord.Game(name="명령어 = 저기,"))

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
        await app.send_message(message.channel, '준비중이에요~')
        
    if  message.content.startswith('저기, 역할 추가'):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(app.get_all_members(), id=message.author.id)
        for i in message.server.roles:
            if i.name == rolename[3]:
                role = i
                break
        await app.add_roles(member, role)
        await app.send_message(message.channel, '추가해드렸어요~')

    if  message.content.startswith('저기, 역할 제거'):
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
            await app.send_message(message.channel, "다음 차례")

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
                    role = ""
                    member = discord.utils.get(app.get_all_members(), id=vmention_id)
                    for i in message.server.roles:
                        if i.name == "패배자":
                            role = i
                            break
                    await app.add_roles(member, role)
                    await app.send_message(message.channel, "<@" + vmention_id + ">")
                    embed = discord.Embed(title="사망!!!", description="하하하하하하하하하하하하하하하하하", color=0xFC67E0)
                    embed.set_footer(text = "패 배 자")
                    embed.set_image(url="https://i.imgur.com/F0c4egd.jpg")
                    await app.send_message(message.channel, embed=embed)
                    os.remove(" v " + message.server.id + " _ " + vmention_id + ".txt")
                    
                else:
                    await app.send_message(message.channel, "<@" + vmention_id + "> 의 남은 체력은 `" + now_warn + "`!!")

            else:
                await app.send_message(message.channel,"<@" + vmention_id + "> 룰 스폰해주세요 시발아")
        else:
            await app.send_message(message.channel, "똑바로 써 병신아")
            

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
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`이 `" + now_warn + "개`나 가지고 계시네요~")

                elif int(ram) >= 7:
                    await app.send_message(message.channel, "대박~!!!")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + message.author.id + "> 님이 <@" + mention_id + "> 님한테 엄청난 양의 마감 `" + ram + "`개를 해주셨어요~!!\n")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`이 `" + now_warn + "개`나 가지고 계시네요~")

                elif int(ram) < 0:
                    await app.send_message(message.channel, "천사같은<@" + message.author.id + "> 님이 <@" + mention_id + "> 님한테 마감 `" + ram + "`개를 해결해주셨네요~\n")
                    time.sleep(0.5)
                    await app.send_message(message.channel, "<@" + mention_id + "> 님은 `마감`이 `" + now_warn + "개`나 가지고 계시네요~")
            else:
                f = open(message.server.id + " _ " + mention_id + ".txt", 'w')
                f.write("1")
                f.close()
                await app.send_message(message.channel,"축하드려요~!\n<@" + message.author.id + "> 님이 쑥쓰러워 하면서 <@" + mention_id + "> 님한테 첫 `마감`을 선물해주셨어요~\n<@" + mention_id + "> 님은 열심히 해주세요~!")
        else:
            await app.send_message(message.channel, "명령어를 정확히 써주세요~")


    if message.content.startswith("야! 사다리타기"):
        await app.send_message(message.channel, '따라다라 딴! 딴!')
        time.sleep(0.5)
        await app.send_message(message.channel, '따라다라 딴! 딴!')
        time.sleep(0.5)
        await app.send_message(message.channel, '따라다라 따라라라...')
        time.sleep(2)
        team = message.content[9:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await app.send_message(message.channel, "`" + person[i] + "` 넌 `" + teamname[i] + "` 일로가")
        
    if message.content.startswith('야! 골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice)-1)
        choiceresult = choice[choicenumber]
        await app.send_message(message.channel, '코카콜라 맛있다')
        time.sleep(0.5)
        await app.send_message(message.channel, '맛있으면 또 먹어')
        time.sleep(0.5)
        await app.send_message(message.channel, '또 먹으면 배탈나')
        time.sleep(0.5)
        await app.send_message(message.channel, '척척박사님 알아맞춰보세요')
        time.sleep(0.5)
        await app.send_message(message.channel, '딩동댕동')
        await app.send_message(message.channel, "`" + choiceresult + "`코코스키")

    if message.content.startswith('마법의 즘라고동님'):
        anser = "응~안돼 하지마 해보던가 알아서하셈 아똥마려 ㄲㅈ ㅗ ㅄ ㅉㅉ 작작물어봐 왜나한테물어봄 응아니야"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber-1]
        await app.send_message(message.channel, anserresult)
        
    if message.content.startswith('야! 거울'):
        await app.send_message(message.channel, "<@" + message.author.id + ">")

    if message.content.startswith('야! 소형빈'):
        await app.send_message(message.channel, '친구는 대형빈')

    if message.content.startswith('야! 히오스'):
        await app.send_message(message.channel, '너...그런거 하니??')

    if message.content.startswith('야! 게타'):
        await app.send_message(message.channel, '담배만세~')

    if message.content.startswith('야! 은갈치'):
        await app.send_message(message.channel, '아몰랑 한남은 왜 깝치는 건주')

    if message.content.startswith('야! 자기소개'):
        await app.send_message(message.channel, '귀찮음')

    if message.content.startswith('개띠껍네'):
        await app.send_message(message.channel, '하하하하하하하하')

    if message.content.startswith('띠껍'):
        await app.send_message(message.channel, '하하하하하하하하')

    if message.content.startswith('즘킂'):
        await app.send_message(message.channel, '나 부름?')

    if message.content.startswith('봇'):
        await app.send_message(message.channel, '나 부름?')

    if message.content.startswith('심심'):
        await app.send_message(message.channel, '나랑 놀자')

    if message.content.startswith('똥'):
        await app.send_message(message.channel, '스프른이 좋아함')

    if message.content.startswith('야! 현탁이'):
        await app.send_message(message.channel, '횬탁이')

    if message.content.startswith('야! 밍'):
        await app.send_message(message.channel, '우 레사레사~')

    if message.content.startswith('야! 베루아'):
        await app.send_message(message.channel, '단발은 비추야')

    if message.content.startswith('야! 수선배'):
        await app.send_message(message.channel, '이키스기....이쿠...이쿠....응아앗(≧Д≦)')

    if message.content.startswith('야! 농심'):
        await app.send_message(message.channel, '농심이 그런 회사였구나...')

    if message.content.startswith('야! 진짬뽕'):
        await app.send_message(message.channel, '오오~ 짬뽕이네~')

    if message.content.startswith('야! 짱깨'):
        await app.send_message(message.channel, '야 구름미즈')

    if message.content.startswith('야! 하루카'):
        await app.send_message(message.channel, '치킨엔 마요지')

    if message.content.startswith('야! 가브릴'):
        await app.send_message(message.channel, '으으;;')

    if message.content.startswith('노'):
        await app.send_message(message.channel, '노? 신고합니다')

    if message.content.startswith('야! 동'):
        await app.send_message(message.channel, 'https://www.pornhub.com/')

    if message.content.startswith('야! 구갤러리'):
        await app.send_message(message.channel, '너...그런거 하니??')  

    if message.content.startswith('야! 자지'):
        await app.send_message(message.channel, '혁노한테 달려있는거')

    if message.content.startswith('야! 보지'):
        await app.send_message(message.channel, '혁노한테 달려있는거')

    if message.content.startswith('야! 즘좆'):
        await app.send_message(message.channel, 'ㅗ')

    if message.content.startswith('야! 똥킂'):
        await app.send_message(message.channel, 'ㅗ')

    if message.content.startswith('야! 응가'):
        await app.send_message(message.channel, '스프른의 보물 1호')

    if message.content.startswith('야! 똥좆'):
        await app.send_message(message.channel, 'ㅗㅗ')

    if message.content.startswith('야! 시미켄'):
        await app.send_message(message.channel, '안뇽? 미켄횽이야~')

    if message.content.startswith('야! 보겸'):
        await app.send_message(message.channel, '신고합니다;;')

    if message.content.startswith('야! ㅂㅇㄹ'):
        await app.send_message(message.channel, 'ㅂㅇㄹ~')

    if message.content.startswith('야! 똥깃'):
        await app.send_message(message.channel, '으으 똥 깃;')

    if message.content.startswith('야! 노무현'):
        await app.send_message(message.channel, '그립습니다...')

    if message.content.startswith('야! 탄젠트'):
        await app.send_message(message.channel, 'R분의 Y')

    if message.content.startswith('야! 혁노'):
        await app.send_message(message.channel, '보지')

    if message.content.startswith('야! 시접선'):
        await app.send_message(message.channel, '호우호우')  
            
    if message.content.startswith('야! 기분좋다'):
        await app.send_message(message.channel, '노무횬')

    if message.content.startswith('야! 오즈한'):
        await app.send_message(message.channel, 'oh yeah!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    if message.content.startswith('야! 여유만만'):
        await app.send_message(message.channel, '가방 싫어')

    if message.content.startswith('야! 김밥'):
        await app.send_message(message.channel, '야오!(좋음)')

    if message.content.startswith('야! 소주'):
        await app.send_message(message.channel, '야오!(좋음)')

    if message.content.startswith('야! 삼겹살'):
        await app.send_message(message.channel, '야오!(좋음)')

    if message.content.startswith('야! 김치'):
        await app.send_message(message.channel, '우!(싫음) 개노맛;;')

    if message.content.startswith('야! 이만'):
        await app.send_message(message.channel, '보레스타')

    if message.content.startswith('야! 진격의 싸이'):
        await app.send_message(message.channel, '오빤 거인이야! 오빤 거대한 다리로 니 마더 때리는 사나에!!')

    if message.content.startswith('야! 펄른'):
        await app.send_message(message.channel, '야~!!!! 좋~- 다~-~-~-~-~-~-~-~- 딱~!!!! 좋~- 다~-~-~-↓~-↓↓~-↓↓↓\n다~-~-~- 다 다~- 다 다~- 다 다~- 다 다~- 다 다~- 다~-~-~-~-~-~-\n다~-~-~-~-~-~- 다~-~-~-~-~-~-')

    if message.content.startswith('야! 만능열차'):
        await app.send_message(message.channel, '욧')

    if message.content.startswith('야! 유시민'):
        await app.send_message(message.channel, '알릴레오 알릴레오 알릴레오 유')

    if message.content.startswith('야! 위뚝'):
        await app.send_message(message.channel, '틱(젖가락 치는 소리)')

    if message.content.startswith('야! 나비붙이'):
        await app.send_message(message.channel, '[록음악 마니아]가 있으니까아아아아아아ㅏㅇ아아아아ㅏ아아아ㅏ아아ㅏ악!!')

    if message.content.startswith('야! 인시대'):
        await app.send_message(message.channel, '이 연극에서 주인공은 나다(팩트)')

    if message.content.startswith('야! 스오'):
        await app.send_message(message.channel, ';;')

    if message.content.startswith('야! 호'):
        await app.send_message(message.channel, '개노잼')

    if message.content.startswith('야! 싸이'):
        await app.send_message(message.channel, 'https://youtu.be/wA0UQ1bAu8k')

    if message.content.startswith('야! 샌즈'):
        await app.send_message(message.channel, 'https://i.imgur.com/emouNum.png')

    if message.content.startswith('야! 문재인'):
        await app.send_message(message.channel, '적폐...청산!')

    if message.content.startswith('야! 구름미즈'):
        await app.send_message(message.channel, '야 짱깨')

    if message.content.startswith('야! 슬라임맨'):
        await app.send_message(message.channel, '쉬벌 슬라임맨이야;')

    if message.content.startswith('야! 외노출'):
        await app.send_message(message.channel, '치마의 은밀한 취미')

    if message.content.startswith('야! 키소바'):
        await app.send_message(message.channel, '개맛있음')

    if message.content.startswith('야! 홍카콜라'):
        await app.send_message(message.channel, '문재앙 보다는 홍발정이 낫다~')

    if message.content.startswith('야! 놀자'):
        await app.send_message(message.channel, '초특가 야놀자 초특가 야놀자 초특가 야야야야야야야양 야 놀 자')

    if message.content.startswith('야! 가브릴'):
        await app.send_message(message.channel, '비추야')

    if message.content.startswith('야! 레드존'):
        await app.send_message(message.channel, '띵땅뚱땅 뚜둥땅 빠라바 띵땅뚱땅 띠딩 땅')

    if message.content.startswith('야! 허준호'):
        await app.send_message(message.channel, '地水믹')

    if message.content.startswith('야! 퓨머스'):
        await app.send_message(message.channel, 'https://youtu.be/wA0UQ1bAu8k')

    if message.content.startswith('야! 연어'):
        await app.send_message(message.channel, '야 나와')

    if message.content.startswith('야! 5등분'):
        await app.send_message(message.channel, '요츠바는 개추야')

    if message.content.startswith('야! 썬진'):
        await app.send_message(message.channel, '합성하기 위해 태어난 남자')

    if message.content.startswith('야! 미디'):
        await app.send_message(message.channel, '네류의 보물 1호')

    if message.content.startswith('야! 버스'):
        await app.send_message(message.channel, '우리가 타고다니는 것')

    if message.content.startswith('야! 도겸'):
        await app.send_message(message.channel, '렌더는 비추야')

    if message.content.startswith('야! 오빠워치'):
        await app.send_message(message.channel, 'ㅗ')

    if message.content.startswith('야! 도나'):
        await app.send_message(message.channel, '개가 공을 가지고 놀고 있습니다')

    if message.content.startswith('야! 쿠자'):
        await app.send_message(message.channel, '개노잼;')

    if message.content.startswith('야! 쿄로'):
        await app.send_message(message.channel, '레드존 초딩은 비추야')

    if message.content.startswith('야! 월곶'):
        await app.send_message(message.channel, '아 상민이만 살았습니다~ 아...')

    if message.content.startswith('야! 섹스'):
        await app.send_message(message.channel, '우리가 영원히 못하는 것')

    if message.content.startswith('야! 나가'):
        await app.send_message(message.channel, '니나 나가')

    if message.content.startswith('야! 게이'):
        await app.send_message(message.channel, '너요')

    if message.content.startswith('야! 장발'):
        await app.send_message(message.channel, 'ㅗㅜㅑㅗㅜㅑㅗㅜㅑㅗㅜㅑ')

    if message.content.startswith('야! 엔타이노'):
        await app.send_message(message.channel, '오늘은 로리 먹을꺼야!')

    if message.content.startswith('야! 정준혁'):
        await app.send_message(message.channel, '애리를 좋아함')

    if message.content.startswith('야! 드스'):
        await app.send_message(message.channel, '노코맨트')

    if message.content.startswith('야! 인마타'):
        await app.send_message(message.channel, '어깨동무 어깨동무 친구 내친구 야~?')

    if message.content.startswith('야! 에리'):
        await app.send_message(message.channel, '씨발')

    if message.content.startswith('야! 맨틀'):
        await app.send_message(message.channel, '너 왜 사람 왜 젠틀젠틀 하게 해~~~~')

    if message.content.startswith('야! 액시온'):
        await app.send_message(message.channel, '나는 띠노가 조아 띠노띠노띠노')

    if message.content.startswith('야! 상민이'):
        await app.send_message(message.channel, 'ㅋㅋㅋㅋㅋㅋㅋㅋ')

    if message.content.startswith('야! 임춘식'):
        await app.send_message(message.channel, '아임 26시간동안 나대는~')

    if message.content.startswith('야! 쭈꾸미'):
        await app.send_message(message.channel, '여유만만이 먹어야 하는 것')

    if message.content.startswith('야! 여울'):
        await app.send_message(message.channel, 'ㅅㅂ 차라리 여유만만 파트를 봐라')

    if message.content.startswith('야! 트매드'):
        await app.send_message(message.channel, '나는 땅꼬마다~ 나는....')

    if message.content.startswith('야! 세레노'):
        await app.send_message(message.channel, '어이가 없네 하하하하하하하하')

    if message.content.startswith('야! 빈모드'):
        await app.send_message(message.channel, '디스 일 빨타!')

    if message.content.startswith('야! 야!'):
        await app.send_message(message.channel, '작작불러;')

    if message.content.startswith('야! 시발'):
        await app.send_message(message.channel, '시발 쓰지 마세요')

    if message.content.startswith('야! 와타텐'):
        await app.send_message(message.channel, '먀네~')

    if message.content.startswith('야! 뱅드림'):
        await app.send_message(message.channel, '제작자가 5만원 질러놓고 안하는 것')

    if message.content.startswith('야! 짤'):
        await app.send_message(message.channel, '응 안보여줘 하하하하하하하하하')

    if message.content.startswith('야! 갤러'):
        await app.send_message(message.channel, '손절해라')

    if message.content.startswith('야! 해봐'):
        await app.send_message(message.channel, '싫은데?')

    if message.content.startswith('야! 에반스'):
        await app.send_message(message.channel, '야구선수임')

    if message.content.startswith('야! 업데이트'):
        await app.send_message(message.channel, '주말에만 함')

    if message.content.startswith('야! ㅗ'):
        await app.send_message(message.channel, '왜 선시텀;')

    if message.content.startswith('야! 짬뽕'):
        await app.send_message(message.channel, '간짬뽕이 제일 맛있더라')

    if message.content.startswith('야! 베가스'):
        await app.send_message(message.channel, '터져라')

    if message.content.startswith('야! 에펙'):
        await app.send_message(message.channel, '터져라')

    if message.content.startswith('야! 리퍼'):
        await app.send_message(message.channel, '터져라')

    if message.content.startswith('야! 에펠'):
        await app.send_message(message.channel, '터져라')

    if message.content.startswith('야! 시포디'):
        await app.send_message(message.channel, '터져라')

    if message.content.startswith('야! 수푸른'):
        await app.send_message(message.channel, '아메으리카노? 은? 은? 은? 은?')

    if message.content.startswith('야! 이명박'):
        await app.send_message(message.channel, '여러분 여러분 이거 다~ 판매왕 아시죠?')

    if message.content.startswith('야! 박근혜'):
        await app.send_message(message.channel, '바쁜 벌꿀은 슬퍼할 시간도 없다')

    if message.content.startswith('야! 안녕하살법'):
        await app.send_message(message.channel, '안녕하살법 받아치기!')

    if message.content.startswith('야! 패치노트'):
        embed = discord.Embed(title="띠꺼운 물고기(금,토,일,작동)", description="즘봇 Mk. II\n'마법의 즘라고동님'명령어 추가\n'야! 주사위'추가\n'야! 똥코인 @맨션'명령어 추가\n'야! 작작해'명령어 제거\n'야! 5초게임하자'명령어 추가\n'야! 나랑뜨자 @맨션'명령어 추가\n'야! 죽지마 @맨션'명령어 추가\n'야! ㄱㄱ베스킨' 야! 베스킨 (숫자)'명령어 추가\n'야! ㄱㄱ젠가' '야! 젠가'명령어 추가\n", color=0xFC67E0)
        embed.set_footer(text = "제작자 - 베루아[BeruA#7777]")
        embed.set_image(url="https://i.imgur.com/vT9PnlU.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 제작자'):
        embed = discord.Embed(title="나다", description="고3", color=0xFC67E0)
        embed.set_footer(text = "BeruA#7777")
        embed.set_image(url="https://i.imgur.com/bcgllBS.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 소피'):
        embed = discord.Embed(title="소 피 조 아", description="ㅗㅜㅑㅗㅜㅑ", color=0xFC67E0)
        embed.set_footer(text = "아니 이건 실 순 뒈????")
        embed.set_image(url="https://i.imgur.com/VyCWZTD.png")
        await app.send_message(message.channel, embed=embed)
    
    if message.content.startswith('야! 여우엘건'):
        embed = discord.Embed(title="여우엘건은 개추야", description="크레아 마오키나는 비추야", color=0xFC67E0)
        embed.set_footer(text = "누가 봐도 화놑이 만들어줌")
        embed.set_image(url="https://i.imgur.com/OLPf0na.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! ㅅㅂㅁㅌ'):
        embed = discord.Embed(title="다으 다으다으다으 다으다으 짠 짠짠 짠짠짠 짠짠짠 서~해~물~과", description="날씨 맑은 완행선 왕복열차에", color=0xFC67E0)
        embed.set_footer(text = "마음약해서 잡지못했네")
        embed.set_image(url="https://i.imgur.com/kQlO1d4.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 뤼기'):
        embed = discord.Embed(title="뤼 기야!!!!!!!!!!!", description="(투쉬)", color=0xFC67E0)
        embed.set_footer(text = "아 나왔어난~")
        embed.set_image(url="https://i.imgur.com/27J063X.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 시청자'):
        embed = discord.Embed(title="사타나키아 맥도웰", description="「나는 대악마, 쿠루미자와 사타니키아 맥도웰!」", color=0xFC67E0)
        embed.set_footer(text = "감투종자놈들")
        embed.set_image(url="https://i.imgur.com/ftePxs2.jpg")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 피음'):
        embed = discord.Embed(title="궁예리언", description="견찰서를 사랑하는 DVD", color=0xFC67E0)
        embed.set_footer(text = "담배만세~")
        embed.set_image(url="https://i.imgur.com/6uoSDXg.png")
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('야! 뿡져스텐'):
        embed = discord.Embed(title="뿡져스텐", description="뿡져스텐", color=0xFC67E0)
        embed.set_footer(text = "고버졁")
        embed.set_image(url="https://i.imgur.com/p8s2trY.jpg")
        await app.send_message(message.channel, embed=embed)

    elif message.content.startswith('야! 즘킂'):
        await app.send_message(message.channel, '왜')
        msg = await app.wait_for_message(timeout=5.0, author=message.author)
 
        if msg is None:
            await app.send_message(message.channel, 'ㅅㅂ 불러놓고 말을 안해')
            return
        else:
            await app.send_message(message.channel, msg.content)

    elif message.content.startswith('야! 눈치게임 하자'):
        await app.send_message(message.channel, 'ㅇㅋ 너먼저 하셈')
        msg = await app.wait_for_message(timeout=7.0, author=message.author)
 
        if msg is None:
            await app.send_message(message.channel, 'ㅅㅂ 불러놓고 왜 안해;;')
            return
        else:
            await app.send_message(message.channel, msg.content)
            await app.send_message(message.channel, '눈치 더럽게 없네;')

    elif message.content.startswith('야! 끝말잇기 하자'):
        await app.send_message(message.channel, 'ㅇㅋ 나부터 함 [기쁨]')
        msg = await app.wait_for_message(timeout=3.0, author=message.author)
 
        if msg is None:
            await app.send_message(message.channel, 'ㅋㅋㅋㅋㅋ개못하네')
            return
        else:
            await app.send_message(message.channel, '응 졌어~')

    elif message.content.startswith('야! 5초게임하자'):
        await app.send_message(message.channel, 'ㅇㅋ 시작!')
        msg = await app.wait_for_message(timeout=5.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, '5초!')
            msg = await app.wait_for_message(timeout=0.1, author=message.author)

            if msg is None:
                    await app.send_message(message.channel, '하하 무승부라고 치자')
                    return
                
            else:
                await app.send_message(message.channel, '응 지났어 하하하하하하')
            
        else:
            await app.send_message(message.channel, '응 5초 안됬어')

    elif message.content.startswith('야! 젠틀맨'):
        await app.send_message(message.channel, '아몰랑 한남은 왜 깝치는 건지;')
        msg = await app.wait_for_message(timeout=3.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, '확 자지 짤라 버린다 뤼 기야!')
            msg = await app.wait_for_message(timeout=3.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, '젠틀...?')
                msg = await app.wait_for_message(timeout=3.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, '나....일베한다 뤼 기야!!')
                    return
                
                else:
                    await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
            else:
                await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
        else:
            await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')

    elif message.content.startswith('야! 김윤수'):
        await app.send_message(message.channel, '마약이 필요해!')
        msg = await app.wait_for_message(timeout=1.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, '마약 줘!')
            msg = await app.wait_for_message(timeout=1.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, '마약좀 줘!')
                msg = await app.wait_for_message(timeout=1.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, '마약좀 주세요!')
                    msg = await app.wait_for_message(timeout=1.0, author=message.author)

                    if msg is None:
                        await app.send_message(message.channel, '마약을 주세요!!')
                        msg = await app.wait_for_message(timeout=1.0, author=message.author)

                        if msg is None:
                            await app.send_message(message.channel, '저한테 마약을 주세요!!!')
                            msg = await app.wait_for_message(timeout=1.0, author=message.author)

                            if msg is None:
                                await app.send_message(message.channel, '육각형! 그래 육각형을 주세요!!')
                                msg = await app.wait_for_message(timeout=1.0, author=message.author)

                                if msg is None:
                                    await app.send_message(message.channel, '육각형! 육각형!! 육각형!!!!')
                                    msg = await app.wait_for_message(timeout=1.0, author=message.author)

                                    if msg is None:
                                        await app.send_message(message.channel, '아 육각형!! 마약!! 아!!')
                                        return

                                    else:
                                        await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
                                else:
                                    await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
                            else:
                                await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
                        else:
                            await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
                    else:
                        await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
                else:
                    await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
            else:
                await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')
        else:
            await app.send_message(message.channel, 'ㅅㅂ 말하는데 왜 끊음;;')

            
    elif message.content.startswith('야! 묵언수행'):
        await app.send_message(message.channel, 'ㅇㅋ닥치고 있으셈')
        msg = await app.wait_for_message(timeout=60.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, "오 <@" + message.author.id + "> 1분 버팀")
            msg = await app.wait_for_message(timeout=540.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, "오 <@" + message.author.id + "> 10분 버팀")
                msg = await app.wait_for_message(timeout=3000.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, "오 <@" + message.author.id + "> 1시간 버팀")
                    msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                    if msg is None:
                        await app.send_message(message.channel, "오 <@" + message.author.id + "> 2시간 버팀")
                        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                        if msg is None:
                            await app.send_message(message.channel, "오 <@" + message.author.id + "> 3시간 버팀")
                            msg = await app.wait_for_message(timeout=7200.0, author=message.author)

                            if msg is None:
                                await app.send_message(message.channel, "오 <@" + message.author.id + "> 5시간 버팀")
                                msg = await app.wait_for_message(timeout=7200.0, author=message.author)

                                if msg is None:
                                    await app.send_message(message.channel, "오 <@" + message.author.id + "> 7시간 버팀")
                                    msg = await app.wait_for_message(timeout=10800, author=message.author)

                                    if msg is None:
                                        await app.send_message(message.channel, "오 <@" + message.author.id + "> 10시간 동안 버팀ㅋㅋㅋㅋㅋ죽은거 아니냐ㅋㅋㅋ 니가 이김 ㅊㅊ")
                                        return

                                    else:
                                        await app.send_message(message.channel, 'ㅉㅉ 10시간도 못참노')
                                else:
                                    await app.send_message(message.channel, 'ㅉㅉ 7시간도 못참노')
                            else:
                                await app.send_message(message.channel, 'ㅉㅉ 5시간도 못참노')
                        else:
                            await app.send_message(message.channel, 'ㅉㅉ 3시간도 못참노')
                    else:
                        await app.send_message(message.channel, 'ㅉㅉ 2시간도 못참노')
                else:
                    await app.send_message(message.channel, 'ㅉㅉ 1시간도 못참노')
            else:
                await app.send_message(message.channel, 'ㅉㅉ 10분도 못참노')
        else:
            await app.send_message(message.channel, 'ㅉㅉ 1분도 못참노')

    elif message.content.startswith('야! 잘꺼야'):
        await app.send_message(message.channel, '잘쟈♥')
        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

        if msg is None:
            await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 1시간째...")
            msg = await app.wait_for_message(timeout=7200.0, author=message.author)
            
            if msg is None:
                await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 3시간째...")
                msg = await app.wait_for_message(timeout=3600.0, author=message.author)
            
                if msg is None:
                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 4시간째...")
                    msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                    if msg is None:
                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 5시간째...")
                        msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                        if msg is None:
                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 6시간째...")
                            msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                            if msg is None:
                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 7시간째...")
                                msg = await app.wait_for_message(timeout=3600.0, author=message.author)

                                if msg is None:
                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 8시간째...")
                                    msg = await app.wait_for_message(timeout=3600, author=message.author)

                                    if msg is None:
                                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 9시간째...")
                                        msg = await app.wait_for_message(timeout=3600, author=message.author)

                                        if msg is None:
                                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 10시간째...")
                                            msg = await app.wait_for_message(timeout=3600, author=message.author)

                                            if msg is None:
                                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 11시간째...")
                                                msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                if msg is None:
                                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 12시간째...")
                                                    msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                    if msg is None:
                                                        await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 13시간째...")
                                                        msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                        if msg is None:
                                                            await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 14시간째...")
                                                            msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                            if msg is None:
                                                                await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 15시간째...")
                                                                msg = await app.wait_for_message(timeout=3600, author=message.author)

                                                                if msg is None:
                                                                    await app.send_message(message.channel, "우리 <@" + message.author.id + ">는 꿈나라에 간지 16시간째....?? 아니 시발 왜 안일어나 죽은거 아님??")
                                                                    return

                                                                else:
                                                                    await app.send_message(message.channel, '15시간 잤네')
                                                            else:
                                                                await app.send_message(message.channel, '14시간 잤네')
                                                        else:
                                                            await app.send_message(message.channel, '13시간 잤네')
                                                    else:
                                                        await app.send_message(message.channel, '12시간 잤네')
                                                else:
                                                    await app.send_message(message.channel, '11시간 잤네')
                                            else:
                                                await app.send_message(message.channel, '10시간 잤네')
                                        else:
                                            await app.send_message(message.channel, '9시간 잤네')
                                    else:
                                        await app.send_message(message.channel, '8시간 잤네')
                                else:
                                    await app.send_message(message.channel, '7시간 잤네')
                            else:
                                await app.send_message(message.channel, '6시간 잤네')
                        else:
                            await app.send_message(message.channel, '5시간 잤네')
                    else:
                        await app.send_message(message.channel, '4시간 잤네')
                else:
                    await app.send_message(message.channel, '3시간 잤네')
            else:
                await app.send_message(message.channel, '1시간 잤네')
        else:
            await app.send_message(message.channel, 'ㅅㅂ 잔다매')
            
 
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
