def twoStrings(s1, s2):
  # go through each character in the first string, and store it in a dictionary
  # key = letter, value = boolean
  # set comprehension string_set={let for let in s1}
    string_set = {let for let in s1}
    for letter in s2:
        if letter in dic:
            return "YES"
    return "NO"


def twoStrings(s1, s2):
  count = 0
  s1_subs = get_substrings(s1)

  s2_subs = get_substrings(s2)

  for sub in s1_subs:
    if sub in s2_subs:
      count += 1

  return count
  # create a set of all substrings in s1


def get_substrings(s):
  # range([start], stop[, step])
  subs = set()
  for start in range(len(s)):
    for end in range(start+1, len(s)+1):
      subs.add(s[start:end])

  return subs



s1 = "pancakes"
s2 = "bake"

# a k e ak ke ake
print(twoStrings(s1,s2))
