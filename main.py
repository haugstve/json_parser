from validate_input import Source
import json


def pretty_print(json_str):
    print(json.dumps(json.loads(json_str), indent=4))


with open("example.json") as input_file:
    input_payload = input_file.read()


test_input = Source.from_json(input_payload)
pretty_print(test_input.to_json())
