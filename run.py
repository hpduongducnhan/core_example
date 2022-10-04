# -*- coding: utf-8 -*-
import asyncio
import uvloop
uvloop.install()



async def run_loop():
    from core.receiver import MessageReceiver
    from core.schema import CoreChatInputMessage

    receiver = MessageReceiver()
    await receiver.initialize()

    text_message = CoreChatInputMessage(msg_type='text', chat_type='zalo')
    await receiver.process_message(text_message)

    emoji_of_msg = CoreChatInputMessage(msg_type='emoji-on-message', chat_type='zalo')
    await receiver.process_message(emoji_of_msg)

    text_message = CoreChatInputMessage(msg_type='text', chat_type='facebook')
    await receiver.process_message(text_message)
    
    emoji_of_msg = CoreChatInputMessage(msg_type='emoji-on-message', chat_type='facebook')
    await receiver.process_message(emoji_of_msg)

    text_message = CoreChatInputMessage(msg_type='text', chat_type='live_chat')
    await receiver.process_message(text_message)
    
    emoji_of_msg = CoreChatInputMessage(msg_type='emoji-on-message', chat_type='live_chat')
    await receiver.process_message(emoji_of_msg)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_loop())