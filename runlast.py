import os, subprocess

last = sorted(list(filter(lambda x: x[:3] == 'dec' and x[-2:] == 'py', os.listdir())))[-1]
subprocess.run(["python", last])