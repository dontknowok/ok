
import re
import os
import sys
import asyncio

os.system("pip install pytgcalls==3.0.0.0dev24")
os.system("pip install telethon")

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from pytgcalls import GroupCallFactory

API_ID = 2184829
API_HASH = "6930b92388baabff4cb4a1d377085035"
# SESSION = "1BVtsOKwBu7UJsTIHd5hCSID4xdTOsA2WM84TwFSCHq5u3dU63t5ZDrn6glJYrEojpUCONQ7lB_YR9CvKLm35ICKyK6Tt88e5zoGa7-5_KT_SBqAwvYWQCMLHDNIVBGmRiqAgbHQoeKyczgNuE4d038tw1VtLjI8JBi7fKvHUWunDcKgoRzZUNV9KJ3tDTKQhXfRQVe8hsjDdqGFeWC4ZB9PPShyjXKazeS8KzLw4_Jc1A1_7Kz9LpulC0zfySRfRBQjPZQSNzPvyYhzbPZJX-VsxVVUZaettq-N_PAKy-KBjbm0lnAh44Gya7BJ_Vaqp5boDjFYiUoAl_rkqNj1H-6KpQIaD6h4="
SESSION1 = ""
SESSION2 = ""
SESSION3 = ""
SESSION4 = ""
SESSION5 = ""
SESSION6 = ""
LOGGER = int(-1001547885937)
SUDO = [1212368262, 5645461720, 5450204360, 5323136147, 5742165534]
DEV = [1212368262, 5645461720, 5450204360, 5323136147, 5742165534, 6089929322]

