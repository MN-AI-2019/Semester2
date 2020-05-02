
import subprocess
import re
import os 

import send_email

def start_ngrok(wait_time):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    process = subprocess.Popen([dir_path + '/ngrok', 'http', '8080', '--log', 'stdout'], 
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        line = output.strip()
        print(line)
        m = re.search('(?<=url\=)http:\S+', line)
        if m is not None:
            print('Find address ', m.group(0))
            send_email.send_email_api("dowliang@gmail.com", m.group(0))

            try:
                process.wait(wait_time)
            except subprocess.TimeoutExpired:
                process.kill()
            
        # Do something else, need to capture the url.
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

start_ngrok(10)
