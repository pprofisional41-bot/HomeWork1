def is_balanced_recursive(s):
    brackets = {'(': ')', '{': '}', '[': ']'}

    def remove_pairs(s):
        if not s:
            return True


        for i in range(len(s) - 1):
            if s[i] in brackets and brackets[s[i]] == s[i + 1]:
                new_s = s[:i] + s[i + 2:]
                return remove_pairs(new_s)

        return s == ""

    return remove_pairs(s)

print(is_balanced_recursive("({})"))