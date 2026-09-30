# set(): 중복을 허용하지 않는 자료 구조

# 선언: set()
# add(), update(), remove()
# 합집합(union: |), 교집합(intersecton: &), 차집합(difference: -)

# 빈 셋을 선언
empty_set = set()

num_set = {1, 2, 3, 4}
num_two = {3, 4, 5, 6}
print(num_set)

num_set.add(2)
print(num_set)

# 합집합
union_r = num_set.union(num_two)
print(union_r)
print(num_set | num_two)

# 교집합
inter_r = num_set.intersection(num_two)
print(inter_r)

# 차집합
diff_r = num_set.difference(num_two)
print(diff_r)
