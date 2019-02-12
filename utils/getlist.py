from telethon import TelegramClient, events, sync
from secure import api_id, api_hash


def get_participants_hash(api_id: int, api_hash: str, channel_id: int):
    client = TelegramClient('session_name', api_id, api_hash)
    try:
        client.start()
        return str(client.get_participants(channel_id))
    finally:
        client.disconnect()

def cut_from_hash(find_string_start: str, find_string_end: str, hash: str):
    start_pos = hash.find(find_string_start) + len(find_string_start)
    end_pos = hash.find(find_string_end, start_pos)
    return  hash[start_pos: end_pos].strip("'"), hash[end_pos:]

def get_userlist(hash: str):
    user_list = []
    while True:
        if hash.find("first_name=") == -1:
            break
        # finding first name
        first_name, hash = cut_from_hash("first_name=", ",", hash)
        # finding last name
        last_name, hash = cut_from_hash("last_name=", ",", hash)
        # finding username
        user_name, hash = cut_from_hash("username=", ",", hash)
        user_list.append({'first_name': first_name, 'last_name': last_name, 'user_name': user_name})
    return user_list


if __name__ == '__main__':
    # This found an id of cursor group
    # I commented it to not to load the program
    # client = TelegramClient('session_name', api_id, api_hash)
    # client.start()
    # dialogs = str(client.get_dialogs())
    # dialogs = dialogs[dialogs.find('channel_id='):]
    # cursor_id = int(dialogs[dialogs.find('=') + 1: dialogs.find(')')])
    # print(cursor_id)
    cursor_id = 1392175264
    p_hash = get_participants_hash(api_id, api_hash, cursor_id)
    u_list = get_userlist(p_hash)
