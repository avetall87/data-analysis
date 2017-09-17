import pandas as pd
import numpy as np
data = pd.read_csv("data/mlbootcamp5_train.csv", sep=";")

# common dataFrame
groupingGender = data.groupby('gender')

# Сколько мужчин и женщин ?
print('Сколько мужчин и женщин ?')

meanHeight = data['height'].mean()
menSign = 0
womenSign = 0

if data[data['gender'] == 1]['height'].mean() > meanHeight: menSign = 1; womenSign = 2
else: menSign = 2; womenSign = 1

print('Кол-во мужчин:',data[data['gender'] == menSign]['id'].count())
print('Кол-во жещин:',data[data['gender'] == womenSign]['id'].count())
print('\n')


# Кто в среднем чаще указывает, что употребляет алкоголь – мужчины или женщины?
print('Кто в среднем чаще указывает, что употребляет алкоголь – мужчины или женщины?')

alcCountMen = 0
alcCountWomen = 0

if groupingGender['gender'].mean().count() == 2:
    for rowNum, sub_df in groupingGender:
        average = sub_df['alco'].mean()
        if (sub_df['gender'].mean() == menSign):alcCountMen = average
        elif(sub_df['gender'].mean() == womenSign): alcCountWomen = average

if alcCountMen>alcCountWomen: print('мужчины')
else:print('женщины')

# Можно проще и посмотреть глазами на результат ;)
#print(data.groupby('gender')['alco'].mean())

print('\n')

#Во сколько раз (округленно) процент курящих среди мужчин больше, чем процент крящих среди женщин?
print('Во сколько раз (округленно) процент курящих среди мужчин больше, чем процент курящих среди женщин?')
percentMen = data[data['gender'] == menSign]['smoke'].mean()
percentWomen = data[data['gender'] == womenSign]['smoke'].mean()
print('Округлено больше в',np.round(percentMen/percentWomen).astype('int'),'раз')
print('\n')

# На сколько месяцев отличаются медианные значения возраста курящих и некурящих?
print('На сколько месяцев отличаются медианные значения возраста курящих и некурящих?')
noneSmokeMedian = data[data['smoke'] == 0]['age'].median()
smokeMedian = data[data['smoke'] == 1]['age'].median()
print('Примерно на:',np.round((noneSmokeMedian-smokeMedian)/365*12).astype('int'),'месяцев')
print('\n')

# Во сколько раз отличаются доли больных в двух сегментах, описанных в задании?
print('Во сколько раз отличаются доли больных в двух сегментах, описанных в задании?')
data['years'] = (data['age'] / 365).round().astype('int')
smokeMen_60_64_year = data[(data['gender'] == menSign) & (data['smoke'] == 1) & ((data['years'] >= 60) & (data['years'] < 65))]

first_subgroup = smokeMen_60_64_year[smokeMen_60_64_year['cholesterol'] == 1 & (smokeMen_60_64_year['ap_hi'] < 120)]['cardio'].mean()

second_subgroup = smokeMen_60_64_year[smokeMen_60_64_year['cholesterol'] == 3 & ((smokeMen_60_64_year['ap_hi'] >= 160) &
                                                                                 (smokeMen_60_64_year['ap_hi'] < 180))] ['cardio'].mean()

print('В',(second_subgroup/first_subgroup).round().astype('int'),'раза')

#Выберите все верные утверждения
print('Выберите все верные утверждения. BMI')
data['bmi'] = data['weight'] / ((data['height']/100)*(data['height']/100))
medianMbi = data['bmi'].median()
print('Медиана mbi:',medianMbi,'норма от 18.5 до 25')

print('bmi у жунщин(1) и мужчин(2):')
print(data.groupby('gender')['bmi'].median())

print('У здоровых(0) в среднем BMI выше, чем у больных(1)')
print(data.groupby('cardio')['bmi'].median())

print('В сегменте здоровых и непьющих мужчин BMI ближе к норме, чем в сегменте здоровых и непьющих женщин')
print(data.groupby(['gender','alco','cardio'])['bmi'].median())

print('Сколько процентов данных было выброшено в процессе чистки?')
garbage = data[(data['ap_lo']  <= data['ap_hi']) &
               (data['height'] >= data['height'].quantile(0.025)) &
               (data['height'] <= data['height'].quantile(0.975)) &
               (data['weight'] >= data['weight'].quantile(0.025)) &
               (data['weight'] <= data['weight'].quantile(0.975))]

print('Было выброшено:',100.0 - np.round((garbage.shape[0] / data.shape[0])*100),'%')