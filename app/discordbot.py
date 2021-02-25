# インストールした discord.py を読み込む
import discord
# 日付の取得
from datetime import datetime

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'あなたのアクセストークン'

# 接続に必要なオブジェクトを生成
client = discord.Client()
# 接続に関するdictの作成
connecttime_dict = {}

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました\n')
#    await greet()

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(696642627914825731)
    await channel.send('おはよう！')

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '.neko':
        await message.channel.send('にゃーん')

    if message.content == '.inu':
        await message.channel.send('わんわん')

# ボイチャに関するイベントハンドラを定義
@client.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None):
        connecttime_dict[member.name] = datetime.now() # 開始時間を記録

    elif(after.channel == None):
        channel = client.get_channel(813327022523678740)
        duration_time = datetime.now() - connecttime_dict[member.name]
        duration_time_second = duration_time.total_seconds()
        duration_time_result = int(duration_time_second)
        msg = member.nick + ' がボイスチャットを中止しました。 通話時間: ' + str(duration_time_result) +'秒'
        await channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
