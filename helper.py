# -*- coding: utf-8 -*-
### IMPORT MODUL ###
from BANDIET.linepy import *
from BANDIET.liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
#from LineAPI.main import qr
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
import json, requests
import html5lib
import requests,uvloop
import requests,json,urllib3
from random import randint
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from multiprocessing import Pool, Process
from googletrans import Translator
from bs4.element import Tag
import requests as uReq
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, pafy, youtube_dl, asyncio, timeago, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, subprocess, pyqrcode, humanize, os.path, traceback, atexit, wikipedia
import urllib, urllib3
from gtts import gTTS
from humanfriendly import format_timespan, format_size, format_number, format_length
from subprocess import Popen, PIPE

dietz = LINE('u52c6f63461e40e2ff1a1873f43635055:aWF0OiAxNTUxMzY2NTUwMzc4Cg==..rVKajv10IVi3Ai15WLyCU8BKBmI=',appName='IOS\t8.14.2\tRyn\t11.2.5')##
dietz.log("Auth Token : " + str(dietz.authToken))
dietz1 = LINE('ude761fadfc05145cb83667893f537921:aWF0OiAxNTUyMDQ5MjMwMjA0Cg==..XhJHfPGejP7Bhru23D33o849/Ow=',appName='IOS\t8.14.2\tRyn\t11.2.5')##
dietz1.log("Auth Token : " + str(dietz1.authToken))
print ("\n\
                     ========     \n\
                      ======     \n\
                       ====     \n")
print (" THANKS TO ALLOH SWT ======")
print (" THANKS TO PY3 AND -JK- ======")
print (" KEEP STAY AND RULLES ============")
print ("\n\
            ========   =====     ========      ========    \n\
            ========   =====     ========      ========    \n\
            ========   =====     ========      ========    \n\
            ========     ===     ========     ========     \n\
========    ========             ========  ========        \n\
========    ========             ========     ========     \n\
  ======== ========              ========      ========    \n\
       ========                  ========      ========    \n\
         ====                    ========      ========    \n")
print ("=========== Login Helper Succes ==========")

CSdits = ['u98517e2ccdeb96025ef1019d637a02d4','ub36af1e68f76a6dd51b39e52d208ca80']
admin = ['u98517e2ccdeb96025ef1019d637a02d4','ub36af1e68f76a6dd51b39e52d208ca80']
dietzMID = dietz.profile.mid
mid = dietz.getProfile().mid
mid1 = dietz1.getProfile().mid

sambitan = []

dietzProfile = dietz.getProfile()
dietz1Profile = dietz1.getProfile()

dietzSettings = dietz.getSettings()
dietz1Settings = dietz1.getSettings()
oepoll = OEPoll(dietz)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
botStart = time.time()
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

responsename = dietz.getProfile().displayName
responsename2 = dietz1.getProfile().displayName
myProfile["displayName"] = dietzProfile.displayName
myProfile["statusMessage"] = dietzProfile.statusMessage
myProfile["pictureStatus"] = dietzProfile.pictureStatus

listApp = [
    "IOSIPAD\t8.12.2\tHelloWorld\t8.22.17", 
    "CHROMEOS\t2.1.5\tHelloWorld\t11.2.5", 
    "DESKTOPWIN\t5.9.2\tHelloWorld\t11.2.5", 
    "DESKTOPMAC\t5.9.2\tHelloWorld\t11.2.5", 
    "WIN10\t5.5.5\tHelloWorld\t11.2.5"
]

with open('JKcs.json', 'r') as fp:
    admin = json.load(fp)

