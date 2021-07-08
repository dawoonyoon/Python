test1 = "Error is %d%%." % 98
print(test1)

#오른쪽 정렬
test2 = "%10s" % "hi1234"
print(test2)

#왼쪽 정렬
test3 = "%-10s" % "hi1234"
print(test3)

#소수점 자르는 방법
test4 = "%0.4f" % 3.42134234
print(test4)

#오른쪽 정렬 & 소수점 4자리 
test5 = "%10.4f" % 3.42134234
print(test5)
