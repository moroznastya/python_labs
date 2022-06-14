import re

result = re.findall("01/Jul/1995:03:39|4[0-9]|5[0-5]:00.+(gif|GIF)", open('access_log_Jul95', ).read())
print(f"gif: {len(result)}")
