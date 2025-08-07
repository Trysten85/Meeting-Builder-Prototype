#data initiliazes the empty list 
data = []
#collects the data from the users 
def enter_availability():
    print("Enter participant availability data")
    while True:
        name = input("Enter participant name (enter 'done' to get best time): ")
        if name.lower() == 'done':
            break
        best_times = input("Enter best times ( ex: 9-10am,2-3pm): ")
        worst_times = input("Enter worst times ( ex: 12-1pm,4-5pm): ")
        participant = {
            'name': name,
            'best_times': [t.strip() for t in best_times.split(',')],
            'worst_times': [t.strip() for t in worst_times.split(',')]
        }
        data.append(participant)
#counts how often each time is mentioned
def calculate_best_time():
    time_counter = {}

    for participant in data:
        for time in participant['best_times']:
            time_counter[time] = time_counter.get(time, 0) + 1

    if time_counter:
        best_time = max(time_counter, key=time_counter.get)
        print(f"\nChosen Meeting Time: {best_time} with {time_counter[best_time]} vote(s)")
    else:
        print("No best times were given")
#collects the availibities and calculates and displays the most popular time that was picked the most often
def main():
    print("=== Frequency-Based Meeting Time Picker ===")
    enter_availability()
    calculate_best_time()
#calls the main function when you run the file 
if __name__ == "__main__":
    main()
