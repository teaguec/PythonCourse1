time = int(input("Enter total race time"))
pit_stop_number = int(input("How many pit stops were there?"))
avg_stop_duration = int(input("Average pit stop duration?"))

total_pitstop_time = pit_stop_number * avg_stop_duration
percentage = f"{((total_pitstop_time / time) * 100): .2f}"

print(percentage)
