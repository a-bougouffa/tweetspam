import subprocess
tweet = input("Tweet: ")
twitter_tool = 'twitter -eabdelhak.alg@gmail.com set %s' % tweet
subprocess.call(twitter_tool, shell=True)
