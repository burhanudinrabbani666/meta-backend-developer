# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1]
print(new_trial)


# recursion
def string_reversal(strings: str) -> str:
    if len(strings) == 0:
        return strings
    else:
        return string_reversal(strings[1:]) + strings[0]


new_str = "reversal"
reverse = string_reversal(new_str)
print(reverse)
