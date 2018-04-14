#--===auroraplugin===--
#  -*- coding: utf-8 -*-
#  aurora plugin
#  version_plugin.py
#  edited by kf (kforkingfisher@gmail/nimbuzz.com)
#############################################
###########    ##    #####         ##########
############  ###  #######  #####  ##########
############  ##  ########  #################
############  #  #########  #################
############    ##########  #### ############
############   ###########       ############
############    ##########  #### ############
############  #  #########  #################
############  ##   #######  #################
############  ###   ######  #################
###########    ##     ###    ################
#############################################
###########KFORKINGFISHER@GMAIL.COM##########
##########KFORKINGFISHER@NIMBUZZ.COM#########
#############################################

import os, sys

version_pending=[]

def handler_version(type, source, parameters):
	nick = source[2]
	groupchat=source[1]
	iq = xmpp.Iq('get')
	id='vers'+str(random.randrange(1000, 9999))
	globals()['version_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'jabber:iq:version');
	if parameters:
		jid=groupchat+'/'+parameters.strip()
		if GROUPCHATS.has_key(groupchat):
			nicks = GROUPCHATS[groupchat].keys()
			param = parameters.strip()
			if not nick in nicks:
				iq.setTo(param)
			else:
				if GROUPCHATS[groupchat][nick]['ishere']==0:
					reply(type, source, u'А он тут? :-O')
					return
				iq.setTo(jid)
	else:
		jid=groupchat+'/'+nick
		iq.setTo(jid)
	JCON.SendAndCallForResponse(iq, handler_version_answ, {'type': type, 'source': source})
	return

def handler_version_answ(coze, res, type, source):
	id=res.getID()
	if id in globals()['version_pending']:
		globals()['version_pending'].remove(id)
	else:
		print 'Someone is doing wrong...'
		return
	rep =''
	if res:
		if res.getType() == 'result':
			name = '[no name]'
			version = '[no ver]'
			hos = '[no os]'
			props = res.getQueryChildren()
			for p in props:
				if p.getName() == 'name':
					name = p.getData()
				elif p.getName() == 'version':
					version = p.getData()
				elif p.getName() == 'os':
					hos = p.getData()
			if name:
				rep = name
			if version:
				rep +=' '+version
			if hos:
				rep += ' [OS: ' + hos + ']'
		elif res.getType() == 'get':
			name = '[no name]'
			version = '[no ver]'
			hos = '[no os]'
			
			last_rev = get_last_rev(SVN_REPOS)
			
			name = BOT_VER['botver']['name']
			version = BOT_VER['botver']['ver'] % (BOT_VER['rev']+last_rev)
			hos = BOT_VER['botver']['os']
			
			if not BOT_VER['botver']['os']:
				osver=''
				if os.name=='nt':
					osname=os.popen("ver")
					osver=osname.read().strip().decode('cp866')+'\n'
					osname.close()			
				else:
					osname=os.popen("uname -sr", 'r')
					osver=osname.read().strip()+'\n'
					osname.close()			
				pyver = sys.version
				BOT_VER['botver']['os'] = osver + ' ' + pyver
			
			hos = BOT_VER['botver']['os']
			
			if name:
				rep = name
			if version:
				rep +=' '+version
			if hos:
				rep += ' [OS: ' + hos + ']'
		else:
			rep = u'It is encrypted!'
	else:
		rep = u'No such !'
		
	reply(type, source, rep)
	
register_command_handler(handler_version, '.version', ['info','muc','all','*'], 0, 'Shows information about a client which utillizes user or server.', '.version [nick\server]', ['.version','.version nick','.version jsmart.web.id'])