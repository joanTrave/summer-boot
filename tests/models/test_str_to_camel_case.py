from summer.models.camel.str_to_camel_case import str_to_camel_case


def test_str_to_camel_case():
    no_camel_input: str = "A_new fr1end"
    camel_cased_expected_output: str = "aNewFr1end"
    assert str_to_camel_case(no_camel_input) == camel_cased_expected_output
