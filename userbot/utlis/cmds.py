import os

from userbot import CMD_HELP, CMD_HELP_BOT

from userbot.config import Config

HANDLER = Config.HANDLER

# Made this class for help menu

class CmdHelp:

    FILE = ""

    ORIGINAL_FILE = ""

    FILE_AUTHOR = ""

    IS_OFFICIAL = True

    COMMANDS = {}

    PREFIX = HANDLER

    WARNING = ""

    INFO = ""

    EXTRA = {}

    def __init__(self, file: str, official: bool = True, file_name: str = None):

        self.FILE = file

        self.ORIGINAL_FILE = file

        self.IS_OFFICIAL = official

        self.FILE_NAME = file_name if not file_name == None else file + ".py"

        self.COMMANDS = {}

        self.FILE_AUTHOR = ""

        self.WARNING = ""

        self.INFO = ""

        self.EXTRA = {}

    def set_file_info(self, name: str, value: str):

        if name == "name":

            self.FILE = value

        elif name == "author":

            self.FILE_AUTHOR = value

        return self

    def add_command(self, command: str, params=None, usage: str = "", example=None):

        self.COMMANDS[command] = {

            "command": command,

            "params": params,

            "usage": usage,

            "example": example,

        }

        return self

    def add_warning(self, warning):

        self.WARNING = warning

        return self

    def add_info(self, info):

        self.INFO = info

        return self

    def add_extra(self, extra: str, content: str):

        self.EXTRA[extra] = {

            "extra": extra,

            "content": content,

        }

        return self

    def get_result(self):

        result = f"**✅ FILE :**  `{self.FILE}`\n"

        if self.INFO == "":

            if not self.WARNING == "":

                result += f"**⛔ WARNING :**  {self.WARNING}\n\n"

        else:

            if not self.WARNING == "":

                result += f"**⛔WARNING :**  {self.WARNING}\n"

            result += f"**ℹ️ INFO :**  {self.INFO}\n"

        if self.EXTRA:

            for extra in self.EXTRA:

                extra = self.EXTRA[extra]

                result += f"**{extra['extra']} :**  `{extra['content']}`\n"

        result += "\n"

        for command in self.COMMANDS:

            command = self.COMMANDS[command]

            if command["params"] == None:

                result += f"**🛠 COMMAMD :**  `{HANDLER[:1]}{command['command']}`\n"

            else:

                result += f"**🛠 COMMAMD :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"

            if command["example"] == None:

                result += f"**💬 DETAILS :**  `{command['usage']}`\n\n"

            else:

                result += f"**💬 DETAILS :**  `{command['usage']}`\n"

                result += (

                    f"**⌨️ Eg. :**  `{HANDLER[:1]}{command['example']}`\n\n"

                )

        return result

    def add(self):

        CMD_HELP_BOT[self.FILE] = {

            "info": {

                "warning": self.WARNING,

                "info": self.INFO,

            },

            "extra": self.EXTRA,

            "commands": self.COMMANDS,

        }

        CMD_HELP[self.FILE] = self.get_result()

        return True

    def getText(self, text: str):

        if text == "REPLY_OR_USERNAME":

            return "<user name> <user name/answer >"

        elif text == "OR":

            return "or"

        elif text == "USERNAMES":

            return "<user name (s)>"
