class script(object):
    START_TXT = """๐ท๐ด๐ป๐พ {},
๐ด๐ ๐ต๐จ๐ด๐ฌ , <a href='https://t.me/Dhanush_media_bot'>Dhanush</a>, ๐ฐ๐'๐ ๐ฝ๐๐๐๐ ๐ฌ๐๐๐. ๐ฑ๐๐๐ ๐จ๐๐ ๐ด๐ ๐ป๐ ๐๐๐๐ ๐ฎ๐๐๐๐ ๐จ๐๐ ๐ด๐๐๐ ๐ด๐ ๐จ๐๐๐๐, ๐ป๐๐๐๐ ๐จ๐๐, ๐ฐ'๐ณ๐ณ ๐ท๐๐๐๐๐๐ ๐ด๐ถ๐ฝ๐ฐ๐ฌ๐บ ๐ป๐๐๐๐ ๐ค
๐ฏ๐ฌ๐,<a href='http://t.me/Dhanush_media_Bot?startgroup=true'>๐จ๐๐ ๐ด๐ ๐ป๐ ๐๐๐๐ ๐ฎ๐๐๐๐ ๐จ๐๐ ๐ด๐๐๐ ๐ด๐ ๐จ๐ ๐จ๐๐๐๐ ๐ป๐๐๐๐</a>
โโโโโโโโโโโโโ
ยฉ๏ธMแดษชษดแดแดษชษดแดD Bส: <a href="https://t.me/y2say">Shin shan</a>"""
    HELP_TXT = """๐ท๐ด๐ {}
๐๐ฆ๐ณ๐ฆ ๐๐ด ๐๐ฉ๐ฆ ๐๐ฆ๐ญ๐ฑ ๐๐ฐ๐ณ ๐๐บ ๐๐ฐ๐ฎ๐ฎ๐ข๐ฏ๐ฅ๐ด."""
    ABOUT_TXT = """
โช ๐๐๐ท๐ช๐ถ๐ฎ: <a href="https://t.me/Dhanush_media_Bot"> Dhanush </a>
โช ๐๐ป๐ฎ๐ช๐ฝ๐ธ๐ป: <a href="https://t.me/Veralevelda07"> Naveen </a>
โช ๐๐ฒ๐ซ๐ป๐ฎ๐ช๐ป๐ป๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โช ๐๐ช๐ท๐ฐ๐พ๐ช๐ฐ๐ฎ: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โช ๐๐ช๐ฝ๐ช ๐๐ช๐ผ๐ฎ: ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
โช ๐๐ธ๐ฝ ๐ผ๐ฎ๐ป๐ฟ๐ฎ๐ป: ๐ท๐ด๐๐พ๐บ๐
โช ๐๐พ๐ฒ๐ต๐ญ ๐ข๐ฝ๐ช๐ฝ๐พ๐ผ: v1.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐ฐ ๐๐ ๐๐๐ ๐ ๐๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐๐๐. 
- ๐ท๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐๐

๐ ๐๐ฆ๐ง๐๐ฅ:
<a href="https://t.me/VERALEVELDA07"> NAVEEN </a>  """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Dhanush ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐.
2. ๐ถ๐๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐.
3. ๐จ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐ ๐ ๐๐๐๐๐ ๐๐ 64 ๐๐๐๐๐๐๐๐๐๐.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Dhanush Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Dhanush supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Dhanush_media_Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Dhanush

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โช ๐ป๐๐๐๐ ๐๐๐๐๐: <code>{}</code>
โช ๐ป๐๐๐๐ ๐ผ๐๐๐๐: <code>{}</code>
โช ๐ป๐๐๐๐ ๐ช๐๐๐๐: <code>{}</code>
โช ๐ผ๐๐๐ ๐บ๐๐๐๐๐๐: <code>{}</code> ๐ผ๐๐ฑ
โช ๐ญ๐๐๐ ๐บ๐๐๐๐๐๐: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
