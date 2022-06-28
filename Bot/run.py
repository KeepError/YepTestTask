#!/usr/bin/env python

import dotenv


def main():
    dotenv.load_dotenv("../.env")

    import bot
    bot.start()


if __name__ == '__main__':
    main()
