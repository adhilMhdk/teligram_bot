from telethon import TelegramClient, events, sync
import config
import response
import os

# Remember to use your own values from my.telegram.org!
api_id = config.API_ID
api_hash = config.API_HASH
client = TelegramClient(config.SESSION_NAME, api_id, api_hash)




client.start()

@client.on(events.NewMessage())
async def my_event_handler(event):
    res_ans = response.generateResponse(event.raw_text)
    if res_ans.startswith("$FILE$"):
        await client.send_file(event.message.peer_id.user_id,res_ans.replace("$FILE$",""))
        os.remove(res_ans.replace("$FILE$",""))

    else:
        await event.respond(res_ans)
    print(event.raw_text)

client.run_until_disconnected()