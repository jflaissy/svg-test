import subprocess
import time

def go(input_file, output_dir, parameters):
    print 'Capture statique. in:', input_file, 'out:', output_dir
    output_file = "%s.png" % output_dir

    p = subprocess.Popen(['google-chrome', '--new-window'])
    print 'sleep 10s...'
    time.sleep(10)
    print 'ok'
    p.kill()
    return output_file
