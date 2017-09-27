# elotelebot
for telegram

* Installation using pip

```
$ pip install pyTelegramBotAPI
```

**While the API is production-ready, it is still under development and it has regular updates, do not forget to update it regularly by calling `pip install pytelegrambotapi --upgrade`*

### Prerequisites

It is presumed that you [have obtained an API token with @BotFather](https://core.telegram.org/bots#botfather). We will call this token `TOKEN`.
Furthermore, you have basic knowledge of the Python programming language and more importantly [the Telegram Bot API](https://core.telegram.org/bots/api).

The TeleBot class (defined in \__init__.py) encapsulates all API calls in a single class. It provides functions such as `send_xyz` (`send_message`, `send_document` etc.) and several ways to listen for incoming messages.


Then, open the file and create an instance of the TeleBot class.
```python
import telebot

bot = telebot.TeleBot("TOKEN")
```
