# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODEyOTI0MzU1MzM1ODE1MTk4.YDH0zQ.ULMCFcgP5zvBtAE0G2DTI8RYTPM'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '.neko':
        await message.channel.send('にゃーん')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

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

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)