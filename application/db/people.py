def get_employees(man_category):

    db = {'chief':['Alexander Petrov'], 'engineer':['Stepan Holodov', 'Artem Nerko'], 
          'cleaner':['Alena Moon','Anfisa Chehova'], 'programmer':['Indira Gandi','Stas Mikhailov']}
    return f"К категории <{man_category}> относятся {','.join(db.get(man_category))}"

if __name__ == "__main__":
    print('Этот вывод из модуля people.py')