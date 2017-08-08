import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())

    maarker = results.find('has address') + 12

    return  results[maarker:].splitlines()[0]

