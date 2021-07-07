print('welcome to grade calculator')
maths_mark = input('input a maths mark')
chemistry_mark = input('input a chemistry mark')
physics_mark = input('input a physics mark')
total_mark = (int(maths_mark) + int(chemistry_mark) + int(physics_mark) )/ 3
if total_mark < 40:
    print('You failed')
elif total_mark >= 70:
    print('A')
elif total_mark >= 60:
    print('B')
elif total_mark >= 50:
    print('C')
else: 
    print('D')