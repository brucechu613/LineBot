from transitions.extensions import GraphMachine
from random import random
from utils import *

s = ""
flirt = ["鐵棒和木棒打你頭哪個痛？", "我真的是太笨了。", "你單身多久了？", "請管好你的嘴。", "我覺得我好花心。", "要是我和你生一個孩子你覺得他會是什座？", "美女，你是什麼座的啊？", "我不要再抱怨生活了。", "你知道你和猴子有什麼區別嗎？", "你一定很孤單吧？"]
flirt_answer = {"":"我愛你","鐵棒和木棒打你頭哪個痛？" : "錯了，是我的心痛。", "我真的是太笨了。" : "除了喜歡你，其它什麼都做不好。", "你單身多久了？" : "對不起，讓你等了這麼久。", "請管好你的嘴。" : "因為我會隨時親你。", "我覺得我好花心。" : "因為你的每個樣子我都喜歡。", "要是我和你生一個孩子你覺得他會是什座？" : "不，我們的傑作", "美女，你是什麼座的啊？" : "我是…我是為你量身定做的。", "我不要再抱怨生活了。" : "我想要擁抱你。", "你知道你和猴子有什麼區別嗎？" : "猴子住在山洞裡，你住在我心裡。", "你一定很孤單吧？" : "因為我的心裡只住著你一個人。"}
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "intro"
    
    def is_going_to_greet(self,event):
        text = event.message.text
        greetlist = ["hi", "Hi", "hello", "Hello", "嗨", "哈囉", "你好", "安安", "安"]
        return text in greetlist
    
    def is_going_to_flirt(self,event):
        text = event.message.text
        return text == "撩我"
    
    def is_going_to_reply_flirt(self,event):
        return True
    
    def on_enter_fsm(self, event):
        print("I'm entering fsm")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://github.com/brucechu613/LineBot/blob/master/img/show-fsm.png?raw=true")
        send_image_url(reply_token, "https://github.com/brucechu613/LineBot/blob/master/img/show-fsm.png?raw=true")
        self.go_back(event)

    def on_exit_fsm(self, event):
        print("Leaving fsm")

    def on_enter_intro(self, event):
        print("I'm entering intro")

        reply_token = event.reply_token
        send_text_message(reply_token, "想必你一定迫不及待的想跟英俊的害羞男孩我聊天吧\n才會如此著急的想知道我有哪些功能\n以下是我帥氣的功能唷\n\n1:輸入fsm 可以看到fsm的圖\n2:輸入intro 可以看到英俊的害羞男孩我的使用功能\n3:輸入撩我 英俊的害羞男孩我會反過來讓你害羞")
        self.go_back(event)

    def on_exit_intro(self, event):
        print("Leaving intro")

    def on_enter_greet(self, event):
        print("I'm entering greet")
        greetlist = ["你好呀美女/帥哥(媚眼","好久不見!!!\n最近過得如何呢小可愛","怎麼了嗎親愛的?\n需要我幫你甚麼嗎(嬌羞"]

        reply_token = event.reply_token
        send_text_message(reply_token, greetlist[int(3*random())])
        self.go_back(event)      
          
    def on_exit_greet(self, event):
        print("Leaving greet")
        
    def on_enter_flirt(self, event):
        print("I'm entering flirt")
        reply_token = event.reply_token
        self.s = flirt[int(len(flirt)*random())]
        send_text_message(reply_token, self.s)

    def on_exit_flirt(self, event):
        print("Leaving flirt")
        
    def on_enter_reply_flirt(self, event):
        print("I'm replying flirt")

        reply_token = event.reply_token
        send_text_message(reply_token, flirt_answer[self.s])
        self.go_back(event)

    def on_exit_reply_flirt(self, event):
        print("Leaving replyflirt")
        
    