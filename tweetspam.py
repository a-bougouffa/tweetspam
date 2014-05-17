# NOTE: I write this just for fun, don't use it! don't be evil ^_^

import subprocess
import random

list_des_mots = (	"Je suis au #algeria20",
					"rahom ya7ko 3la les #SOCIAL_MEDIA #algeria20"
					"O.o #algeria20",
					":P #algeria20",
					"-_- 'social!!!' MEDIA!! #algeria20",
					"je suis un SPAM #algeria20")

while True:
	twitter_tool = 'twitter -eabdelhak.alg@gmail.com set %s' % random.choice(list_des_mots)
	subprocess.call(twitter_tool, shell=True)
	print("Twitted ", end=" ")