### KUMPULAN DEF ##
settings = {
    "modeJAIL": True,
    "wrqr": False,
    "wrinv": False,
    "wrcan": False,
    "wrjon": False,
    "protect": True,
    "qrprotect": False,
    "inviteprotect": False,
    "cancelprotect": False,
    "canceljoin": False,
    "cancelgroup":False,
    "kickjoin": False,
    'autoAdd':True,
    'crotAdd':False,
    'autoblock':False,
    'autoAddblock':False,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoscan": False,
    "autoread": False,
    "ditsticker": False,
    "replytikel": False,
    "mentakolpm1": False,
    "mentakolpm": False,
    "mentakol": False,
    "menpict": True,
    "Bandietrespon": False,
    "detectMention": False,
    "detectMention2": False,
    "detectMention3": False,  
    "detectMentionpc": False,
    "kickMention": False,
    "checkSticker": False,
    "comment":"╔══ஜ°°°Aᴜᴛᴏ°°Lɪᴋᴇ°°°ஜ══╗\n║           🎩^$€^™^β¤t^🎩           \n╚══ஜ°°Oᴘᴇɴ Oʀᴅᴇʀ°°ஜ══╝\n⚖SᴇʟғBᴏᴛ\n⚖Pʀᴏᴛᴇᴄᴛ Bᴏᴛ\n⚖Cᴏɪɴ Lɪɴᴇ Vɪᴀ Gɪғᴛ\n⚖Tʜᴇᴍᴀ\n⚖Vɪᴘ Sᴍᴜʟᴇ\n⚖Sᴀɢᴀʟᴀ Aʏᴀ Wᴇʟᴀʜ\n╔═ஜ°° Cʀᴇᴀᴛᴇᴅ Bʏ °°ஜ══╗\n║  https://line.me/ti/p/~dit2159 \n╚═ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═╝",
    "comment1":"╔══ஜ°°°Aᴜᴛᴏ°°Lɪᴋᴇ°°°ஜ══╗\n║           🎩^$€^™^β¤t^🎩           \n╚══ஜ°°Oᴘᴇɴ Oʀᴅᴇʀ°°ஜ══╝\n⚖SᴇʟғBᴏᴛ\n⚖Pʀᴏᴛᴇᴄᴛ Bᴏᴛ\n⚖Cᴏɪɴ Lɪɴᴇ Vɪᴀ Gɪғᴛ\n⚖Tʜᴇᴍᴀ\n⚖Vɪᴘ Sᴍᴜʟᴇ\n⚖Sᴀɢᴀʟᴀ Aʏᴀ Wᴇʟᴀʜ\n╔═ஜ°° Cʀᴇᴀᴛᴇᴅ Bʏ °°ஜ══╗\n║  https://line.me/ti/p/~dit2159 \n╚═ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═╝",
    "lang":"JP",
    "ghost": False,
    "cscium": False,
    "cstakol": False,
    "blacklist":{},
    "Sider":{},
    "spamtag": {},
    "responcrot":"",
    "responcrot2":"",
    "sidercrot":"",
    "addcrot":"",
    "welcrot":"",
    "leftcrot":"",
    "pmcrot":"",
    "pmcrotakol":"",
    "Bandietresponcrot":"",
    "postEndUrl":{},
    "groupPicture":{},
    "allchangePicture":False,
    "changePicture":False,
    "changePictureProfile": False,
    "wblack":False,
    "dblack":False,
    "wblacklist":False,
    "dblacklist":False,
    "scanblack":False,
    "admincipok":False,
    "adminletak":False,
    "welreplay": False,
    "Sambutan": False,
    "save_sticker": False,
    "update_mention": True,
    "SpamInvite":False,
    "save_mention": " ",
    "pkgid": {},
    "stkid": {},
    "id": {},
    "gid": {},
    'add': {},
    "likeOn": False,
    "joinkick": False,
    "setKey": False,
    "keyCommand": "",
    "nilaiSpam": "1",
    "GroupSpam": {},
    "Unsend": False,
    "checkmid": False,
    "unsend": True,
    "changeProfileVideo": False,
    "autoRespon": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "save_sticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "chatEvent": {},
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "addAudio": {
        "name": "",
        "status": False
    },
    "addImage": {
        "name": "",
        "status": False
    },
    "addSticker": {
        "name": "",
        "status": False
    },
    "addStickertag": {
        "status": False
    },
    "addVideo": {
        "name": "",
        "status": False
    },
    'autoCancel':{"on":False,"members":50},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }

}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restartBot():
    backupData()
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    dietz.log("TERJADI ERROR : " + str(text))
    time_ = datetime.now()
    with open("error.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        dietz.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def DESKTOPMAC():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPMAC\t5.9.2\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def DESKTOPWIN():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPWIN\t5.10.0\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def IOSIPAD():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "IOSIPAD\t8.12.2\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def CHROMEOS():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "CHROMEOS\t2.1.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def WIN10():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "WIN10\t5.5.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def ANDROID():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "ANDROID\t8.12.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def mentionMember1(to, mid):
    try:
        arrData = ""
        textx = "╔═ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═╗\n╠[1.]❂"
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠[%i.]❂ " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(dietz.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        dietz.sendMessage(to, textx+"╚═ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═╝", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        dietz.sendMessage(to,"Total Mention:\n [{}] Members".format(str(len(mid))))
    except Exception as error:
        logError(error)  
  
def token(to,nametoken,msg_id,sender):
    try:
        a = nametoken
        a.update({'x-lpqs' : '/api/v4/TalkService.do'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        qr = clienttoken.getAuthQrcode(keepLoggedIn=1, systemName='AditmadzsToken')
        link = "line://au/q/" + qr.verifier
        dietz.sendReplyMessage(msg_id, to, "Click This Link Only For 2 Minute :)\n\n{}".format(link))
        a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
        json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
        a.update({'x-lpqs' : '/api/v4p/rs'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        req = LoginRequest()
        req.type = 1
        req.verifier = qr.verifier
        req.e2eeVersion = 1
        res = clienttoken.loginZ(req)
        try:
            token = res.authToken
            contact = dietz.getContact(sender)
            dietz.sendMessage(sender, "Nama : {}\nMid : {}\nTOKEN : {}\n\nCreator".format(contact.displayName,contact.mid,token))
            dietz.sendContact(sender, dietzMID)
        except Exception as e:
            dietz.sendMessage(to, str(e))
    except Exception as error:
        dietz.sendMessage(to, "Login Success")

def searchRecentMessages(to,id):
    for a in dietz.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost        
        
def sendTextTemplateDIT(to, text):
    data = {
            "type": "flex",
            "altText": "°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
      "header": {
        "backgroundColor": "#0000FF"
        }
      },  
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "xs",
                "margin": "none",
                "color": "#FFD700",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    dietz.postTemplate(to, data)

def lineBot(op):
    try:
        if op.type == 0:
            print ("DONE")
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                dietz.sendText(op.param1, "╔════❂[♚♚♛♚♚]══════\n╠°❂ Hᴀii... {} \n╠°❂Tʜᴀɴᴋs Fᴏʀ Aᴅᴅ Mᴇ !!\n╚❂[══\n╔❂[══\n╠°❂°Suᴘᴘᴏʀᴛ Bʏ:\n╠══ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═══\n╠═°❂°\n╚══ஜ°°Oᴘᴇɴ Oʀᴅᴇʀ°°ஜ═════\n⚖SᴇʟғBᴏᴛ\n⚖Pʀᴏᴛᴇᴄᴛ Bᴏᴛ\n⚖Cᴏɪɴ Lɪɴᴇ Vɪᴀ Gɪғᴛ\n⚖Tʜᴇᴍᴀ\n⚖Vɪᴘ Sᴍᴜʟᴇ\n⚖Sᴀɢᴀʟᴀ Aʏᴀ Wᴇʟᴀʜ\n╔═ஜ°° Cʀᴇᴀᴛᴇᴅ Bʏ °°ஜ═════\n║  https://line.me/ti/p/~dit2159 \n╚═ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ════".format(str(dietz.getContact(op.param1).displayName)))

        if op.type == 13:
          if dietzMID in op.param3:
            group = dietz.getGroup(op.param1)
            contact = dietz.getContact(op.param2)
            dietz.acceptGroupInvitation(op.param1)
            sendTextTemplateDIT(op.param1,"╔════❂[♚♚♛♚♚]══════\n╠⚖ Hᴇʟʟᴏ...  \n╠°❂[ " + dietz.getContact(op.param2).displayName + " ]\n╠⚖ Tʜᴀɴᴋs Fᴏʀ Iɴviᴛᴇ Mᴇ Tᴏ Gʀᴜᴘ...\n╠°❂ " + str(group.name) + " " + "\n╚════❂[♚♚♛♚♚]══════\n╔❂[══\n╠°❂°Suᴘᴘᴏʀᴛ Bʏ:\n╠══ஜ°°Sᴜɴᴅᴀɴis Eᴅᴀɴ°°ஜ═══\n╚❂[ https://line.me/ti/p/~dit2159 ]❂═")
            data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/B4mMt6T/1548341661798.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dit2159",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {  
            "type": "text",
            "text": " ╔══ஜ══°° L.ᴬ®d!et™ °°══ஜ══╗",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "xs"
          },
          {
            "text": "ʙᴏᴛ ᴅᴇғ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {  
            "type": "text",
            "text": " ═ °Sᴜɴᴅᴀɴis Eᴅᴀɴ° ═",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "lg"
           },
           {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° 5 вσтs",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° 7 вσтs",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° 10 вσтs",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° 15 вσтs",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xxl",
                    "type": "icon",
                    "url":"https://i.ibb.co/xX2Zzdd/IMG-20181220-204012.jpg"
                  },
                  {
                    "text": " ☜❂ Kepoin Aja Sok Lah__",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
            },
            {
            "type": "separator",
            "color": "#FFFFFF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°°My°Acount°°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°Oᴘᴇɴ Oʀᴅᴇʀ°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/41vKc4x/1548340163416.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dit2159",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {  
            "type": "text",
            "text": " ╔══ஜ══°° L.ᴬ®d!et™ °°══ஜ══╗",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "xs"
          },
          {
            "text": "sᴇʟғ ʙᴏᴛ ᴛʜᴇ ᴘᴇᴏᴘʟᴇ",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {  
            "type": "text",
            "text": " ═ °Sᴜɴᴅᴀɴis Eᴅᴀɴ° ═",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "lg"
           },
           {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/B4mMt6T/1548341661798.jpg"
                  },
                  {
                    "text": " °❂° sᴇʟғʙᴏᴛ ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/B4mMt6T/1548341661798.jpg"
                  },
                  {
                    "text": " °❂° sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/B4mMt6T/1548341661798.jpg"
                  },
                  {
                    "text": " °❂° sᴇʟғʙᴏᴛ 3-10 ᴀsɪsᴛ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/B4mMt6T/1548341661798.jpg"
                  },
                  {
                    "text": " °❂° sᴇʟғʙᴏᴛ ᴀsɪsᴛ + ᴀ.ɢs",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xxl",
                    "type": "icon",
                    "url":"https://i.ibb.co/xX2Zzdd/IMG-20181220-204012.jpg"
                  },
                  {
                    "text": " ☜❂ Kepoin Aja Sok Lah__",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
            },
            {
            "type": "separator",
            "color": "#FFFFFF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°°My°Acount°°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°Oᴘᴇɴ Oʀᴅᴇʀ°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/B4mMt6T/1548341661798.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dit2159",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {  
            "type": "text",
            "text": " ╔══ஜ══°° L.ᴬ®d!et™ °°══ஜ══╗",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "xs"
          },
          {
            "text": "ᴘᴇᴍᴀsᴀɴɢᴀɴ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {  
            "type": "text",
            "text": " ═ °Sᴜɴᴅᴀɴis Eᴅᴀɴ° ═",
            "wrap": True,
            "align": "center",
            "weight": "bold",
            "color": "#00FF00",
            "size": "lg"
           },
           {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° sᴍᴜʟᴇ ʀᴏᴏᴍ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° ᴇᴠᴇɴᴛ sᴍᴜʟᴇ ʀᴏᴏᴍ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° ᴄʜᴀᴛᴛɪɴɢ ʀᴏᴏᴍ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/41vKc4x/1548340163416.jpg"
                  },
                  {
                    "text": " °❂° ʀᴏᴏᴍ ɴᴀᴏɴ Wᴇʟᴀʜ",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xxl",
                    "type": "icon",
                    "url":"https://i.ibb.co/xX2Zzdd/IMG-20181220-204012.jpg"
                  },
                  {
                    "text": " ☜❂ Kᴇᴘᴏiɴ ᴀjᴀ Wᴇʟᴀʜ __",
                    "color": "#00FFFF",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
            },
            {
            "type": "separator",
            "color": "#FFFFFF"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°°My°Acount°°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "°❂°Oᴘᴇɴ Oʀᴅᴇʀ°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

            dietz.postFlex(op.param1, data)
        if op.type == 17:
            if op.param1 in sambitan:
                if op.param2 in dietzMID:
                    return
                ginfo = dietz.getGroup(op.param1)
                contact = dietz.getContact(op.param2)
                dit = settings["welcrot"]
                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                sendTextTemplateDIT(op.param1,"╔════❂[♚♚♛♚♚]════°❂°\n╠⚖    Wɪʟᴜjᴇᴜɴɢ Sᴜᴍᴘɪɴɢ     \n╚════❂[♚♚♛♚♚]════°❂°")
                dietz.sendImageWithURL(op.param1,path) 
                sendTextTemplateDIT(op.param1,"╔════❂[♚♚♛♚♚]════°❂°\n╠⚖ Hᴇʟʟᴏ...\n╠°❂° " + dietz.getContact(op.param2).displayName + "\n╠⚖ Wᴇʟᴄᴏᴍᴇ Tᴏ...\n╠❂➤ " + str(ginfo.name) + " " + "\n╠°❂° " + dit + "\n╚════❂[♚♚♛♚♚]═════°❂°")
#-------------------------------------------------------------------------------
        if op.type == 15:
            if op.param1 in sambitan:
                if op.param2 in admin:
                    return
                ginfo = dietz.getGroup(op.param1)
                contact = dietz.getContact(op.param2)
                dit = settings["leftcrot"]
                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                sendTextTemplateDIT(op.param1,"╔════❂[♚♚♛♚♚]════°❂°\n╠⚖    Wɪʟᴜjᴇᴜɴɢ Mᴜʟɪʜʜ.     \n╚════❂[♚♚♛♚♚]════°❂°")
                dietz.sendImageWithURL(op.param1,path)
                sendTextTemplateDIT(op.param1,"╔════❂[♚♚♛♚♚]════°❂°\n╠⚖ Gᴏᴏᴅ Bʏᴇ...\n╠°❂° " + dietz.getContact(op.param2).displayName + "\n╠⚖ Sᴇᴇ You Nᴇxᴛ Tɪᴍᴇ Tᴏ..\n╠°❂° " + str(ginfo.name) + " " + "\n╠❂" + dit + "\n╚════❂[♚♚♛♚♚]═════°❂°")
        if op.type == 24:
            print ("INFO SELBOT : LEAVE ROOM")
        if op.type in [25, 26]:
            msg = op.message
            text = msg.text
            to = msg.to
            msg_id = msg.id
            msg.from_ = msg._from
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "token list":
                                lists = {"result": [{"name": "Token Chrome",},{"name": "Token Iospad",},{"name": "Token Win10",},{"name": "Token Desktopmac",}]}
                                if lists["result"] != []:
                                        ret_ = []
                                        for fn in lists["result"]:
                                                if len(ret_) >= 20:
                                                    pass
                                                else:
                                                    ret_.append({
                                                            "title": "{}".format(fn["name"]),	
                                                            "text": "Click This Button For Get Your Token",
                                                         #   "size": "xl",
                                                        #    "weight": "bold",
                                                            "actions": [
                                                                {
                                                                    "type": "uri",
                                                                    "label": "Click Here.",
                                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("{}".format(fn["name"])))
                                                                }
                                                            ]
                                                        }
                                                    )
                                        k = len(ret_)//10
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Token°L.ᴬ®d!et™_________•",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            dietz.postTemplate(to, data)
                if msg.text.lower().startswith(".helptube"):
                          if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#ffffff"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#ffffff",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#1C1C1C",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#000000"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#000000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "-Youtube°L.ᴬ®d!et™_________•",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    dietz.postTemplate(to, data)
                if msg.text.lower().startswith(".helpmusic "):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                f = str(b["lyric"])
                                g = str(b["image"])
                                hasil = "\n╠°❂° Penyanyi: "+str(d)
                                hasil += "\n╠°❂° Judul : "+str(c)
                                hasil += "\n╠°❂° Lyric : \n╠\n╚══°°L.ᴬ®d!et™°°══╝\n\n" +str(f)
                                data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xxl",
                    "type": "icon",
                    "url":"https://i.ibb.co/xX2Zzdd/IMG-20181220-204012.jpg"
                  },
                  {
                    "text": "\n°❂°「 Musical Info 」°❂°\n\n╔══°°L.ᴬ®d!et™°°══╗\n╠"+str(hasil)+"\n╠°❂°Suᴘᴘᴏʀᴛ Bʏ:\n╚══°Sᴜɴᴅᴀɴis Eᴅᴀɴ°══╝",
                    "size": "xs",
                    "margin": "none",
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "°❂° Happy Listening's !",
            "size": "xs",
            "align": "end",
            "color": "#FFFFFF",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "       °❂°°My°Acount°°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
              },
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " °❂°Oᴘᴇɴ Oʀᴅᴇʀ°❂°",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~dit2159"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                dietz.postFlex(to, data)
                                dietz.sendAudioWithURL(to, e)
                            except Exception as error:
                                dietz.sendMessage(to, "?? error\n?? " + str(error))
                                logError(error)
                if msg.text.lower().startswith(".helpsong"):
                            if msg._from in admin:
                                try:
                                            sep = msg.text.split(" ")
                                            query = msg.text.replace(sep[0] + " ","")
                                            r = requests.get("http://ryns-api.herokuapp.com/joox?q={}".format(query))
                                            data = r.text
                                            data = json.loads(data)
                                            data = data["result"]
                                            jmlh = len(data)

                                            datalagu = []

                                            if jmlh > 10 :
                                              jmlh = 10
                                            else:
                                              pass

                                            for x in range(0,jmlh):
                                                item= {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "{}".format(data[x]["img"]),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "{}".format(data[x]["img"])
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(data[x]["title"]),
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Artist :",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 2
              },
              {
                "type": "text",
                "text": "{}".format(data[x]["artis"]),
                "wrap": True,
                "color": "#B22222",
                "size": "sm",
                "flex": 3
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Preview",
              "uri": "{}".format(data[x]["url"]),
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Download",
              "uri": "{}".format(data[x]["url"]),
            }
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "°❂ᴄʀᴇᴀᴛᴇᴅ❂°",
            "size": "xs",
            "color": "#B22222",
            "flex": 0
          },
          {
            "type": "text",
            "text": "By : °L.ᴬ®d!et™•",
            "color": "#B22222",
            "size": "xs",
            "align": "end"
          }
        ]
      }
    ]
  }
}
                                                datalagu.append(item)


                                            data1 = {  
                                        "type": "flex",
                                        "altText": "°L.ᴬ®d!et™• Music For {}".format(str(query)),
                                        "contents": {
  "type": "carousel",
  "contents":datalagu }}
                                            dietz.postTemplate(to,data1)
                                            search_url="https://www.youtube.com/results?search_query="
                                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                            sb_url = search_url + query
                                            sb_get = requests.get(sb_url, headers = mozhdr)
                                            soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                            yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                            x = (yt_links[1])
                                            yt_href =  x.get("href")
                                            yt_href = yt_href.replace("watch?v=", "")
                                            qx = "https://youtu.be" + str(yt_href)
                                            vid = pafy.new(qx)
                                            stream = vid.streams
                                            best = vid.getbest()
                                            best.resolution, best.extension
                                            xd = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(query))))
                                            data = xd.text
                                            data = json.loads(data)
                                            b = data
                                            c = str(b["title"])
                                            d = str(b["singer"])
                                            e = str(b["url"])
                                            f = str(b["lyric"])
                                            g = str(b["image"])
                                            me = best.url
                                            hasil = ""
                                            hasil += "\n°❂「 Happy Listening! 」❂°\n╔══°°L.ᴬ®d!et™°°══╗\n╠\n╠°❂° Penyanyi: "+str(d)
                                            hasil += "\n╠°❂° Judul : "+str(c)
                                            hasil += "\n╠°❂° Lyric : \n╠\n╚══°°L.ᴬ®d!et™°°══╝\n\n" +str(f)
                                            dietz.sendVideoWithURL(msg.to, me)
                                            dietz.sendAudioWithURL(to, e)
                                            sendTextTemplateDIT(msg.to, hasil)
                                except: 
                                    pass
                elif msg.text.lower().startswith(".helpbcg: "):
                          if msg._from in admin:
                            try:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                contact = dietz.getContact(msg._from)
                                cName = contact.displayName
                                group = dietz.getGroup(msg.to)
                                dot = "\n°°Succes Broadcast\n╔════════════\n╠°\n╠°❂° Froom By Group.\n╠°❂° ❂☞ {}  ".format(str(group.name))
                                dot += "\n╠°❂° Created Brodcast By.\n╠°❂° ❂☞ {} ".format(str(cName))
                                dot += "\n╠°❂° At The Date Off : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠°❂° On The Clock [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                saya = dietz.getGroupIdsJoined()
                                for group in saya:
                                    dit = ""
                                    dit += "\n" + str(dot) + "\n╠°\n╚══ஜ° L.ᴬ®d!et™ °ஜ══"
                                    data = {
                                        "type": "flex",
                                        "altText": "°L.ᴬ®d!et™_________•",
                                        "contents": {
  "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#2F4F4F"
        },
        "header": {
          "backgroundColor": "#2F4F4F"
      }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://i.ibb.co/xX2Zzdd/IMG-20181220-204012.jpg",
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "text": " °Sᴜɴᴅᴀɴis Eᴅᴀɴ°\n           ʙᴏᴛ°™\n\n  「°Broadcast°」",
            "size": "sm",
            "color": "#00FF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "❂☞ My Text : ________________________\n\n"+str(pesan),
                "size": "lg",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": ""+str(dit),
                "size": "sm",
                "margin": "none",
                "color": "#FFD700",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],                                     
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "    ❂☞ Cʟick Hᴇrᴇ My Creator ☜❂",
                "size": "md",
                "weight": "bold",
                "action": {
                  "uri": "http://line.me/ti/p/~dit2159",
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFFFFF",
                "weight": "bold",
                "type": "text"
              } 
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                    dietz.postTemplate(group, data)
                            except Exception as e:
                                pass
                elif text.lower() == '.helpglist':
                    if msg._from in admin:
                        groups = dietz.groups
                        ret_ = "°❂°[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = dietz.getGroup(gid)
                            ret_ += "╠°❂° {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n°❂°[ Total {} Groups ]".format(str(len(groups)))
                        sendTextTemplateDIT(msg.to, ret_)                   
                elif text.lower() == "help":
                                with open("help.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"])),
                                                        "color": "#00FF00"
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",
                                                "altText": "Help°L.ᴬ®d!et™_________•",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                            }
                                        dietz.postTemplate(to, data)
                                        
                elif msg.text.lower().startswith(".helpimg "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                                data = url.json()
                                dietz.sendImageWithURL(to, data["url"])                        
                elif text.lower() == ".ctoken primary":
                    if msg._from in admin:
                        dietz.sendReplyMessage(msg.id, to, " ┏━━━━━━━━━━━°❂°\n ❂ Below This Primary Token Account.")
                        dietz.sendContact(msg.to, mid1)
                elif text.lower() == 'help menu':
                    sendTextTemplateDIT(msg.to, "╔❂[ °Sᴜɴᴅᴀɴis Eᴅᴀɴ° ]❂══\n╠°\n╚═『 Helpers V.X6 』═══\n╠\n╠°❂° .helper restart\n╠°❂° .errorlog \n╠°❂° .helper runtime \n╠°❂° .dellpro \n╠°❂° .dellscreen\n╠°❂° .screen -ls\n╠°❂° .data user\n╠°❂° .procl login\n╠°❂° .login sb\n╠°❂° .login sb1js\n╠°❂° .login 5as1js\n╠°❂° .screenbotcl [ ]\n╠°❂° .screensb [ ]\n╠°❂° .screensb1js [ ]\n╠°❂° .screen5as1js [ ]\n╠°❂° .list costum [ ]\n╠°❂° .addcostum @\n╠°❂° .delcostum @\n╠°❂° .ctoken primary\n╠°\n╠══❂[ For Public ]❂══\n╠°❂° .img [ Search ]\n╠°❂° .heltube [ Search ]\n╠°\n╠°❂° token chrome\n╠°❂° token iospad\n╠°❂° token win10\n╠°❂° token desktopmac\n╠\n╚══❂[ Sein_JK™ ]❂══")
### BOT MENU COMMAND ###
                elif text.lower() == '.helper restart':
                    if msg.from_ in admin:
                        dietz.sendReplyMessage(msg.id, to, "Waiting...")
                        time.sleep(5)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Bot On Again And Please Click [ Help ].")
                        restartBot()
                elif text.lower() == '.errorlog':
                    if msg.from_ in admin:
                        with open('error.txt', 'r') as er:
                            error = er.read()
                        dietz.sendMessage(to, str(error))          
                elif text.lower() == '.helper runtime':
                    if msg.from_ in admin:
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂" "{}".format(str(runtime)))
#---------------------------------------------------user wawan
                elif ".delpro " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.delpro ','')
                        os.system('screen -S {} -X quit'.format(userx))
                        os.system('rm -rf clone/{}'.format(userx))
                        time.sleep(2)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Delete data Costumer succes.")
                  
                elif ".delscreen " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.delscreen ','')
                        os.system('screen -S {} -X quit'.format(userx))
                        os.system('rm -rf clone/{}'.format(userx))
                        time.sleep(2)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Delete data Costumer succes.")
                
                elif text.lower() == '.screen -ls':
                    if msg.from_ in admin:
                        process = os.popen('screen -list')
                        a = process.read()
                        dietz.sendReplyMessage(msg.id, to, "{}".format(a))
                        process.close()
                elif text.lower() == '.data user':
                    if msg.from_ in admin:
                        process = os.popen('cd clone && ls')
                        a = process.read()
                        a += "\n── Data All Costumer ──\n ┗━━━━━━━━━━━°❂°"
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n── Data Screen Helper ──\n\n"+str(a))
                        process.close()
#-------------------------------------------------
                elif text.lower() == ".procl login":
                    if msg.from_ in admin:
                        sendTextTemplateDIT(msg.to, ' ┏━━━━━━━━━━━°❂°\n ❂ login protect\n\nWaitting..........')
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, '{}'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif ".screenbotcl " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.screenbotcl ','')
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg.from_)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        tkn = req.text
                        os.system('cp -r utama clone/{}'.format(userx))
                        os.system('cd clone/{} && echo -n "{} \c" > token.txt'.format(userx, tkn))
                        os.system('screen -dmS {}'.format(userx))
                        os.system('screen -r {} -X stuff "cd clone/{} && python3 batt.py \n"'.format(userx, userx))
                        time.sleep(3)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Succes Login New Costumer\nSetelah Login klik [ rs && sname]")
                        
                elif text.lower() == ".login sb":
                    if msg.from_ in admin:
                        sendTextTemplateDIT(msg.to, ' ┏━━━━━━━━━━━°❂°\n\n ❂ Waitting Login Selfbot.\n ❂ Please You Click Fass Link Here...\n ❂ Setelah Succes Login SEGERA Ketik! \n ❂☞               [ DONE ]')
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, '{}'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)
                
                elif ".screensb " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.screensb ','')
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg.from_)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        tkn = req.text
                        os.system('cp -r onlysb clone/{}'.format(userx))
                        os.system('cd clone/{} && echo -n "{} \c" > token.txt'.format(userx, tkn))
                        os.system('screen -dmS {}'.format(userx))
                        os.system('screen -r {} -X stuff "cd clone/{} && python3 sb.py \n"'.format(userx, userx))
                        time.sleep(3)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Succes Login New Costumer\n ❂ Setelah Login Klick ❂☞ [ .sp Or .help ]")
                
                elif text.lower() == ".login sbx":
                    if msg.from_ in admin:
                        sendTextTemplateDIT(msg.to, ' ┏━━━━━━━━━━━°❂°\n\n ❂ Waitting Login Selfbot.\n ❂ Please You Click Fass Link Here...\n ❂ Setelah Succes Login SEGERA Ketik! \n ❂☞               [ DONE ]')
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, '{}'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)
                
                elif ".screensbx " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.screensbx ','')
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg.from_)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        tkn = req.text
                        os.system('cp -r onlysb clone/{}'.format(userx))
                        os.system('cd clone/{} && echo -n "{} \c" > token.txt'.format(userx, tkn))
                        os.system('screen -dmS {}'.format(userx))
                        os.system('screen -r {} -X stuff "cd clone/{} && python3 sbx.py \n"'.format(userx, userx))
                        time.sleep(3)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Succes Login New Costumer\n ❂ Setelah Login Klick ❂☞ [ .sp Or .help ]")
                        
                
                elif text.lower() == ".login sb1js":
                    if msg.from_ in admin:
                        sendTextTemplateDIT(msg.to, ' ┏━━━━━━━━━━━°❂°\n\n ❂ Waitting Login Selfbot+1js.\n ❂ Please You Click Fass Link Here...\n ❂ Setelah Succes Login SEGERA Ketik! \n ❂☞               [ DONE ]')
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, '{}'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)
                
                elif ".screensb1js " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.screensb1js ','')
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg.from_)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        tkn = req.text
                        os.system('cp -r onlysb clone/{}'.format(userx))
                        os.system('cd clone/{} && echo -n "{} \c" > token.txt'.format(userx, tkn))
                        os.system('screen -dmS {}'.format(userx))
                        os.system('screen -r {} -X stuff "cd clone/{} && python3 sbspam.py \n"'.format(userx, userx))
                        time.sleep(3)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Succes Login New Costumer\n ❂ Setelah Login Klick ❂☞[ .sp Or .me ]")
                
                elif text.lower() == ".login 5as1js":
                    if msg.from_ in admin:
                        sendTextTemplateDIT(msg.to, ' ┏━━━━━━━━━━━°❂°\n\n ❂ Waitting Login Sb 5asist+js.\n ❂ Please You Click Fass Link Here...\n ❂ Setelah Succes Login SEGERA Ketik! \n ❂☞               [ DONE ]')
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, '{}'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)
                
                elif ".screen5as1js " in msg.text:
                    if msg.from_ in admin:
                        userx = msg.text.replace('.screen5as1js ','')
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg.from_)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        tkn = req.text
                        os.system('cp -r asist clone/{}'.format(userx))
                        os.system('cd clone/{} && echo -n "{} \c" > token.txt'.format(userx, tkn))
                        os.system('screen -dmS {}'.format(userx))
                        os.system('screen -r {} -X stuff "cd clone/{} && python3 asist.py \n"'.format(userx, userx))
                        time.sleep(3)
                        sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Succes Login New Costumer\n ❂ Setelah Login Klick ❂☞[ .sp Or .me ]")

                
