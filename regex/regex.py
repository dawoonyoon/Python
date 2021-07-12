
# 주소록에서, 전화번호만 찾는 정규표현식
regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'

# 주소록
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드
import re
result = re.findall(regex, search_target)
print("\n".join(result))


"""
\d => digit
\w => a, b, c, 가, 나, 다, 1, 2 와 같은 문자와 숫자를 포함
    특수문자를 포함하지는 않지만, _는 포함
"""
