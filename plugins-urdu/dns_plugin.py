#--===auroraplugin===--
#  -*- coding: utf-8 -*-
#  riax plugin
#  dns_plugin.py
#  edited by Mr Riaz Hussain

import socket

def dns_query(query):
	try:
		int(query[-1])
	except ValueError:
		try:
			(hostname, aliaslist, ipaddrlist) = socket.gethostbyname_ex(query)
			return u', '.join(ipaddrlist)
		except socket.gaierror:
			return u'i did not find :-('
	else:
		try:
			(hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(query)
		except socket.herror:
			return u'sorry i did not find :-('
		return hostname + ' ' + string.join(aliaslist) + ' ' + string.join(aliaslist)

def handler_dns_dns(type, source, parameters):
	if parameters.strip():
		result = dns_query(parameters)
		reply(type, source, result)
	else:
		reply(type, source, u'what is it?')
def handler_pak(type, source, parameters):
       replies = [u'i love pak']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_riaz(type, source, parameters):
       replies = [u'riaz is my owner']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_zehri(type, source, parameters):
       replies = [u'zehri is my owner']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_mr_zehri(type, source, parameters):
       replies = [u'mr_zehri created me :) ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_tameena(type, source, parameters):
       replies = [u'tameene to mere malik hai :-P ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_tameene(type, source, parameters):
       replies = [u'tameene to mere malik hai :-P ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_tamina(type, source, parameters):
       replies = [u'tamina zehri :$ kaha hai    ? :-P']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_tamine(type, source, parameters):
       replies = [u'tamina zehri :$ kaha hai   ? :-P']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_kameena(type, source, parameters):
       replies = [u'kameene to mere malik hai :-P ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_kameene(type, source, parameters):
       replies = [u'kameene to mere malik hai :-P ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_kamina(type, source, parameters):
       replies = [u'kamina kf :$ kaha hai kf ? :-P']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_kamine(type, source, parameters):
       replies = [u'aho aho is kamina :$ where is he ? :-P']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_maker_(type, source, parameters):
       replies = [u'zehri bot is property of \nMR_zehri \ncontact him at:\nmr_zehri@nimbuzz.com \nz3hri@nimbuzz.com \nriazjohn45@gmail.com']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)

def handler_english_(type, source, parameters):
       replies = [u'zehri bot is edited by \nMr_zehri \ncontact him at : \nmr_zehri@nimbuzz.com \nz3hri@nimbuzz.com \nriazjohn45@gmail.com ']
       balas = random.choice(replies)
       if type == 'public':
               if source[1]:
                       reply(type, source, balas)
       elif type == 'private':
               reply(type, source, balas)


register_command_handler(handler_dns_dns, 'dns', ['info','all'], 10, 'Shows an answer from DNS for a certain host or IP of address.', 'dns <host/IP>', ['dns server.tld', 'dns 127.0.0.1'])
register_command_handler(handler_pak, 'pak', ['new'], 0, '', '', [''])
register_command_handler(handler_riaz, 'riaz', ['new'], 0, '', '', [''])
register_command_handler(handler_zehri, 'zehri', ['new'], 0, '', '', [''])
register_command_handler(handler_mr_zehri, 'mr_zehri', ['new'], 0, '', '', [''])
register_command_handler(handler_tameena, 'tameena', ['new'], 0, '', '', [''])
register_command_handler(handler_tameene, 'tameene', ['new'], 0, '', '', [''])
register_command_handler(handler_tamina, 'tamina', ['new'], 0, '', '', [''])
register_command_handler(handler_tamine, 'tamine', ['new'], 0, '', '', [''])
register_command_handler(handler_kameena, 'kameena', ['new'], 0, '', '', [''])
register_command_handler(handler_kameene, 'kameene', ['new'], 0, '', '', [''])
register_command_handler(handler_kamina, 'kamina', ['new'], 0, '', '', [''])
register_command_handler(handler_kamine, 'kamine', ['new'], 0, '', '', [''])
register_command_handler(handler_maker_, 'maker', ['new'], 0, '', '', [''])
register_command_handler(handler_maker_, 'owner', ['new'], 0, '', '', [''])
register_command_handler(handler_maker_, 'malik', ['new'], 0, '', '', [''])
register_command_handler(handler_maker_, 'aurora', ['new'], 0, '', '', [''])
register_command_handler(handler_maker_, 'creator', ['new'], 0, '', '', [''])
register_command_handler(handler_english_, 'english', ['new'], 0, '', '', [''])
register_command_handler(handler_english_, 'eng', ['new'], 0, '', '', [''])

