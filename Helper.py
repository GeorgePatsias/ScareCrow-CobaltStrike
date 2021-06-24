#!/usr/bin/python3
from sys import argv
from subprocess import check_output


def generate(executable, payload, loader, domain):
    check_output([executable, '-I', payload, '-Loader', loader, '-domain', domain])
    check_output(['rm', '-f', payload])


if __name__ == '__main__':
    arg_list = argv[1:]

    generate(arg_list[0], arg_list[1], arg_list[2], arg_list[3])
