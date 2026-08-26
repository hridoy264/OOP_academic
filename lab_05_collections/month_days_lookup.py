
month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


user_month = input("Enter a month name: ").strip().title()
print("Days in a month:")
if user_month in month_days:
    print(f"There are {month_days[user_month]} days in {user_month}.\n")
else:
    print("Invalid month name entered.\n")


print("Sorted by alphabetical order: ")
sorted_months = sorted(month_days.keys())
for month in sorted_months:
    print(month)
print()


print("Months containing 31 days: ")
for month, days in month_days.items():
    if days == 31:
        print(month)
print()

print("Sorted by number of days in a month: ")
sorted_by_days = sorted(month_days.items(), key=lambda x: x[1])

for month, days in sorted_by_days:
    print(f"{month}: {days} days")