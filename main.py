import yaml,boto3

# TO-DO
# 1. Argparse cli flags?

# 2. read and parse build.y[a]ml file
# 3. return a dict. with the ssm parameter names and corresponding TF_VAR name


def extract_ssm_vars(yamlfile):
    """Return a dictionary of key/values defined under the parameter-store section of the input yaml file"""
    ssm_vars = yaml.safe_load(yamlfile)['env']['variables']['parameter-store']
    return ssm_vars

# 4. Use boto to get the decrypted values of the ssm-parameters
# 5. Print the strings to be eval in the shell


def print_ssm_vars(dictionary):
    terminal_output = ""
    for key, value in dictionary.items():
        terminal_output += f'export {key}={value}\n'
    return terminal_output