#============SC AMBIL TOKEN==========
                elif text.lower() == 'token chrome':
                        req = requests.get('https://api.eater.pw/token?header=CHROMEOS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Chrome Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'chrome done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))

                elif text.lower() == 'token iospad':
                        req = requests.get('https://api.eater.pw/token?header=IOSIPAD')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Iospad Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'iospad done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))

                elif text.lower() == 'token win10':
                        req = requests.get('https://api.eater.pw/token?header=WIN10')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Win10 Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'win10 done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))

                elif text.lower() == 'token desktopmac':
                        req = requests.get('https://api.eater.pw/token?header=DESKTOPMAC')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Desktopmac Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'desktopmac done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))
                        
                elif text.lower() == 'token desktopwin':
                        req = requests.get('https://api.eater.pw/token?header=DESKTOPWIN')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Desktopwin Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'desktopwin done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))        
                        
                elif text.lower() == 'token clovafriends':
                        req = requests.get('https://api.eater.pw/token?header=CLOVAFRIENDS')
                        a = req.text
                        b = json.loads(a)
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        tkn['{}'.format(msg.from_)] = []
                        tkn['{}'.format(msg.from_)].append({
                            'qr': b['result'][0]['linkqr'],
                            'tkn': b['result'][0]['linktkn']
                            })
                        qrz = b['result'][0]['linkqr']
                        dietz.sendMessage(to, 'Klik link dibawah ini:\n\n{}\n\nKetik "Clovafriends Done" jika sudah selesai!'.format(qrz))
                        with open('tkn.json', 'w') as outfile:
                            json.dump(tkn, outfile)

                elif text.lower() == 'clovafriends done':
                        tknop= codecs.open("tkn.json","r","utf-8")
                        tkn = json.load(tknop)
                        a = tkn['{}'.format(msg._from)][0]['tkn']
                        req = requests.get(url = '{}'.format(a))
                        b = req.text
                        text = '{}'.format(str(b))
                        dietz.sendMessage(msg.to, str(text))
