import random
from datetime import timedelta


def generate_random_date(start_date, end_date):
  date_range = end_date - start_date
  
  random_days = random.randint(0, date_range.days)
  random_date = start_date + timedelta(days=random_days)
  return random_date

def generate_licence_plate():
  chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  nums = '0123456789'
  
  return "".join([random.choice(chars) for i in range(3)]+[random.choice(nums) for i in range(3)]+[random.choice(chars) for i in range(2)])