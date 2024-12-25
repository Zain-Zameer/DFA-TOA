# # -------- getting letters ---------
# print("GETTING LETTERS FROM DOCUMENT :>: ")
# f_getFirstLine = open("transTable.txt")
# f_line_getFirstLine = f_getFirstLine.readline()
# f_line_getFirstLine = f_line_getFirstLine.strip()
# f_line_getFirstLine = f_line_getFirstLine.replace(' ','')
# for i in range(0,len(f_line_getFirstLine)):
#     print(f_line_getFirstLine[i])
# print("\n")
# # -------- getting states -----------
# print("GETTING STATES FROM DOCUMENT :>: ")
starting_state = None
Ending_states = []

f = open("transTable.txt")
lines = f.readlines()[1:]
lines = [line for line in lines if line.strip()]

for i in range(0,len(lines)):
    if(lines[i][3]=='-'):
        starting_state = lines[i][0:2]
    elif(lines[i][3]=='+'):
        Ending_states.append(lines[i][0:2])

print("Starting state: "+starting_state)
print("Ending states: "+str(Ending_states))
# print("\n")
# # ----------- getting rules of a table ------------
# print("GETTING RULES FROM DOCUMENT :>: ")
rules = {}
f = open("transTable.txt")
lines = f.readlines()[1:]
lines = [line for line in lines if line.strip()]
for line in lines:
    if len(line) > 5: 
        current_state, input_symbol, next_state = line.split()
        if current_state not in rules:
            rules[current_state] = {}
        rules[current_state][input_symbol] = next_state
print(rules)

# ---- Fetching strings from token.txt ----
print("\n\n")
fetched_strings = []
token = open("token.txt")
token = token.readlines()
for i in range(0,len(token)):
    fetched_strings.append(token[i].strip())
print(fetched_strings)
print("\n")
print("current step:\n")
for i in range(0,len(fetched_strings)):
    current_state = starting_state
    current_rule = {}
    for j in range(0,len(fetched_strings[i])):
        current_letter = fetched_strings[i][j]
        for key,value in rules.items():
            if(key==current_state):
                current_rule = value
        for item,value in current_rule.items():
            if(current_letter==item):
                current_state = value
    if(current_state in Ending_states):
        print(f"{fetched_strings[i]} (Accepted)")
    else:
        print(f"{fetched_strings[i]} (Rejected)")


# Sample

# current_state = starting_state
# print(current_state)
# current_rule = {}
# current_letter = "b"
# for key,value in rules.items():
#     if(key==current_state):
#         current_rule = value
# # print(current_rule)
# for item,value in current_rule.items():
#     if(current_letter==item):
#         current_state = value
# print(current_state)
