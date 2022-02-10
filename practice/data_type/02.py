h_cm = float(input('身長を入力してください(cm) > '))
w_kg = float(input('体重を入力してください(kg) > '))
bmi = w_kg / (h_cm/100)**2
print('BMI = {}'.format(bmi))