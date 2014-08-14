#!/usr/bin/env python

#

from sulley   import *
from requests import http

########################################################################################################################
#sess = sessions.session(session_filename="audits/webrick_2000.session")

sess = sessions.session(session_filename="audits/icecast.session",sleep_time=0.01)
target = sessions.target("127.0.0.1", 8000)
"""
target.procmon         = pedrpc.client("127.0.0.1", 26002)
target.procmon_options = \
{ 
	"proc_name" : "ntop", 
	"start_command" : "/etc/init.d/ntop start",
	"stop_command" : "/etc/init.d/ntop stop",
}
"""
sess.add_target(target)
sess.connect(s_get("HTTP VERBS"))
sess.connect(s_get("HTTP VERBS BASIC"))
sess.connect(s_get("HTTP VERBS POST"))
sess.connect(s_get("HTTP HEADERS"))
sess.connect(s_get("HTTP COOKIE"))
sess.fuzz()
