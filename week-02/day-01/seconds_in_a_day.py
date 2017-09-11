current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
all_seconds = 24*60*60
past_seconds = ((14*60*60) + (34*60) + 42)
print(str(all_seconds % past_seconds) + " seconds remaining from the day!" ) 