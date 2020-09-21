from os import system

try:
    from pyrogram import Client, filters
except ModuleNotFoundError:
    system('pip install pyrogram')

try:
    import gtts
except ModuleNotFoundError:
    system('pip install gtts')

app = Client("my_account", api_id=1582033, api_hash="d8a9ec6ca042b6391baa12d13ded42d2")


@app.on_message(filters.command("s", prefixes="."))
def tts(_, msg):
    if msg.chat.type == 'private' or msg.outgoing:
        msg.delete()
        reply = False
    else:
        reply = True
    text_tos = msg.text.split(".s ", maxsplit=1)[1]
    lng = msg.text[3:5]
    audio_file = str(msg.from_user.username).replace('None', 'Кто-то') + ' сказал - by NIKDISSV.mp3'

    try:
        tts = gtts.gTTS(text=text_tos.replace(lng, ''), lang=lng)
        tts.save(audio_file)
    except ValueError:
        app.send_message(msg.from_user.username,
                         '[Вот](https://ru.m.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2) коды языков, стыдно их не знать!')
    if reply:
        msg.reply_audio(audio_file)
    else:
        app.send_audio(msg.chat.id, audio_file)
    system('rm *.mp3')


app.run()