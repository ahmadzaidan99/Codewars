import re
def solution(s):
    if len(s)%2!=0:
        s += "_"
    return re.findall('..',s)
