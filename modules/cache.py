
import os
import shutil
import subprocess


def CacheSize(msg):
    print("Getting Cache Size", flush=True)
    output = subprocess.check_output(['du','-sh', 'Downloads']).split()[0].decode('utf-8')
    msg.reply_text("Cache size : " + output)

def clearCache(msg):
    print("Clearing cache", flush=True)
    #delete all files in Downloads folder using linux command
    shutil.rmtree('Downloads')
    os.makedirs('Downloads')
    #subprocess.call(['rm','-rf','Downloads/*'])
    msg.reply_text("Cache Cleared")
    CacheSize(msg)
