
def calculate_salary(month, man_category):
    work_days_in_month = {'january':15, 'february':17, 'march':21,'april':20,'may':18,
                          'june':21, 'july':23,'august':22, 'september':20, 'october':21,
                          'november':20,'december':21}
    work_category = {'chief':50, 'cleaner':1,'engineer':8, 'programmer':12}

    return f"Зарплата составляет: {work_days_in_month.get(month.lower()) * work_category.get(man_category.lower())} рублей"

if __name__ == "__main__":
    print('Этот вывод из модуля salary.py')