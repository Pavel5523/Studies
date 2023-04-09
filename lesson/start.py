import geometry.rect

r1 = RecTangle(1, 2)
r2 = RecTangle(3, 4)
# print(r1.get_per_rect(), r2.get_per_rect())

s1 = Square(10)
s2 = Square(20)
# print(s1.get_per_sq(), s2.get_per_sq())

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_per())