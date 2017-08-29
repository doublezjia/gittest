#coding=utf8
import requests,os
import itchat

key = 'dc47ce10cfd24347a6e0baf08401d2d8'
def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
	    'key'    : key, # 如果这个Tuling Key不能用，那就换一个
	    'info'   : msg, # 这是我们发出去的消息
	    'userid' : 'Atom', # 这里你想改什么都可以
	}
	# 我们通过如下命令发送一个post请求
	try:
		req = requests.post(apiUrl, data=data).json()
		if req.get('code') == 200000 :
			return req.get('text')+'\n'+req.get('url')
		elif req.get('code') == 302000:
			new = ''
			for i in range(len(req.get('list'))):
				new =new+'\n标题：'+req.get('list')[i].get('article')+'\n地址：'+req.get('list')[i].get('detailurl')+'\n来源：'+req.get('list')[i].get('source')+'\n'
			return req.get('text')+'\n'+new
		else:
			return req.get('text')
	except:
		return 'QAQ Error'

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	if msg['ToUserName'] != 'filehelper': 
		return
	else:
		# defaultReply = 'I received: ' + msg['Text']
		reply = get_response(msg['Text'])
		# return reply or defaultReply
		itchat.send(reply,'filehelper')
itchat.auto_login()
itchat.run()
