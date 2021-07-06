#!/usr/bin/python3
import os.path
from sys import argv
from subprocess import check_output, Popen, PIPE, call


def generate(executable, payload, loader, domain, cs_directory):
    process = Popen([executable, '-I', payload, '-Loader', loader, '-domain', domain], stdout=PIPE)
    stdout, stderr = process.communicate()

    reader = stdout.decode('utf-8').splitlines()

    filename = None
    for row in reader:
        if row.startswith('[*] Signing'):
            filename = row

    filename = filename.split('[*] Signing ')[1].split(' With a Fake Cert')[0]

    call(['mv', cs_directory + '/' + filename, os.path.dirname(payload) + "/"])
    check_output(['rm', '-f', payload])

    return os.path.dirname(payload) + "/" + filename


if __name__ == '__main__':
    arg_list = argv[1:]

    shellcode_dir = generate(arg_list[0], arg_list[1], arg_list[2], arg_list[3], arg_list[4])
    print(shellcode_dir)