#=======### COMMAND ADD Custemer ###=======                        
                elif msg.text.lower().startswith(".addcostum "):
                    if msg._from in CSdits:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('JKcs.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ New Costumer Add Executed.")
                                break
                            except:
                                sendTextTemplateDIT(msg.to,"Aᴅᴅᴇᴅ Tᴀʀgᴇᴛ Faɪʟ !")
                                break
                    
                elif msg.text.lower().startswith(".delcostum "):
                    if msg._from in CSdits:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('JKcs.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                sendTextTemplateDIT(msg.to, " ┏━━━━━━━━━━━°❂°\n ❂ Costumer Done Removed Executed.")
                                break
                            except:
                                sendTextTemplateDIT(msg.to,"Rᴇᴍovᴇ Tᴀʀgᴇᴛ Faɪʟ !")
                            break
                            
                elif text.lower() == ".list costum":
                            if msg._from in CSdits:
                                ab = ""
                                a = 0
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    ab += str(a) + ". " +dietz.getContact(m_id).displayName + "\n"
                                sendTextTemplateDIT(msg.to,"°❂°「 List Costumer 」°❂°\n\n°❂°[ Costumer: \n\n"+ab+"\n「%s」List Costumer" %(str(len(admin))))
                
#=======### COMMAND GRUP ###=======
                elif msg.text.lower().startswith(".helpin "):
                  if msg._from in admin:
                      separate = text.split(" ")
                      number = text.replace(separate[0] + " ","")
                      G = dietz.getGroupIdsJoined()
                      cgroup = dietz.getGroups(G)
                      for x in range(len(cgroup)):
                        if number == str(x):
                           gid = cgroup[x].id
                           gname = cgroup[x].name
                      try:
                        dietz.inviteIntoGroup(gid, [msg._from])
                        dietz.sendMessageWithMention(msg.to,msg._from,"","\n°°________________________\nSucces Invited to %s"%(gname))
                      except Exception as error:
                       print (error)
                       print (gid)
                       dietz.sendText(msg.to,"Failed")
                elif msg.text.lower().startswith(".helpnyusup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = dietz.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = dietz.getGroup(group)
                                G.preventedJoinByTicket = False
                                dietz.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = dietz.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n╔═════════❂\n╠❂° Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dietz.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "╠❂° Nama : {}".format(G.name)
                                ret_ += "\n╠❂° Group Qr : {}".format(gQr)
                                ret_ += "\n╠❂° Pendingan : {}".format(gPending)
                                ret_ += "\n╠❂° Group Ticket \n╚═════════❂\n {}".format(gTicket)
                                ret_ += ""
                                dietz.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                elif '.helpwc ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('.helpwc ','')
                              if spl == 'on':
                                  if msg.to in sambitan:
                                       msgs = "°❂°Done on"
                                  else:
                                       sambitan.append(msg.to)
                                       ginfo = dietz.getGroup(msg.to)
                                       msgs = "╔════════════°❂°\n╠°❂°Mode Welc on\n╠°❂°In Group : " +str(ginfo.name) +"\n╚═══════════════°❂°"
                                  sendTextTemplateDIT(msg.to, "「 Status 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in sambitan:
                                         sambitan.remove(msg.to)
                                         ginfo = dietz.getGroup(msg.to)
                                         msgs = "╔════════════°❂°\n╠°❂°Mode Welc off\n╠°❂°In Group : " +str(ginfo.name) +"\n╚═══════════════°❂°"
                                    else:
                                         msgs = "°❂°Done off"
                                    sendTextTemplateDIT(msg.to, "「 Status 」\n" + msgs)
                elif ".helpwelcset: " in msg.text:
                  if msg._from in admin:
                                c = msg.text.replace(".helpwelcset: ","")
                                if c in [""," ","\n",None]:
                                    dietz.sendMessage(msg.to,"❂➤ Mᴇʀᴜᴘᴀᴋᴀɴ sᴛʀɪɴɢ ʏᴀɴɢ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪᴜʙᴀʜ")
                                else:
                                    settings["welcrot"] = c
                                    sendTextTemplateDIT(msg.to, "「Wᴇʟᴄ Mᴀɴ」\n╔════════════°❂°\n╠°❂° Hᴀs Bᴇᴇɴ Cʜᴀɴɢᴇᴅ Tᴏ...\n╠°❂° " + c + "\n╚═══════════════°❂°")
 
                elif ".helpleftset: " in msg.text:
                  if msg._from in admin:
                                c = msg.text.replace(".helpleftset: ","")
                                if c in [""," ","\n",None]:
                                    dietz.sendMessage(msg.to,"❂➤ Mᴇʀᴜᴘᴀᴋᴀɴ sᴛʀɪɴɢ ʏᴀɴɢ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪᴜʙᴀʜ")
                                else:
                                    settings["leftcrot"] = c
                                    sendTextTemplateDIT(msg.to, "「Lᴇғᴛ Mᴀɴ」\n╔════════════°❂°\n╠°❂° Hᴀs Bᴇᴇɴ Cʜᴀɴɢᴇᴅ Tᴏ...\n╠°❂° " + c + "\n╚═══════════════°❂°")

                elif ".helpsiderset: " in msg.text:
                  if msg._from in admin:
                                c = msg.text.replace(".helpsiderset: ","")
                                if c in [""," ","\n",None]:
                                    dietz.sendMessage(msg.to,"❂➤ Mᴇʀᴜᴘᴀᴋᴀɴ sᴛʀɪɴɢ ʏᴀɴɢ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪᴜʙᴀʜ")
                                else:
                                    settings["sidercrot"] = c
                                    sendTextTemplateDIT(msg.to, "「Sɪᴅᴇʀ Mᴀɴ」\n╔════════════°❂°\n╠°❂° Hᴀs Bᴇᴇɴ Cʜᴀɴɢᴇᴅ Tᴏ...\n╠°❂° " + c + "\n╚═══════════════°❂°")
                elif text.lower() == '.helpsider on':
                    if msg._from in admin:
                        try:
                            del cctv['point'][msg.to]
                            del cctv['sidermem'][msg.to]
                            del cctv['cyduk'][msg.to]
                        except:
                            pass
                        cctv['point'][msg.to] = msg.id
                        cctv['sidermem'][msg.to] = ""
                        cctv['cyduk'][msg.to]=True
                        settings["Sider"] = True
                        sendTextTemplateDIT(msg.to, "「Aᴜᴛᴏsɪᴅᴇʀ」\n╔════════════°❂°\n╠°❂° Aʟʀᴇᴀᴅʏ Cᴇᴋ Sɪᴅᴇʀ...\n╚═══════════════°❂°")
                    
                elif text.lower() == '.helpsider off':
                    if msg._from in admin:
                        if msg.to in cctv['point']:
                            cctv['cyduk'][msg.to]=False
                            settings["Sider"] = False
                            sendTextTemplateDIT(msg.to, "「Aᴜᴛᴏsɪᴅᴇʀ」\n╔════════════°❂°\n╠°❂° Cᴇᴋ Sɪᴅᴇʀ Oғғ...\n╚═══════════════°❂°")

                elif text.lower() == ".help glist":
                       if msg._from in admin:
                              ma = ""
                              a = 0
                              gid = dietz.getGroupIdsJoined()
                              for i in gid:
                                  G = dietz.getGroup(i)
                                  a = a + 1
                                  end = "\n"
                                  ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                              sendTextTemplateDIT(msg.to, "╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                              
                elif msg.text.lower().startswith(".help tagroom: "):
                      if msg._from in admin:
                            separate = msg.text.split(":")
                            number = msg.text.replace(separate[0] + ":"," ")
                            groups = dietz.getGroupIdsJoined()
                            gid = groups[int(number)-1]                                                            
                            group = dietz.getGroup(gid)                                                            
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                              txt = u''
                              s=0
                              b=[]
                              for i in group.members[a*20 : (a+1)*20]:
                                b.append(i.mid)
                              mentionMember1(gid, b)                            
                              sendTextTemplateDIT(msg.to, "╔➩[ Succes Mention To Group:\n╠\n╚➩[ " + str(group.name))
                elif msg.text.lower().startswith(".th "):
                    if msg._from in admin:
                        sep = text.split(" ")
                        isi = text.replace(sep[0] + " ","")
                        translator = Translator()
                        hasil = translator.translate(isi, dest='th')
                        A = hasil.text
                        dietz.sendMessage(msg.to, A)
                elif msg.text.lower().startswith(".ar "):
                    if msg._from in admin:
                        sep = text.split(" ")
                        isi = text.replace(sep[0] + " ","")
                        translator = Translator()
                        hasil = translator.translate(isi, dest='ar')
                        A = hasil.text
                        dietz.sendMessage(msg.to, A)
                elif text.lower() == ".helpbye":
                    if msg._from in admin:
                         G = dietz.getGroup(msg.to)
                         dietz.sendMessageWithMention(msg.to,msg._from,"","\n╠❂°Sᴇᴇ Yᴏᴜ・_____\n╠❂°" + str(G.name))
                         dietz.leaveGroup(msg.to)
                elif "/ti/g/" in msg.text.lower():
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = dietz.findGroupByTicket(ticket_id)
                                     dietz.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplateDIT(msg.to, "╔═❂[════════°❂°\n╠❂° Sᴜᴄᴄᴇss Join To Group:\n╠❂° %s" % str(group.name))
                                     
                elif text.lower() == 'qr on':
                    if msg.toType == 2:
                        group = dietz.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            dietz.sendMessage(to, "group qr done open")
                        else:
                            group.preventedJoinByTicket = False
                            dietz.updateGroup(group)
                            dietz.sendMessage(to, "group qr open")
                elif text.lower() == 'qr off':
                    if msg.toType == 2:
                        group = dietz.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            dietz.sendMessage(to, "group qr done close")
                        else:
                            group.preventedJoinByTicket = True
                            dietz.updateGroup(group)
                            dietz.sendMessage(to, "group qr close")
                           

        if op.type == 26:
            #print ("PENSAN TELAH DI TERIMA!!!")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != dietz.getProfile().mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                dietz.sendChatChecked(to, msg_id)
        
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = dietz.getContact(op.param2).displayName
                            ginfo = dietz.getGroup(op.param1)
                            dit = settings["sidercrot"]
                            contact = dietz.getContact(op.param2)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendTextTemplateDIT(op.param1, "" + "☞ " + nick[0] + " ☜" + "")
                                        dietz.sendImageWithURL(op.param1,image)
                                        sendTextTemplateDIT(op.param1, "『Aᴜᴛᴏsɪᴅᴇʀ』\nHᴀɪɪ " + "☞ " + nick[0] + " ☜" + "\n" + dit)
                                    else:
                                        sendTextTemplateDIT(op.param1, "" + "☞ " + nick[1] + " ☜" + "")
                                        dietz.sendImageWithURL(op.param1,image)
                                        sendTextTemplateDIT(op.param1, "『Aᴜᴛᴏsɪᴅᴇʀ』\nHᴀɪɪ " + "☞ " + nick[1] + " ☜" + "\n" + dit)
                                else:
                                    sendTextTemplateDIT(op.param1, "" + "☞ " + Name + " ☜" + "")
                                    dietz.sendImageWithURL(op.param1,image)
                                    sendTextTemplateDIT(op.param1, "『Aᴜᴛᴏsɪᴅᴇʀ』\nHᴀɪɪ " + "☞ " + Name + " ☜" + "\n" + dit)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
        
        if op.type == 55:
            print ("PESAN TELAH DI BACA!!!")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
