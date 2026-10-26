s = input()
i = 0
result = ""
while i < len(s):
  if s[i] == ".":
    result +="0"
  elif s[i:i+2] =="-.":
    result += "1"
  else:
    result += "2"
print(result)