async def main():
    global bot1
    global bot2     
    global bot3  
    global bot4     
    global bot5     
    global bot6     

    if SESSION1:
        bot1 = TelegramClient(session=StringSession(SESSION1), api_id=API_ID, api_hash=API_HASH)
        await bot1.start()
    else:
        bot1 = TelegramClient("CopyVcBlocker1", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot1.start()
        except Exception as e:
            pass

    if SESSION2:
        bot2 = TelegramClient(session=StringSession(SESSION2), api_id=API_ID, api_hash=API_HASH)
        await bot2.start()
    else:
        bot2 = TelegramClient("CopyVcBlocker2", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot2.start()
        except Exception as e:
            pass

    if SESSION3:
        bot3 = TelegramClient(session=StringSession(SESSION3), api_id=API_ID, api_hash=API_HASH)
        await bot3.start()
    else:
        bot3 = TelegramClient("CopyVcBlocker3", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot3.start()
        except Exception as e:
            pass

    if SESSION4:
        bot4 = TelegramClient(session=StringSession(SESSION4), api_id=API_ID, api_hash=API_HASH)
        await bot4.start()
    else:
        bot4 = TelegramClient("CopyVcBlocker4", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot4.start()
        except Exception as e:
            pass

    if SESSION5:
        bot5 = TelegramClient(session=StringSession(SESSION5), api_id=API_ID, api_hash=API_HASH)
        await bot5.start()
    else:
        bot5 = TelegramClient("CopyVcBlocker5", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot5.start()
        except Exception as e:
            pass

    if SESSION6:
        bot6 = TelegramClient(session=StringSession(SESSION6), api_id=API_ID, api_hash=API_HASH)
        await bot6.start()
    else:
        bot6 = TelegramClient("CopyVcBlocker6", api_id=API_ID, api_hash=API_HASH)
        try:
            await bot6.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

group_call_factory1 = GroupCallFactory(bot1, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call1 = group_call_factory1.get_file_group_call('input.raw')

group_call_factory2 = GroupCallFactory(bot2, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call2 = group_call_factory2.get_file_group_call('input.raw')

group_call_factory3 = GroupCallFactory(bot3, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call3 = group_call_factory3.get_file_group_call('input.raw')

group_call_factory4 = GroupCallFactory(bot4, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call4 = group_call_factory4.get_file_group_call('input.raw')

group_call_factory5 = GroupCallFactory(bot2, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call5 = group_call_factory5.get_file_group_call('input.raw')

group_call_factory6 = GroupCallFactory(bot2, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call6 = group_call_factory6.get_file_group_call('input.raw')

permissions = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

approved = []

@group_call1.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot1.send_message(chat_id, 'Successfully joined voice chat #1!')
    else:
        await bot1.send_message(chat_id, 'Disconnected from voice chat #1!')

@group_call2.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot2.send_message(chat_id, 'Successfully joined voice chat #2!')
    else:
        await bot2.send_message(chat_id, 'Disconnected from voice chat #2!')
        
@group_call3.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot3.send_message(chat_id, 'Successfully joined voice chat #3!')
    else:
        await bot3.send_message(chat_id, 'Disconnected from voice chat #3!')

@group_call4.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot4.send_message(chat_id, 'Successfully joined voice chat #4!')
    else:
        await bot4.send_message(chat_id, 'Disconnected from voice chat #4!')

@group_call5.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot5.send_message(chat_id, 'Successfully joined voice chat #5!')
    else:
        await bot5.send_message(chat_id, 'Disconnected from voice chat #5')

@group_call6.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = context.full_chat.id
    if is_connected:
        await bot6.send_message(chat_id, 'Successfully joined voice chat #6!')
    else:
        await bot6.send_message(chat_id, 'Disconnected from voice chat #6!')

@group_call1.on_participant_list_updated
async def participants_are_updated(group_call1, participants):
    chat_id = group_call1.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot1.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot1(EditBannedRequest(chat_id, part, permissions))
                await bot1.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot1.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot1.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")

@group_call2.on_participant_list_updated
async def participants_are_updated(group_call2, participants):
    chat_id = group_call2.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot2.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot2(EditBannedRequest(chat_id, part, permissions))
                await bot2.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot2.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot2.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")

@group_call3.on_participant_list_updated
async def participants_are_updated(group_call3, participants):
    chat_id = group_call3.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot3.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot3(EditBannedRequest(chat_id, part, permissions))
                await bot3.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot3.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot3.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")

@group_call4.on_participant_list_updated
async def participants_are_updated(group_call4, participants):
    chat_id = group_call4.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot4.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot4(EditBannedRequest(chat_id, part, permissions))
                await bot4.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot4.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot4.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")

@group_call5.on_participant_list_updated
async def participants_are_updated(group_call5, participants):
    chat_id = group_call5.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot5.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot5(EditBannedRequest(chat_id, part, permissions))
                await bot5.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot5.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot5.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")

@group_call6.on_participant_list_updated
async def participants_are_updated(group_call6, participants):
    chat_id = group_call6.full_chat.id
    chat_entity = await bot1.get_entity(chat_id)
    chat_name = chat_entity.title
    for participant in participants:
        # partt = participant.peer.channel_id
        part = await bot6.get_peer_id(participant.peer) # Best Code
    check = str(part)
    if not os.path.exists("approved.txt"):
        async with open("approved.txt", "w") as nf:
            pass
    ids = open("approved.txt").readlines()
    ids_lst = [string.strip() for string in ids]
    for id in ids_lst:
        if id not in approved:
            approved.append(id)
    else:
        pass
    if check.startswith("-100"):
        if str(part) not in approved:
            try:
                await bot6(EditBannedRequest(chat_id, part, permissions))
                await bot6.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")
            except Exception as e:
                await bot6.send_message(chat_id, f"/ban {part} CHANNEL FOUND IN VC!")
                await bot6.send_message(LOGGER, f"#BANNED_IN_VOICE_CHAT\n\nChannel ID:- `{part}`\n\nChat Name:- `{str(chat_name)}`\n\nChat ID:- `{chat_id}`\n\nCHANNEL FOUND IN VC!")


@bot1.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj1$'))
async def join_handler1(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj1"):
        if sender_id in SUDO:
            await group_call1.start(e.chat_id)

@bot2.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj2$'))
async def join_handler2(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj2"):
        if sender_id in SUDO:
            await group_call2.start(e.chat_id)

@bot3.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj3$'))
async def join_handler3(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj3"):
        if sender_id in SUDO:
            await group_call3.start(e.chat_id)

@bot4.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj4$'))
async def join_handler4(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj4"):
        if sender_id in SUDO:
            await group_call4.start(e.chat_id)

@bot5.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj5$'))
async def join_handler5(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj5"):
        if sender_id in SUDO:
            await group_call5.start(e.chat_id)

@bot6.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcj6$'))
async def join_handler6(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcj6"):
        if sender_id in SUDO:
            await group_call6.start(e.chat_id)

@bot1.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl1$'))
async def leave_handler1(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl1"):
        if sender_id in DEV:
            await group_call1.stop()

@bot2.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl2$'))
async def leave_handler2(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl2"):
        if sender_id in DEV:
            await group_call2.stop()

@bot3.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl3$'))
async def leave_handler3(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl3"):
        if sender_id in DEV:
            await group_call3.stop()

@bot4.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl4$'))
async def leave_handler4(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl4"):
        if sender_id in DEV:
            await group_call4.stop()

@bot5.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl5$'))
async def leave_handler5(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl5"):
        if sender_id in DEV:
            await group_call5.stop()

@bot6.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcl6$'))
async def leave_handler6(e):
    textt = e.raw_text
    sender_id = e.sender_id
    if textt.startswith("/vcl6"):
        if sender_id in DEV:
            await group_call6.stop()

@bot1.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vca'))
async def approve_handler(e):
    textt = e.raw_text
    text = e.raw_text[5:]
    sender_id = e.sender_id
    if textt.startswith("/vca"):
        if sender_id in DEV:
            ids = open("approved.txt").readlines()
            ids_lst = [string.strip() for string in ids]
            if text not in ids_lst:
                f = open("approved.txt", "a")
                f.write(f"{text}\n")
                f.close()
                await bot1.send_message(e.chat_id, f"`{text}` Approved In Vc Blocker!")
            else:
                await bot1.send_message(e.chat_id, f"`{text}` Already Approved In Vc Blocker!")

@bot1.on(events.NewMessage(outgoing=True, incoming=True, pattern=r'^/vcd'))
async def disapprove_handler(e):
    textt = e.raw_text
    text = e.raw_text[5:]
    sender_id = e.sender_id
    if textt.startswith("/vcd"):
        if sender_id in DEV:
            ids = open("approved.txt").readlines()
            ids_lst = [string.strip() for string in ids]
            if text in ids_lst:
                string = open("approved.txt", "r").read()
                new_string = re.sub(text, '', string)
                open("approved.txt", "w").write(new_string)
                await bot1.send_message(e.chat_id, f"`{text}` Dispproved In Vc Blocker!")
            else:
                await bot1.send_message(e.chat_id, f"`{text}` Already Dispproved In Vc Blocker!")

if len(sys.argv) not in (1, 3, 4):
    try:
        bot1.disconnect()
    except Exception as e:
        pass
    try:
        bot2.disconnect()
    except Exception as e:
        pass
    try:
        bot3.disconnect()
    except Exception as e:
        pass
    try:
        bot4.disconnect()
    except Exception as e:
        pass
    try:
        bot5.disconnect()
    except Exception as e:
        pass
    try:
        bot6.disconnect()
    except Exception as e:
        pass
else:
    try:
        bot1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bot2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bot3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bot4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bot5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bot6.run_until_disconnected()
    except Exception as e:
        pass

