# Don't Remove Credit Tg - @learnmaterobot

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫  👋! {m.from_user.mention} \n\n ➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 By ♥️ **@irymes** \n\n ➠ 𝐂𝐚𝐧 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐕𝐢𝐝𝐞𝐨𝐬 & 𝐏𝐝𝐟 𝐅𝐫𝐨𝐦 𝐘𝐨𝐮𝐫 𝐓𝐞𝐱𝐭 𝐅𝐢𝐥𝐞 𝐚𝐧𝐝 𝐔𝐩𝐥𝐨𝐚𝐝 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 \n\n ➠ 𝐔𝐬𝐞 /as 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥e..\n\n ➠ 𝐔𝐬𝐞 /stop 𝐓𝐨 𝐬𝐭𝐨𝐩 𝐀𝐧𝐲 𝐎𝐧𝐠𝐨𝐢𝐧𝐠 𝐓𝐚𝐬𝐤 \n\n ➠ 𝐌𝐚𝐝𝐞 𝐁𝐲:- @irymes  </b>")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**🇸🇹🇴🇵🇵🇪🇩**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["as"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('🗣𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞\n\n𝗘𝗴 » `LAKSHYA BANGLA HS (3RD-4TH SEM ) 2026`**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("*📸 𝗘𝗻𝘁𝗲𝗿 𝗥𝗲𝘀𝗼𝗹𝘂𝘁𝗶𝗼𝗻 📸**\n➤ `144`\n➤ `240`\n➤ `360`\n➤ `480`\n➤ `720`\n➤ `1080`")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("📥 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐄𝐃 𝐁𝐘 ➤\n\n𝗘𝗴 » `@irymes`")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg » https://i.ibb.co/T6cnYmm/image.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYwMTAzMTEuNTY2LCJkYXRhIjp7Il9pZCI6IjY0NzFkZmJhZGRkOGJhMDAxODMyNThmMyIsInVzZXJuYW1lIjoiNzY3OTY4NTQ5NyIsImZpcnN0TmFtZSI6IklzaGlkYSIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoiaS5zYWhlYi5yYWhhbWFuQGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTc0NTQwNTUxMX0.qdyYBY7sH3AXkOfnf80MhTqh7NlWMmMkM-W5yl5l_M0'}).json()['url']

            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                pw_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYwMTAzMTEuNTY2LCJkYXRhIjp7Il9pZCI6IjY0NzFkZmJhZGRkOGJhMDAxODMyNThmMyIsInVzZXJuYW1lIjoiNzY3OTY4NTQ5NyIsImZpcnN0TmFtZSI6IklzaGlkYSIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoiaS5zYWhlYi5yYWhhbWFuQGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTc0NTQwNTUxMX0.qdyYBY7sH3AXkOfnf80MhTqh7NlWMmMkM-W5yl5l_M0"
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYwMTAzMTEuNTY2LCJkYXRhIjp7Il9pZCI6IjY0NzFkZmJhZGRkOGJhMDAxODMyNThmMyIsInVzZXJuYW1lIjoiNzY3OTY4NTQ5NyIsImZpcnN0TmFtZSI6IklzaGlkYSIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoiaS5zYWhlYi5yYWhhbWFuQGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTc0NTQwNTUxMX0.qdyYBY7sH3AXkOfnf80MhTqh7NlWMmMkM-W5yl5l_M0"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] Vid_ID:** {str(count).zfill(3)}.** {𝗻𝗮𝗺𝗲𝟭}.mkv \n\n**📚𝐁𝐀𝐓𝐂𝐇 𝗡𝗔𝗠𝗘 ➤**  **{raw_text0}**\n\n📥 𝗘𝗫𝗧𝗥𝗔𝗖𝗧𝗘𝗗 𝗕𝗬 ** ➤**『{raw_text3}』**\n\n━━━━━━━━✦@PRAYAS_WBJEE❤️✦━━━━━━━━'
                cc1 = f'**[📁] Pdf_ID:** {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭} .mkv \n\n**📚𝐁𝐀𝐓𝐂𝐇 𝗡𝗔𝗠𝗘 ➤**  **{raw_text0}**\n\n📥 𝗘𝗫𝗧𝗥𝗔𝗖𝗧𝗘𝗗 𝗕𝗬 ** ➤**『{raw_text3}』**\n\n━━━━━━━━✦@PRAYAS_WBJEE❤️✦━━━━━━━━'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🇩🇴🇼🇳🇱🇴🇦🇩🇮🇳🇬⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**🔰𝐃𝐎𝐍𝐄 ALSO JOIN @PRAYAS_WBJEE**")


bot.run()
