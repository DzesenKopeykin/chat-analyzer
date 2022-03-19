#!/usr/bin/env python
import json
import sys

from pyrogram import Client


def main():
    with Client("chat_analyzer") as app:
        try:
            dialog_filter = lambda d: d.chat.first_name == sys.argv[1]
            dialog = list(filter(dialog_filter, app.get_dialogs()))[0]
        except IndexError:
            raise ValueError("Dialog not found. Pass the contact's first name.")
        print(dialog)

        history_count = app.get_history_count(dialog.chat.id)
        print(history_count)

        sticker_statistics = []
        for message in app.iter_history(dialog.chat.id):
            if message.sticker:
                stat = {
                    "emoji": message.sticker.emoji,
                    "author": message.from_user.first_name,
                }
                sticker_statistics.append(stat)
            print(len(sticker_statistics))

        with open("statistics/sticker_statistics.json", "w") as f:
            json.dump(sticker_statistics, f)


if __name__ == "__main__":
    main()
