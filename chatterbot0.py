# -*- coding: utf-8 -*-

import time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
print(time.strftime('%Y-%m-%d %H:%M:%S'))


# 构建ChatBot并指定
# bot = ChatBot("Training demo")
# bot.set_trainer(ListTrainer)
bot = ChatBot(
    "My ChatterBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[ 'chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter' ],
    preprocessors = [ 'chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.unescape_html' ],
    filters=[ 'chatterbot.filters.RepetitiveResponseFilter' ]
)
bot.set_trainer(ListTrainer)

corpus = open(u"E:/pycharm_project/wx_turing_robot/data/对话聊天记录20170715-20170721test.txt").readlines()
#print(corpus)
corpus_list = []
for i in corpus:
    #print(i.strip('\n'))
    corpus_list.append(i.strip('\n'))
bot.train(corpus_list)
#手动给定一点语料用于训练
# bot.train([
#    '你是谁',
#    '我是bot',
#    '怎么升级',
#    '您问的是否是以下问题，点击或回复序号即可得到对应问题的答案：1.如何添加好友2.如何查询穴位信息3.如何修改密码4.快递费用是如何计算的5.如何注册经销商',
#     '3',
#     '您好，在个人-设置页面点击退出登录按钮，可以退出当前登录账号，点击忘记密码，可以重设密码',
#    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'])

# 手动给定一点语料用于训练
# bot.train([
#    'How can I help you?',
#    'I want to create a chat bot',
#    'Have you read the documentation?',
#    'No, I have not',
#    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'])

# 给定问题并取回结果
# question = 'How do I make an omelette?'
# print(question)
# response = bot.get_response(question)
# print(response)
# print("\n")
# question = 'how to make a chat bot?'
# print(question)
# response = bot.get_response(question)
# print(response)

# test
#print(my_bot.get_response("真喜欢我?"))
print(time.strftime('%Y-%m-%d %H:%M:%S'))
while True:
    #print('输入')
    print(bot.get_response(input(">>>")))