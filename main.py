import discord
from keep_alive import keep_alive
import config

client = discord.Client()

chinese_words = { "love" : ["Ài", "爱"], "like doing something" : ["Ài", "爱"], "eight" : ["Bā", "八"], "father" : ["Bàba", "爸爸"], "dad" : ["Bàba", "爸爸"], "cup" : ["Bēizi", "杯子"], "glass" : ["Bēizi", "杯子"], "Beijing" : ["Běijīng","北京"], 
                 "copy" : ["Běn","本"], "issue" : ["Běn","本 (used for counting books and other bound items)"], "you're welcome" : ["Bù kèqì", "不客气"], "no" : ["Bù", "不"], "not" : ["Bù", "不"], "vegetable" : ["Cài", "菜"], "dish" : ["Cài", "菜"], "tea" : ["Chá", "茶"], "eat" : ["Chī", "吃"], "taxi" : ["Chūzūchē", "出租车"]}

@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))
   
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!nihao'):
        await message.channel.send('你好!' + ' You can ask for Chinese Words in Pinying by using "?" or "@" if you want Hanzi. Leave a space after the symbol and choose the word you want to know...')

    word_eng = "hi"

    if message.content.startswith('?'):
      word_eng = message.content.split('? ',1)[1]
      if word_eng in chinese_words:
        await message.channel.send(chinese_words[word_eng][0])
      else:
        await message.channel.send("That word its not in my library")

    if message.content.startswith('@'):
      word_eng = message.content.split('@ ',1)[1]
      if word_eng in chinese_words:
        await message.channel.send(chinese_words[word_eng][1])
      else:
        await message.channel.send("That word its not in my library")   

        
keep_alive()
client.run(config.TOKEN)  

