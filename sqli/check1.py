import random as rd
rules = {
    "booleanAttack":[
        [userid.partition(' ')[0],"booleanTrueExpr"],
    ],
     "numbers":[
      ["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["0"]
    ],
    "opOr": [
        ["or"],
    ],
    "booleanTrueExpr": [
        ["unaryTrue"],
        ["binaryTrue"]
    ],
    "unaryTrue": [
        ["terDigitOne","opEqual","terDigitOne","hyphen"],
        ["terDigitOne","opEqual","terDigitOne","wsp","hyphen"],
        ["numbers","opEqual","numbers","hyphen"]
     ],
    "binaryTrue":[
      ["parOpen","terDigitOne","opEqual","terDigitOne","parClose","hyphen"],
        ["parOpen","terDigitOne","opEqual","terDigitOne","parClose","wsp","hyphen"],
        ["parOpen","numbers","opEqual","numbers","parClose","hyphen"]
    ],
    "parOpen":[
      ["("]
    ],
    "parClose":[
      [")"]
    ],
    "wsp": [
        ["wsp1"],
        [" "]
    ],
    "wsp1":[
        ["wsp"],
        [" "]
    ],
    "terDigitOne": [
        ["1"]
    ],
    "opEqual":[
        ["="]
    ],
    "hyphen":[
        ["--"]
    ],

}
def generate_items(items):
    for item in items:
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem
        else:
            yield item

        # Our expansion algo
def expansion(start):
    for element in start:
        if element in rules:
            loc = start.index(element)
            start[loc] = rd.choice(rules[element])
        result = [item for item in generate_items(start)]

    for item in result:
        if not isinstance(item, list):
            if item in rules:
                result = expansion(result)

    return result


def to_string(result):
    return ' '.join(result)
boolean1=[]
for i in range(0,5000):
    # An example test you can run to see it at work
    result = ["booleanAttack"]
    # print(result) # Print our starting result
    result = expansion(result) # Expand our starting list
    boolean1.append(to_string(result))
print(boolean1)
# piggy1=[]
# piggy2=[]
# for i in range(0,5000):
#     # An example test you can run to see it at work
#     result = ["unionAttack"]
#     # print(result) # Print our starting result
#     result = expansion(result) # Expand our starting list
#     piggy1.append(to_string(result))
#     piggy2.append(to_string_nospace(result))
# print(piggy1)
# print(piggy2)

# x=
# if x in final:
#     print('found')
# else:
#     print('not found')# Print the final result

