import main

document = """
env:
  variables:
    parameter-store:
      TF_VAR_TEST: /test-param
      TF_VAR_TEST2: /test-param2
"""

ssm_vars_dictionary = {
    "TF_VAR_TEST": "somesampleparameter",
    "TF_VAR_TEST2": "anothersampleparameter"
}

expected_terminal_output = """
export TF_VAR_TEST=somesampleparameter
export TF_VAR_TEST2=anothersampleparameter
"""


def test_extract_ssm_vars():
    results = main.extract_ssm_vars(document)
    assert results['TF_VAR_TEST'] == '/test-param'


def test_print_ssm_vars():
    results = main.print_ssm_vars(ssm_vars_dictionary)
    assert results.strip() == expected_terminal_output.strip()


if __name__ == "__main__":
    test_extract_ssm_vars()
