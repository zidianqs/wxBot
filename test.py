#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import thread

# class MyWXBot(WXBot):
#     def handle_msg_all(self, msg):
#         if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
#             self.send_msg_by_uid(u'hi', msg['user']['id'])
#             #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
#             #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
# '''
#     def schedule(self):
#         self.send_msg(u'张三', u'测试')
#         time.sleep(1)
# '''

# 定义Bot
bot = None

class IntelligenceWxBot(WXBot):
    def handle_msg_all(self, msg):
        print msg

def bot_lifecycle():
    bot = IntelligenceWxBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

def ui_lifecycle():
    while True:
        str = raw_input('你想说啥...')
        if bot:
            bot.send_msg(u'严皓亮', str)
        else:
            print bot
            print u'微信还没初始化'


def main():
    try:
        thread.start_new_thread(bot_lifecycle, ())
        thread.start_new_thread(ui_lifecycle, ())
    except Exception, e:
        print 'Error: Unable to start thread'
        print e
    while True:
        pass


if __name__ == '__main__':
    main()
