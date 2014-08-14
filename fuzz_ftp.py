#!/usr/bin/env python

from sulley   import *
from requests import ftp

s = sessions.session(session_filename="audits/ftp.session")

""""Define state model."""
# commands directly accessible without login
#s.connect(s_get('AUSER'))
s.connect(s_get('AUSER'))
s.connect(s_get('APASS'))
s.connect(s_get('AUSER'), s_get('APASS'))
s.connect(s_get('AHELP'))
s.connect(s_get('AACCT'))
s.connect(s_get('APROT'))
s.connect(s_get('APBSZ'))
s.connect(s_get('AHOST'))
s.connect(s_get('AAUTH'))
s.connect(s_get('AADAT'))
# authenticated commands
s.connect(s_get('DataUSER'))
s.connect(s_get('DataUSER'), s_get('DataPASS'))

s.connect(s_get('DataPASS'), s_get('DataSet1'))
s.connect(s_get('DataPASS'), s_get('PORT'))
s.connect(s_get('DataPASS'), s_get('TYPE1'))
s.connect(s_get('DataPASS'), s_get('TYPE2'))
s.connect(s_get('DataPASS'), s_get('TYPE3'))
s.connect(s_get('DataPASS'), s_get('TYPE4'))
s.connect(s_get('DataPASS'), s_get('ALLO1'))
s.connect(s_get('DataPASS'), s_get('ALLO2'))
s.connect(s_get('DataPASS'), s_get('PBSZ'))
s.connect(s_get('DataPASS'), s_get('EPRT'))
s.connect(s_get('DataPASS'), s_get('EPSV'))
s.connect(s_get('DataPASS'), s_get('LANG'))
s.connect(s_get('DataPASS'), s_get('EPRT'))

# special order of commands
# PASS
s.connect(s_get('DataPASS'), s_get('DataPASV'))
s.connect(s_get('DataPASV'), s_get('APPE'))
s.connect(s_get('DataPASV'), s_get('STOR'))
s.connect(s_get('DataPASV'), s_get('NLST'))
s.connect(s_get('DataPASV'), s_get('LIST'))
s.connect(s_get('DataPASV'), s_get('RETR'))
s.connect(s_get('DataPASV'), s_get('STOU'))
# PORT
s.connect(s_get('DataPASS'), s_get('DataPORT'))
s.connect(s_get('DataPORT'), s_get('APPE'))
s.connect(s_get('DataPORT'), s_get('STOR'))
s.connect(s_get('DataPORT'), s_get('NLST'))
s.connect(s_get('DataPORT'), s_get('LIST'))
s.connect(s_get('DataPORT'), s_get('RETR'))
s.connect(s_get('DataPORT'), s_get('STOU'))
# REST
s.connect(s_get('DataPASS'), s_get('DataREST'))
s.connect(s_get('DataREST'), s_get('APPE'))
s.connect(s_get('DataREST'), s_get('STOR'))
s.connect(s_get('DataREST'), s_get('RETR'))
# RNFR
s.connect(s_get('DataPASS'), s_get('DataRNFR'))
s.connect(s_get('DataRNFR'), s_get('RNTO'))




#######################################################################
""" Define the target to fuzz. """
target         = sessions.target("dougsko.com", 21)
""" grab the banner from the server """
s.pre_send = banner

""" start fuzzing - define target and data """
s.add_target(target)
s.fuzz()
