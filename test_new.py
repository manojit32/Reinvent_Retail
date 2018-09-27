import recomm
import sentiment1
import checkout
import ast
import chat0
a = input()
d = ast.literal_eval(a)

try:

	if(d['t']):
		recomm.trending()
	
		
except:
	pass
	
try:
	if(d['u']):
		recomm.user_based(d['u'])
		
except:
	pass
	
try:

	if(d['i']):
		recomm.item_based(d['i'])
		
except:
	pass
try:

	if(d['s']):
		sentiment1.analyzer(d['s'])
		
except:
	pass	

try:

	if(d['c']):
		checkout.generate()
		
except:
	pass

try:

	if(d['b']):
		chat0.chatbot(d['b'])
		
except:
	pass

	
	
	
	
	