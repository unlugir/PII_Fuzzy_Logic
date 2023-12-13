import numpy
import itertools
import mymodel


def map_range(value, from_min, from_max, to_min, to_max):
    # Check if the value is outside the source range
    if value < from_min:
        value = from_min
    elif value > from_max:
        value = from_max

    # Map the value from the source range to the target range
    from_range = from_max - from_min
    to_range = to_max - to_min

    scaled_value = (value - from_min) / from_range
    mapped_value = to_min + (scaled_value * to_range)

    return mapped_value

combinations = []

for item in mymodel.input_lvs["Walk"]:
    terms = list(item["terms"].keys())
    combinations.append(terms)

all_combinations = list(itertools.product(*combinations))

minimum = 10000
maximum = 0
for combo in all_combinations:
    s = sum(mymodel.input_lvs["Walk"][0]["terms"][combo[0]][1:])/10 \
        + sum(mymodel.input_lvs["Walk"][1]["terms"][combo[1]][1:])/200 \
        - sum(mymodel.input_lvs["Walk"][2]["terms"][combo[2]][1:])/10 * 0.5

    if (s < minimum):
        minimum = s
    elif (s > maximum):
        maximum = s

    print("(", combo,", (", s ,"))",",")

for rule in mymodel.rule_base:
    index = round(map_range(rule[1], minimum, maximum, 0, len(mymodel.output_lv["Walk"]["terms"]) - 1))
    index = len(mymodel.output_lv["Walk"]["terms"]) - 1 - index
    result = list(mymodel.output_lv["Walk"]["terms"].keys())[index]
    new_rule = list(rule)
    new_rule[1] = result
    print(tuple(new_rule),",")
