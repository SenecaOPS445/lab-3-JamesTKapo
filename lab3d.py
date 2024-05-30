#!/usr/bin/env python3
# Author ID: jkapogiannis
import subprocess

def free_space():
    process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    process_grep = subprocess.Popen(['grep', '/$'], stdin=process.stdout, stdout=subprocess.PIPE)
    process_awk = subprocess.Popen(['awk', '{print $4}'], stdin=process_grep.stdout, stdout=subprocess.PIPE)
    process.stdout.close()
    process_grep.stdout.close()
    output, _ = process_awk.communicate()


    return output.decode('utf-8').strip()

print(free_space())