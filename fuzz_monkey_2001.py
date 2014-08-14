#!/usr/bin/env python

#

import os
import urllib2
from sulley   import *
from requests import http
from requests import http_header

def monkey_is_alive():
	try:
		res = urllib2.urlopen("http://ganon:2001", timeout=1).read()
	except:
		print("The server seems down. restarting...")
		res = ''
	return res != ''

def monkey_start():
	os.popen2('sudo /etc/init.d/monkey restart')

sess = sessions.session(session_filename="audits/monkey.session",sleep_time=0.1)
target = sessions.target("127.0.0.1", 2001)
#target.procmon = instrumentation.external(post=monkey_is_alive,
#		start=monkey_start)
sess.add_target(target)
sess.connect(s_get("HTTP VERBS"))
sess.connect(s_get("HTTP VERBS BASIC"))
sess.connect(s_get("HTTP VERBS POST"))
sess.connect(s_get("HTTP HEADERS"))
sess.connect(s_get("HTTP COOKIE"))

"""
sess.connect(s_get("HTTP HEADER ACCEPT"))
sess.connect(s_get("HTTP HEADER ACCEPTCHARSET"))
sess.connect(s_get("HTTP HEADER ACCEPTDATETIME"))
sess.connect(s_get("HTTP HEADER ACCEPTENCODING"))
sess.connect(s_get("HTTP HEADER ACCEPTLANGUAGE"))
sess.connect(s_get("HTTP HEADER AUTHORIZATION"))
sess.connect(s_get("HTTP HEADER CACHECONTROL"))
sess.connect(s_get("HTTP HEADER CLOSE"))
sess.connect(s_get("HTTP HEADER CONTENTLENGTH"))
sess.connect(s_get("HTTP HEADER CONTENTMD5"))
sess.connect(s_get("HTTP HEADER COOKIE"))
sess.connect(s_get("HTTP HEADER DATE"))
sess.connect(s_get("HTTP HEADER DNT"))
sess.connect(s_get("HTTP HEADER EXPECT"))
sess.connect(s_get("HTTP HEADER FROM"))
sess.connect(s_get("HTTP HEADER HOST"))
sess.connect(s_get("HTTP HEADER IFMATCH"))
sess.connect(s_get("HTTP HEADER IFMODIFIEDSINCE"))
sess.connect(s_get("HTTP HEADER IFNONEMATCH"))
sess.connect(s_get("HTTP HEADER IFRANGE"))
sess.connect(s_get("HTTP HEADER IFUNMODIFIEDSINCE"))
sess.connect(s_get("HTTP HEADER KEEPALIVE"))
sess.connect(s_get("HTTP HEADER MAXFORWARDS"))
sess.connect(s_get("HTTP HEADER PRAGMA"))
sess.connect(s_get("HTTP HEADER PROXYAUTHORIZATION"))
sess.connect(s_get("HTTP HEADER RANGE"))
sess.connect(s_get("HTTP HEADER REFERER"))
sess.connect(s_get("HTTP HEADER TE"))
sess.connect(s_get("HTTP HEADER UPGRADE"))
sess.connect(s_get("HTTP HEADER USERAGENT"))
sess.connect(s_get("HTTP HEADER VIA"))
sess.connect(s_get("HTTP HEADER WARNING"))
sess.connect(s_get("HTTP HEADER XATTDEVICEID"))
sess.connect(s_get("HTTP HEADER XDONOTTRACK"))
sess.connect(s_get("HTTP HEADER XFORWARDEDFOR"))
sess.connect(s_get("HTTP HEADER XREQUESTEDWITH"))
sess.connect(s_get("HTTP HEADER XWAPPROFILE"))
"""

sess.fuzz()
