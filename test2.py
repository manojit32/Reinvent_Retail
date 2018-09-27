import recomm1
import ast
import sentiment1
#import chat1
while(True):

	a = input("give input : ")
	d = ast.literal_eval(a)

	try:

		if(d['t']):
			
			recomm1.trending()
		
			
	except:
		pass
		
	try:
		if(d['u']):
			
			recomm1.user_based(d['u'])
			
	except:
		pass
		
	try:

		if(d['i']):
			
			recomm1.item_based(d['i'])
			
	except:
		pass
	try:

		if(d['s']):
			#import sentiment1
			sentiment1.analyzer(d['s'])
			
	except:
		pass	

	try:

		if(d['c']):
			import checkout
			checkout.generate()
			
	except:
		pass

	try:

		if(d['b']):
			#import chat1
			chat1.chatbot(d['b'])
			
	except:
		pass

	try:

		if(d['f']):
			import item_finder
			item_finder.finder(d['f'])
			
	except:
		pass
	
	
	
	
