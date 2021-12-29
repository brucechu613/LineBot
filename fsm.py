from transitions.extensions import GraphMachine

from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "intro"

    def on_enter_fsm(self, event):
        print("I'm entering fsm")

        reply_token = event.reply_token
        send_image_url(reply_token, "https://github.com/brucechu613/LineBot/blob/master/img/show-fsm.png?raw=true")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving fsm")

    def on_enter_intro(self, event):
        print("I'm entering intro")

        reply_token = event.reply_token
        send_text_message(reply_token, "1:輸入fsm 可以看到fsm的圖\n2:輸入intro 可以看到英俊的害羞男孩我的使用功能\n3:輸入撩我 英俊的害羞男孩我會反過來讓你害羞")
        self.go_back()

    def on_exit_intro(self):
        print("Leaving intro")
