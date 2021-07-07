def grade_calc(maths_mark, chemistry_mark, physics_mark):
    total_mark = (int(maths_mark) + int(chemistry_mark) + int(physics_mark) )/ 3
    if total_mark < 40:
        return 'You failed'
    elif total_mark >= 70:
        return 'A'
    elif total_mark >= 60:
        return 'B'
    elif total_mark >= 50:
        return 'C'
    else: 
        return 'D'
if __name__ == "__main__":
    print('welcome to grade calculator')
    maths_mark = input('input a maths mark')
    chemistry_mark = input('input a chemistry mark')
    physics_mark = input('input a physics mark')