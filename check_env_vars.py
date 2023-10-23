# Checks the presence of a environment-variable against a given template file
import argparse
import os
import sys

SEPARATOR = '='
IS_OPTIONAL_STR = '(optional)'

def check_file_exists(filepath):
    """Check file exists"""
    if not os.path.exists(filepath):
        print(f"File not found at path: {filepath}")
        return False
    return True

def read_vars_from_file(filepath):
    """Reads variable names from a file"""
    # vars dict structure: {variable_name: {variable_value: <>, isOptional: <>}}
    vars = {}
    with open(filepath, 'r') as f:
        for env_var in f.read().splitlines():
            if env_var:
                # get variable name and value
                if SEPARATOR in env_var:
                    env_name, env_value = map(str.strip, env_var.split(SEPARATOR, maxsplit=1))
                else:
                    env_name = env_var.strip()
                    env_value = ''

                # get and remove 'is optional' from name
                isOptional = IS_OPTIONAL_STR in env_name
                if isOptional:
                    env_name = env_name.replace(IS_OPTIONAL_STR, '').strip()

                vars.setdefault(env_name, {'value': env_value, 'optional': isOptional})

    return vars

def check_env_var_names(file_path_env, file_path_tamplate):
    """Checks the presence of variables in a file according to a given pattern"""
    if check_file_exists(file_path_env) and check_file_exists(file_path_tamplate):
        env_vars_names = read_vars_from_file(file_path_env)
        env_vars_names_template = read_vars_from_file(file_path_tamplate)

        env_vars_empty = []
        for env_var in env_vars_names_template:
            if not env_var in env_vars_names:
                if not env_vars_names_template[env_var]['optional']:
                    env_vars_empty.append(env_var)

        if env_vars_empty:
            print("The values of variables are required:")
            for _ in env_vars_empty:
                print(_)

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, help='File template for environment vars names')
    parser.add_argument('-e', '--env', type=str, help='File for checking with environment vars names')
    parser.add_argument('-s', '--sep', type=str, help='Separator to separate a variable name and value')
    parser.add_argument('-o', '--optional_str', type=str, help='String to indicate optional variable in template')

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.sep:
        SEPARATOR = namespace.sep
    if namespace.optional_str:
        IS_OPTIONAL_STR = namespace.optional_str
    check_env_var_names(namespace.env, namespace.template)