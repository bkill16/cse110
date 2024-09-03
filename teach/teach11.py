print()

with open("hr_system.txt") as hr_file:

    for data in hr_file:
        clean_line = data.strip()
        parts = clean_line.split()

        name = parts[0]
        id = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        paycheck = salary / 24

        if job_title.lower() == 'engineer':
            paycheck += 1000

        print(f"{name} (ID: {id}), {job_title} - ${paycheck:.2f}")

print()