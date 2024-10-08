from highrise import BaseBot, __main__, CurrencyItem, Item, Position, AnchorPosition, Reaction, SessionMetadata, User
from highrise.__main__ import BotDefinition
from asyncio import run as arun, sleep
import random


class Bot(BaseBot):

    def __init__(self):
        super().__init__()
        self.bot_id = ""
        self.owner_id = ""
        self.room_name = ""
        self.bot_name = ""
        self.door = Position(x=0, y=0, z=0, facing="FrontRight")
        self.spamming = False

    greetings = ["hello", "hi", "س", "سلام"]

    responses = [
        "💝سلام عزیزم", "سلام 😜", "سلام عزیز دلم 😚", "❤️سلام به شما!",
        "سلام عزیزم خوش اومدی ❤️"
    ]

    hru_responses = [
        "🥰خوب خوبم امیدوارم تو ام خوب و با کلی انرژی مثبت باشی",
        "فداتشم تو خوب باشی منم خوبم 🥰",
        "مرسی عزیز دلم خوبم تو چطوری؟ 😎",
    ]
    goodbye_responses = [
        "❤️خداحافظ، امیدوارم بازم ببینمت دوست عزیز",
        "خداحافظ عزیزم ❤️ زود باز بیا پیشم باشه؟ 🥺",
        "🥺 💔خداحافظ دوست خوبم زود بازم برگرد پیشم دلم واست تنگ میشه "
    ]
    panel_responses = [
        "سلام عزیزم به روم بازی خوش اومدی😍🎲 امیدوارم اینجا سرگرم شی و بهت کلی خوش بگذره🤍برای رقصیدن از دنس 1 تا دنس 55 رو وارد کن 🎮",
    ]
    wyd_responses = [
        "سلامتیت عزیزم شما چه خبر؟ 😚",
        "ای بد نیست میگذره خودت چه خبرا؟ 😉",
        "دسته تبر 😂 خبری نیست از دست شما ها ",
    ]

    wrd_responses = [
        "🤩من یه رباتم و اینجام که اینجارو خوشگل تر کنم  و حواسم به روم باشه ",
        "هیچی عزیزم حواسم به روم و شما گوگولیاس ❤️",
        "کارم محافظت از روم و این که به شما کلی خوش بگذره 😍 ❤️",
    ]
    fal_responses = [
        " یک حرف برایت دارم ولی نقطه چین است😚",
        "سوگند به نامت که تو آرام منی . زیر رگبار زمانه تو فقط یار منی😉",
        "درد دل کن که نماند به دلت دلتنگی . کوه هم در فوران است به آن دلسنگی",
        " من دگر سوی چمن هم سر پروازم نیست . که پر بازم اگر هست دل بازم نیست",
        "موی بشکافی به عیب دیگران . ور بپرسم عیب تو کو؟کوری در آن",
        "هزاران چان ما و بهتر از ما .فدای تو که جانه جانه جانی",
    ]

    tas_responses = [
        "تاس انداختی شد ❤️یک",
        "خلاصه بگم دواومد🌟",
        "سه اومد انقدر حرص نخور 😜",
        "شد😊 چهار",
        "پنج🥺 اومد",
        "👍 شیش اومد",
    ]
    jok_responses = [
        "یارو رفت سیگار فروشی گفت: آقا سیگار برگ داری؟ فروشنده گفت نه . یارو گفت پس دوتا کوبیده بده😚",
        "آبادانیه رو توی جنگ اسیر گرفتن وقتی خواستن شکنجه بدن یارو رو میبستن براش نوار بندری میزاشتن نمیتونست برقصه 😉",
        "چرا مهران مدیری داریم ولی مهران معاون نداریم اصلا چرا شیرکاکائو داریم ولی پلنگ کاکائو نداریم🤣",
        "مغز جالب ترین عضو بدنه همیشه کار میکنه جز سر امتحانااااااااا🤣🤣",
        "می دونین ماهی ها غذاشون رو کجا سرخ می کننتوی آدم تابههه😚 ",
        " اگه هزارتا کتلت درست کنن بازم نفری سه تا میرسه🙄 ",
        "مردم می خندن لپشون چال میوفته.ما می خندیم پرانتز باز میشه😂😂",
        "می دونین ماهی های خواهر همدیگر رو چی صدا می کنن؟آبزی😂😂😁😁",
        "میدونین به یه ملوان سیاه پوست چی میگن کاپیتان بلک🤣",
    ]

    sang_responses = [
        "👍قیچی  ",
        "کاغذ 🙌",
        "سنگ اومد 🌟",
    ]
    bot_responses = [
        "🥰جون دلم؟",
        "😘جانم من و صدا کردی؟",
        "❤️جونم عزیزم کارم داشتی؟",
    ]

    dances = {
        "1": "idle-dance-casual",
        "2": "dance-tiktok8",
        "3": "dance-blackpink",
        "4": "dance-tiktok2",
        "5": "dance-pennywise",
        "6": "dance-russian",
        "7": "dance-shoppingcart",
        "8": "dance-tiktok9",
        "9": "dance-weird",
        "10": "dance-tiktok10",
        "11": "idle-loop-sitfloor",
        "12": "emoji-thumbsup",
        "13": "emote-lust",
        "14": "emoji-cursing",
        "15": "emote-greedy",
        "16": "emoji-flex",
        "17": "emoji-gagging",
        "18": "emoji-celebrate",
        "19": "dance-macarena",
        "20": "emote-no",
        "21": "emote-sad",
        "22": "emote-model",
        "23": "emote-yes",
        "24": "emote-laughing",
        "25": "emote-bow",
        "26": "emote-hello",
        "27": "emote-curtsy",
        "28": "emote-snowball",
        "29": "emote-hot",
        "30": "emote-snowangel",
        "31": "emote-charging",
        "32": "emote-wave",
        "33": "emote-confused",
        "34": "idle-enthusiastic",
        "35": "emote-telekinesis",
        "36": "emote-float",
        "37": "emote-teleporting",
        "38": "emote-swordfight",
        "39": "emote-maniac",
        "40": "emote-energyball",
        "41": "emote-snake",
        "42": "idle_singing",
        "43": "emote-frog",
        "44": "emote-superpose",
        "45": "emote-cute",
        "46": "emote-shy",
        "47": "emote-tired",
        "48": "emoji-angry",
        "49": "emote-pose7",
        "50": "emote-pose8",
        "51": "emote-kiss",
        "52": "emote-pose1",
        "53": "emote-pose3",
        "54": "emote-pose5",
        "55": "emote-cutey"
    }

    async def on_user_join(self, user: User) -> None:
        print(f"{user.username} joined the room")
        await self.highrise.chat(
            f" سلام عزیزم😍🎲  {self.room_name} {user.username} خوش اومدی امیدوارم اینجا سرگرم شی و بهت کلی خوش بگذره🤍 برای رقصیدم از دنس1 تا دنس 55 رو وارد کن🎮"
        )

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} left the room")

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot Connected")
        self.bot_id = session_metadata.user_id
        self.owner_id = session_metadata.room_info.owner_id
        self.room_name = session_metadata.room_info.room_name
        room_users = await self.highrise.get_room_users()
        for user, position in room_users.content:
            if user.id == self.bot_id:
                self.bot_name = user.username
                self.door = position
        try:
            await self.highrise.teleport(
                self.bot_id, Position(self.door.x, self.door.y,
                                      self.door.z - 2))
            await self.highrise.walk_to(
                Position(self.door.x, self.door.y, self.door.z - 2,
                         "FrontLeft"))
        except Exception as e:
            print(f"{e}")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username} said: {message}")

        if message.startswith("dance") or message.startswith("دنس"):
            if message.startswith("dance"):
                language = "english"
            elif message.startswith("دنس"):
                language = "persian"
            await self.perform_dance(user, message, language)
        elif message.strip().lower().startswith("خداحافظ"):
            await self.reply_to_bye(user)
        elif message.strip().lower().startswith("سلام"):
            await self.reply_to_hello(user)
        elif message.strip().lower().startswith("فال"):
            await self.reply_to_fal(user)
        elif message.strip().lower().startswith("سنگ"):
            await self.reply_to_sang(user)
        elif message.strip().lower().startswith("جوک"):
            await self.reply_to_jok(user)
        elif message.strip().lower().startswith("جک"):
            await self.reply_to_jok(user)
        elif message.strip().lower().startswith("تاس"):
            await self.reply_to_tas(user)
        elif message.strip().lower().startswith("خوبی"):
            await self.reply_to_hru(user)
        elif message.strip().lower().startswith("چخبر"):
            await self.reply_to_wyd(user)
        elif message.strip().lower().startswith("پنل"):
            await self.reply_to_panel(user)
        elif message.strip().lower().startswith("چیکار میکنی "):
            await self.reply_to_wrd(user)
        elif message.strip().lower().startswith("بات"):
            await self.reply_to_bot(user)
        elif message.strip().lower().startswith(
                "بیا بات") or message.strip().lower().startswith("follow"):
            if user.id == self.owner_id:
                await self.follow_user(user)
            else:
                privilege_response = await self.highrise.get_room_privilege(
                    user.id)
                if privilege_response.moderator or privilege_response.designer:
                    await self.follow_user(user)
                else:
                    print(
                        "Follow command only accessible to owners/moderators")
                    return
        elif message.strip().lower() == "اسپم" or message.strip().lower(
        ) == "spam":
            if not self.spamming:
                self.spamming = True
                await self.send_spam_messages()
                self.spamming = False
        elif message.strip().lower() == "teleport up" or message.strip().lower(
        ) == "ب":
            await self.teleport(
                user, Position(x=11.5, y=10.25, z=6.5, facing='FrontLeft'))
        elif message.strip().lower() == "teleport down" or message.strip(
        ).lower() == "پ":
            await self.teleport(
                user, Position(x=4.5, y=0.0, z=12.0, facing='FrontLeft'))
        elif message.strip().lower().startswith(
                "teleport to ") or message.strip().lower().startswith(
                    "go to "):
            target_username = message.split("@")[-1].strip()
            await self.teleport_to_user(user, target_username)
        elif any(message.strip().lower().startswith(phrase) for phrase in
                 self.greetings) and self.bot_name.lower() in message.lower():
            await self.reply_to_hello(user)

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered {message}")

    async def on_emote(self, user: User, emote_id: str,
                       receiver: User | None) -> None:
        #print(f"{receiver} emoted: {emote_id}")
        pass

    async def on_reaction(self, user: User, reaction: Reaction,
                          receiver: User) -> None:
        #print(f"{user.username} sent {reaction} -> {receiver.username}")
        pass

    async def on_tip(self, sender: User, receiver: User,
                     tip: CurrencyItem | Item) -> None:
        print(f"{sender.username} tipped {tip} -> {receiver.username}")

    async def on_user_move(self, user: User, pos: Position) -> None:
        pass

    async def perform_dance(self, user: User, message: str, language) -> None:
        try:
            message = message.replace(" ", "")
            if language == "english":
                dance_number = message.split("dance")[-1].strip()
                dance_emote = f"{dance_number}"
                emote_id = self.dances.get(dance_emote)
            if language == "arabi":
                dance_number = message.split("dance")[-1].strip()
                dance_emote = f"{dance_number}"
                emote_id = self.dances.get(dance_emote)
            elif language == "persian":
                dance_number = message.split("دنس")[-1].strip()
                dance_emote = f"{dance_number}"
                emote_id = self.dances.get(dance_emote)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error sending dance: {e}")

    async def reply_to_hello(self, user: User) -> None:
        response = random.choice(self.responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_hru(self, user: User) -> None:
        response = random.choice(self.hru_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_bye(self, user: User) -> None:
        response = random.choice(self.goodbye_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_wrd(self, user: User) -> None:
        response = random.choice(self.wrd_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_panel(self, user: User) -> None:
        response = random.choice(self.panel_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_wyd(self, user: User) -> None:
        response = random.choice(self.wyd_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_fal(self, user: User) -> None:
        response = random.choice(self.fal_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_jok(self, user: User) -> None:
        response = random.choice(self.jok_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_sang(self, user: User) -> None:
        response = random.choice(self.sang_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_tas(self, user: User) -> None:
        response = random.choice(self.tas_responses)
        await self.chat(f"@{user.username} {response}")

    async def reply_to_bot(self, user: User) -> None:
        response = random.choice(self.bot_responses)
        await self.chat(f"@{user.username} {response}")

    async def follow_user(self, user: User) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target_user, position in room_users.content:
                if user.id == target_user.id:
                    if isinstance(position, Position):
                        x, y, z = position.x, position.y, position.z
                        facing = position.facing
                        new_z = z - 1
                        await self.walk(Position(x, y, new_z, facing))
                        break
        except Exception as e:
            print(f"An following error occurred: {e}")

    async def send_spam_messages(self) -> None:
        spam_messages = [
            "سلام عزیزم خوش اومدی به روم بازی🎮",
            "از بازی ها لذت ببرید🤍",
            "به دوستاتون لوک بدید😍🎲",
            "چمن بازه برید بازی کنین بچه ها🐼",
            "تم بازه برید بازی کنید بچه ها😛",
            "بفرما داخل جلو در بده😁",
            "بیا بازی کنو کلی جایزه ببر😎",
            "نظرات شما را میپذیریم",
            "برید پایین بازی بچه ها",
            "بازی کنیم",
            "به ادمین ها احترام بزارید😘",
            "ممولی عشق تیم ما",
        ]

        for _ in range(
                30):  # Adjust the number of spam messages you want to send
            spam_message = random.choice(spam_messages)
            await self.chat(spam_message)
            await sleep(0.4)

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(
                        user,
                        Position(position.x, position.y, new_z,
                                 position.facing))
                    break
        except Exception as e:
            print(
                f"An error occurred while teleporting to {target_username}: {e}"
            )

    async def chat(self, message) -> None:
        try:
            await self.highrise.chat(message)
        except Exception as e:
            print(f"Caught Chat Error: {e}")

    async def whisper(self, user: User, message) -> None:
        try:
            await self.highrise.send_whisper(user.id, message)
        except Exception as e:
            print(f"Caught Whisper Error: {e}")

    async def walk(self, position: Position | AnchorPosition):
        try:
            await self.highrise.walk_to(position)
        except Exception as e:
            print(f"Caught Walking Error: {e}")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def start_bot(self, room_id, token) -> None:
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)


if __name__ == "__main__":
    room_id = "66e1a78f1c516138fc7c3434"
    token = "66b1cd58574aabe73b9ef2109648a2b0b615d895a515cd4735a0c81fd345d736"
    arun(Bot().start_bot(room_id, token))
