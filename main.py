#!/usr/bin/env python
from pyrogram import Client


def main():
    with Client("hell0") as app:
        app.send_message("me", "Hello from Pyrogram!")


if __name__ == "__main__":
    main()
