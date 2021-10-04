w= float(input('weight(kg)='))
h= float(input('height(m)='))

BMI= w/(h*h)
print(BMI)

if BMI<18.5:
    print('underweight')
elif BMI>=18.5 and BMI<25:
    print('normal')
elif BMI>=25 and BMI<30:
    print('overweight')
elif BMI>=30 and BMI<35:
    print('obese')
elif BMI>=35:
    print('extremely obese')