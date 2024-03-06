from sdk.send_message import send_group_message
from sdk.message import text_message
from core.plugin import Plugin
from typing import List


async def handler(session: str,group_id: int,sender_id: int,message: List[any]):
    if message[0][:4]=="守夜冠军":
        await send_group_message(session,group_id,[text_message("这才几点？")])

stay_up=Plugin('stay_up')
stay_up.register_callback('group.P',handler)