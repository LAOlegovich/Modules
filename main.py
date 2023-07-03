import datetime, time, tqdm

from application.db.people import get_employees

from application.salary import calculate_salary

if __name__ == "__main__":
    print(calculate_salary('january','programmer'), 
          f'\nвремя обращения: {datetime.datetime.now().__format__("%d.%m.%Y %H:%m:%S")}')
    
    for _ in  tqdm.tqdm(range(1,3), desc = 'время ожидания', unit= "шаг"):
        time.sleep(1)
        
    print(get_employees('programmer'), 
          f'\nвремя обращения: {datetime.datetime.now().__format__("%d.%m.%Y %H:%m:%S")}')


