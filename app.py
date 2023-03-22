from flask import Flask
from skpy import Skype
from flask import request
app = Flask(__name__)
@app.route('/',methods=['GET'] )
def heloo():
    return "hello"

@app.route('/skypemsg',methods=['GET','POST'] )
def Skype_msgSend():
    data = request.json
    userName = data.get('userName')
    password =  data.get('Password')
    sendTo = data.get('sendTo')
    msg = data.get('message')

    try:
        sk = Skype(userName,password) # connect to Skype
        sk.user # you
        sk.contacts # your contacts
        sk.chats # your conversations
        ch = sk.contacts[sendTo].chat # 1-to-1 conversation
        ch.sendMsg(msg)
    except:
        print(userName, msg,sendTo, password)
        return(msg)
    else:
        return("Msg sent")
    
