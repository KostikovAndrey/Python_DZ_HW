def is_year_leap(year):
    return year % 4 == 0


year_to_check = 2024

result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")

print(f"год 2023: {is_year_leap(2023)}")
print(f"год 2008: {is_year_leap(2008)}")
print(f"год 2009: {is_year_leap(2009)}")
print(f"год 2020: {is_year_leap(2020)}")
