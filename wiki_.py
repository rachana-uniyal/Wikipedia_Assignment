'''import json
import time
from sseclient import SSEClient as EventSource

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
#flag = True
end_time = time.time() + 60

while end_time>= time.time():
	for event in EventSource(url):
		if event.event =='message':
			change = json.dumps(event.data, indent=4)
		else:
			pass
print(change)

'''
'''import json           
from pywikibot.comms.eventstreams import EventStreams
stream = EventStreams(streams=['recentchange', 'revision-create'],
		          since='20190111')
stream.register_filter(server_name='fr.wikipedia.org', type='edit')
change = next(iter(stream))
print('{type} on page "{title}" by "{user}" at {meta[dt]}.'.format(**change))'''
'''with open("data.json", "a+") as outfile: 
					outfile.write(event.data+'\n') 
				change = json.loads(event.data)'''

import json
import time
from sseclient import SSEClient as EventSource
import pprint

url = 'https://stream.wikimedia.org/v2/stream/recentchange'

c =0
#t_end = time.time() + 60 

#while time.time() < t_end:
for event in EventSource(url):
	c = c+1
	if c ==50:
		break
	if event.event == 'message':
		try:
			#out_file = open("my-file", "a+")
			#out_file.write(event.data+'\n')
			pass
			print("adding")
			#out_file.close()
		except ValueError:
			pass
		else:
			print("running")
				#print('{user} edited {title}'.format(**change))

			
print("1 min over")

with open('my-file') as f:
	content = f.readlines()
	for i in content:
		data = json.loads(i)
		print(data['meta']['domain'])
		#pprint.pprint(data)



	



           
