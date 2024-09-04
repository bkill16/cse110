interest_year = input("\nEnter the year of interest: ")

overall_min = 9999
overall_max = -1

total_expectancy = 0
average_expectancy = 0
number_of_rows = 0

year_min = 9999
year_max = -1

with open("life-expectancy.csv") as life_expectancy_file:

    next(life_expectancy_file)

    for line in life_expectancy_file:

        clean_line = line.strip()
        
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        if life_expectancy > overall_max:
            overall_max = life_expectancy
            overall_max_entity = entity
            overall_max_year = year

        if life_expectancy < overall_min:
            overall_min = life_expectancy
            overall_min_entity = entity
            overall_min_year = year

        if year == interest_year:
            number_of_rows += 1
            total_expectancy += life_expectancy
            average_expectancy = total_expectancy / number_of_rows

            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_entity = entity

            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_entity = entity

print(f"\nThe overall max life expectancy is: {overall_max} from {overall_max_entity} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min} from {overall_min_entity} in {overall_min_year}")

print(f"\nFor the year {interest_year}:")
print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
print(f"The max life expectancy was in {year_max_entity} with {year_max}")
print(f"The min life expectancy was in {year_min_entity} with {year_min}\n")