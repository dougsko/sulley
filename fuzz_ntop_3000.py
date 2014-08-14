#!/usr/bin/env python

#

from sulley   import *
from requests import http

########################################################################################################################
#sess = sessions.session(session_filename="audits/webrick_2000.session")

sess = sessions.session(session_filename="audits/ntop.session",sleep_time=0.2)
target = sessions.target("127.0.0.1", 3000)
sess.add_target(target)
#sess.connect(s_get("HTTP VERBS"))
#sess.connect(s_get("HTTP VERBS BASIC"))
#sess.connect(s_get("HTTP VERBS POST"))
sess.connect(s_get("HTTP HEADERS"))
#sess.connect(s_get("HTTP COOKIE"))
sess.fuzz()
