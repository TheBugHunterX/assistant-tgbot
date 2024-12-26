from bot.modules.database.mongodb import MongoDB
from bot.modules.database.local_database import LOCAL_DATABASE
from bot import (
    bot,
    logger,
    bot_token,
    owner_id,
    owner_username,
    server_url,
    mongodb_uri,
    db_name
)


async def update_database():
    find = await MongoDB.find("bot_docs", "_id")
    _bot_info = await bot.get_me()
    data = {
        "first_name": _bot_info.first_name,
        "full_name": _bot_info.full_name,
        "last_name": _bot_info.last_name,
        "name": _bot_info.name,
        "username": _bot_info.username,
        "id": _bot_info.id,
        "link": _bot_info.link,
        "language_code": _bot_info.language_code,
        "can_join_groups": _bot_info.can_join_groups,
        "can_read_all_group_messages": _bot_info.can_read_all_group_messages,
        "supports_inline_queries": _bot_info.supports_inline_queries
    }
    await LOCAL_DATABASE.insert_data_direct("_bot_info", data)

    if find:
        data = await MongoDB.find_one("bot_docs", "_id", find[0])
        await LOCAL_DATABASE.insert_data_direct("bot_docs", data)
        logger.info("MongoDB database exist! Skiping update...")
        return
    
    data = {
        "bot_token": bot_token,
        "owner_id": int(owner_id),
        "owner_username": owner_username,
        #alive
        "server_url": server_url,
        #database
        "mongodb_uri": mongodb_uri,
        "db_name": db_name
    }

    try:
        await MongoDB.insert_single_data("bot_docs", data)
        await LOCAL_DATABASE.insert_data_direct("bot_docs", data)
        logger.info("Database updated from config.env ...")
        return True
    except Exception as e:
        logger.warning(e)
        return False
