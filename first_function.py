def percentage_calculator(name, homework, assessment, final_exam):
    total = (int(homework) + int(assessment) + int(final_exam)
    breakpoints = [157, 131, 105, 78, 52, 26, 0]
    ranking = ['A','B','C','D','E','F','G']
    for rank, breakpoint in zip(ranking, breakpoints):
        if total >= breakpoint:
            return name, rank, percentage
    return name, percentage
print(percentage_calculator(input('what is your name?'), input('what is your homework score?'), input('what is your assesment score?'), input('what is your final exam score?')))
