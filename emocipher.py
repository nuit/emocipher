#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#-*- coding: latin-1 -*-
import os
import random
from flask import Flask, request, redirect, render_template, Response
from collections import OrderedDict

import sys
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, template_folder="templates")

lt=list(u"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÇÑ!?-+=_.,:&( )_;%*@$#'<>")
em=u"☂ 😎 😀 😂 😅 😆 😃 😠 😏 😓 😖 😊 😍 😘 😚 😋 😝 😛 😕 😱 😈 😉 ☺ 😽 😻 😇 😼 ❤ ♡ ☻ ♥ 🆗 ♠ ♣ ♦ ⚓ 🐵 🐭 ☀ ☔ ⚽ ❌ ❎ ❓ ➡ 🈁 🈳 ♮ ☠ ☿ ♬ ⚸ ※ ⁜ ⁂ ► ◄ ⋇ ⍰ ☏ ☢ ☣ ☾ 🀄 🃏 ♛ ♚ ♞ ⚒ ⚙ ☄".split()


def get_id():
	global index
	arquivo=open('id.txt', 'rw')     
	index=arquivo.read()   
	arquivo.close()


def save_id(index):
    arquivo=open('id.txt','w')
    arquivo.write(index)
    arquivo.close()
    

dc=OrderedDict()
lc=''
def make_dict():
	global dc,lc
	random.shuffle(em)
	for x,y in zip(lt,em):
		dc[x]=y
		lc += x.encode('utf-8')+'='+y.encode('utf-8')+' ; '


def cipher(text):
	ct=[]
	global lc,ctext,rc,index
	make_dict()
	for l in text:
		l=l.upper()
		for x,y in dc.items():
			if l==x:
				if l==' ':
					y='  '
					ct.append(y)  	
				else:
					ct.append(y)
	
	rc=''.join(ct)
	get_id()
	index=str(int(index)+1)
	save_id(index)
	return index, rc, dc


@app.route("/e8147d4acb721de7550ab5f38fca571c")
def header():
    return render_template('key.html', id=index, cdict=dc)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cipher', methods=['POST'])
def ciphered():
    text = request.form['text']
    cipher(text)
    return render_template('cipher.html', id=index, cipher=rc)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
