import json
import time
from sseclient import SSEClient as EventSource
import pprint

def wiki_stream(): 
	

	url = 'https://stream.wikimedia.org/v2/stream/revision-create'

	c =0
	domain = {}
	user = {}
	start_time = time.time()
	limit = 60
	open("file1", "w").close()
	for event in EventSource(url):
		if (time.time() - start_time) > limit:
			print("*********************************************** Last 1 Min Report **************************************************")
			print("\n")
			break
		if event.event == 'message':
			try:
				out_file = open("file1", "a+")
				out_file.write(event.data+'\n')
				pass
				out_file.close()
			except ValueError:
				pass
	
	
	with open('file1') as f:
		content = f.readlines()
		for i in content:
			if not i.lstrip().rstrip():
				continue
			data = json.loads(i)
			key = data['meta']['domain']
			if key in domain:
				domain[key] = domain[key]+1
			else:
				domain[key] = 1	
			
	dict(sorted(domain.items(), key=lambda item: item[1]))	

	print("                                                        Domain Report")
	print("\n")
	print("Total number of Wikipedia Domains Updated:", len(domain))	
	for d in domain:
		print(d , " : " ,domain[d] , " Pages updated")	


	print("\n")


	with open('file1') as f:
		content = f.readlines()
		for i in content:
			if not i.lstrip().rstrip():
				continue
			data = json.loads(i)
			usr = data['performer']['user_text']
			if data['meta']['domain']=='en.wikipedia.org':
				if usr in user:
					user[usr] = max(user[usr], data['performer']['user_edit_count'])

				else:
					try:
						user[usr] = data['performer']['user_edit_count']
					except:
						pass	


	dict(sorted(user.items(), key = lambda item: item[1]))


	print("                                                        User Report")
	print("\n")
	print("Users who made changes to en.wikipedia.org")
	print("\n")

	for key, value in user.items():
		print(key, " : " ,value)


while (1):
	wiki_stream()
	pass


	



		   
