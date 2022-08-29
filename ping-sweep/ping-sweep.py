#! /home/kali/Documents/myPythonScripts/ping-sweep/.venv/bin/python3

from pythonping import ping

net_ip = input('Enter the /24 network to ping:>\n')
split_input = net_ip.split('.')
split_input.pop()
three_octects = '.'.join(split_input)
results_list = []

for i in range(1, 255):
    print(f'Pinging {three_octects}.{i}')
    result = ping(f'{three_octects}.{i}', count=1, timeout=0.10, verbose=True)
    results_list.append(result)

print('\n The following devices are online:')
format_results = []
for i in results_list:
    if str(i).startswith('Reply'):
        format_results.append(str(i))

for i in format_results:
    split_text = i.split(',')
    online = split_text[0]
    print(online)