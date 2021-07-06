def percentage_calculator(name,homework,assessment,final_exam):
    percentage = ((int(homework) + int(assessment) + int(final_exam))/ 175 ) * 100
    return name, percentage
print(percentage_calculator(input('what is your name?'), input('what is your homework score?'), input('what is your assesment score?'), input('what is your final exam score?')))
