time_spent = []

def analize_time_average(time_spent):
    return sum(time_spent)/len(time_spent)
    
def analize_time_highest(time_spent):
    longest = time_spent[0]
    for i in range(0, len(time_spent), 1):
        if time_spent[i] >= longest:
            longest = time_spent[i]
    return longest

goal_amount = int(input("how many days would you like to practice for?"))

for x in range(0, goal_amount, 1):
    time_today = int(input("practiced minutes today:"))
    time_spent.append(time_today)
    print("nice work!")
    print("average amount:")
    print(analize_time_average(time_spent))
    print("highest amount:")
    print(analize_time_highest(time_spent))
