# -*- coding: utf-8 -*-
# Edited from script LineVodka script made by Merkremont
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + "感謝加入我為好友")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + "歡迎加入 " + group.name)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param3).displayName + " 活該 被踢\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + " 再見\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                #if "gname:" in msg.text:
#--------------------------------------------------------------
                if msg.text == "kick all":
                    print "ok"
                    _name = msg.text.replace("kick all","")
                    gs = client.getGroup(msg.to)
                    sendMessage(msg.to,"  ▶️血盟骑士团◀ 
       強勢招生中

 ✝全新型翻群家族✝
   ✞等著各路高手✞
 ✟加入我們的行列✟


強制掛名  血盟の

一律無特

請先找幹部，確認可以面接才能進行面接內容
若私自掛名或私自進行擴散的話視為無效

入團條件：
1.擴散招生文*5(五群人數總計300人，每群需50人以上
2.破壞*2

二選一


🚫騷擾（變態滾
🚫玻璃（玻璃滾
🚫潛水（不收水鬼
🚫宣傳  (你他媽宣傳洨？
🚫分享 （滾
🚫翻自家群（你要保證你創的回來
✔999+
✔️18+
✔️夜貓
✔️髒話
✔️圖戰
✔️同盟（同盟可宣
✔️翻群
️
「血盟擁有七大罪七位首領，所有指令由七首領們下達」

✗七首領•領頭✗

團長 http://line.naver.jp/ti/p/~asdf0520
副團 http://line.naver.jp/ti/p/~s20001107
主幹 http://line.naver.jp/ti/p/~orz1320
幹部 http://line.naver.jp/ti/p/~
幹部 http://line.naver.jp/ti/p/~

破壞部隊_隊長 http://line.naver.jp/ti/p/~0905562367
破壞部隊_副隊長 http://line.naver.jp/ti/p/~

加工部門_部長 http://line.naver.jp/ti/p/~06294149
加工部門_副部長 http://line.naver.jp/ti/p/~


")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendText(msg.to,"error")
#-------------------------------------------------------------			
		if msg.text == "測速":
                    start = time.time()
                    sendMessage(msg.to, "速度回報")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------		
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()
