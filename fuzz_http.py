#!/usr/bin/env python

#

from sulley   import *
from requests import http

########################################################################################################################
#sess = sessions.session(session_filename="audits/webrick_2000.session")

sess = sessions.session(session_filename="audits/http.session",sleep_time=0.01)
verizon = sessions.target("10.0.0.1", 80)
ddwrt = sessions.target("10.0.0.100", 80)
monkey = sessions.target("127.0.0.1", 2001)
icecast = sessions.target("127.0.0.1", 8000)
sess.add_target(verizon)
sess.add_target(ddwrt)
sess.add_target(monkey)
sess.add_target(icecast)
sess.connect(s_get("HTTP VERBS"))
sess.connect(s_get("HTTP VERBS BASIC"))
sess.connect(s_get("HTTP VERBS POST"))
sess.connect(s_get("HTTP HEADERS"))
sess.connect(s_get("HTTP COOKIE"))
sess.fuzz()
