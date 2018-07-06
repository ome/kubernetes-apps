#!/usr/bin/env python

import argparse
import subprocess
import sys
import yaml


def parse_args(args):
    description = """\
Partial implementation of "helmfile sync" in Python. This will run the
same Helm commands that "helmfile sync" would run. Use --dry-run to
print the list of commands.

helmfile selectors (allows selective partial deployment) are not
implemented, nor are any other commands or arguments. Use the proper
Helmfile if you require that
"""
    p = argparse.ArgumentParser(description=description)
    p.add_argument('-f', '--file', default='helmfile.yaml', help='Helmfile')
    p.add_argument('--dry-run', action='store_true', help='Dry run')
    return p.parse_args(args)


def load_config(helmfile):
    with open(helmfile) as f:
        y = list(yaml.load_all(f))
    if len(y) != 1:
        raise ValueError('Expected one YAML document, found %d' % len(y))
    y = y[0]
    if 'releases' not in y:
        raise ValueError('Expected releases in helmfile')
    return y


def get_helm_command(r):
    command = [
        'helm',
        'upgrade',
        '--install',
        r['name'],
        r['chart'],
    ]
    if 'version' in r:
        command.extend(['--version', r['version']])
    if 'namespace' in r:
        command.extend(['--namespace', r['namespace']])
    for v in r['values']:
        command.extend(['--values', v])
    return command


def main(args):
    cfg = load_config(args.file)
    commands = [get_helm_command(r) for r in cfg['releases']]
    for c in commands:
        print(' '.join(c))
        if not args.dry_run:
            subprocess.check_call(c)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
