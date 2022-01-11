#!/usr/bin/python3
import os.path
from sys import argv
from subprocess import check_output, Popen, PIPE, call


def generate(executable, payload, loader, domain, cs_directory, etw, sandbox, ps_injection, loader_name):

    command = [executable, '-I', payload, '-Loader', loader, '-domain', domain]

    if etw == 'true':
        command.append('-etw')

    if sandbox == 'true':
        command.append('-sandbox')

    if ps_injection:
        command.append('-injection')
        command.append('{}'.format(ps_injection))

    if loader_name:
        if not loader_name.endswith('.js'):
            loader_name = "{}.js".format(loader_name)
        command.append('-O')
        command.append(loader_name)

    filename = None
    if loader in ["control", "excel", "msiexec", "wscript"] and loader_name:
        filename = loader_name
    elif loader in ["excel", "msiexec", "wscript"] and not loader_name:
        filename = "Loader.js"
        command.append('-O')
        command.append(filename)

    process = Popen(command, stdout=PIPE)
    stdout, stderr = process.communicate()    
    
    if loader in ["binary", "dll", "control"]:
        for row in stdout.decode('utf-8').splitlines():
            if row.startswith('[*] Signing'):
                filename = row
                break

        filename = filename.split('[*] Signing ')[1].split(' With a Fake Cert')[0]

        if loader == "control" and not loader_name:
            filename = filename[:-3] + "cpl"

        elif loader == "control" and loader_name:
            filename = loader_name

    call(['mv', cs_directory + '/' + filename, os.path.dirname(payload) + "/"])
    
    check_output(['rm', '-f', payload])

    return os.path.dirname(payload) + "/" + filename


if __name__ == '__main__':
    arg_list = argv[1:]

    if len(arg_list) < 8:
        arg_list.append(None)
    if len(arg_list) < 9:
        arg_list.append(None)

    shellcode_dir = generate(arg_list[0], arg_list[1], arg_list[2], arg_list[3], arg_list[4], arg_list[5], arg_list[6], arg_list[7], arg_list[8])
    print(shellcode_dir)
