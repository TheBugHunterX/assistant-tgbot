from telegram import ChatMember, ChatMemberUpdated

async def _chat_member_status(chat_member_update: ChatMemberUpdated):
    dif = chat_member_update.difference()
    status = dif.get("status")
    if not status:
        return
    
    user_exist = None
    old_status, new_status = status

    user_exist = False if new_status in [ChatMember.LEFT, ChatMember.BANNED] else True

    return user_exist
