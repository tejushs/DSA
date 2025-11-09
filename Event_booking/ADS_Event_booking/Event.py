n = int(input("Enter total number of slots available per day:"))


institutions = {}
num_instituation = int(input("Enter number of institutions: "))

for i in range(num_instituation):
    name = input(f"Enter name of institution {i+1}: ")
    total_students = int(input(f"Enter total number of students in {name}: "))
    institutions[name] = {
        'total': total_students,
        'max_per_day': total_students // 2, # 50% limit per day
        'students' : []  #to store registered sutdents
    }



    days ={
        'Day1': {'remaining':n,'students':[]},
        'Day2': {'remaining':n,'students':[]},
        'Day3': {'remaining':n,'students':[]}
    }


print("\nRegistration Process Begins:\n")

num_students = int(input("Enter total number of students registering: "))

for i in range(num_students):
    print(f"\n Student {i+1}:")
    name = input("Enter Student name: ")
    reg_no = input("Enter Registration number: ")
    inst = input("Enter Institution name: ")
    pref_day = input("Enter preferred day (Day1/Day2/Day3): ")


    #check if preferred day has a slot and within institution limit
    if (days[pref_day]["remaining"] > 0 and
            len([s for s in days[pref_day]["students"] if s['institution'] == inst]) < institutions[inst]["max_per_day"]):
        
            allocated_day = pref_day  # allocate preferred day
    else:
        # Find an alternate day with available slots
        allocated_day = None
        for d in days:
            if (days[d]["remaining"] > 0 and
                len([s for s in days[d]["students"] if s['institution'] == inst]) < institutions[inst]["max_per_day"]):
                allocated_day = d
                break


    # If still no day available
    if not allocated_day:
        print("No slots available for this student.")
        continue


# Add student details to allocated day and institution
studeent = {"name": name, "reg_no": reg_no, "institution": inst , "day": allocated_day}
days[allocated_day]["students"].append(studeent)


print
(f"Student {name} allocated to {allocated_day}.")


# display

print("\n--- DAY-WISE ALLOCATIONS ---")
for d in days:
    print(f"\n{d} ({n - days[d]['remaining']} students):")
    for s in days[d]["students"]:
        print(f"  {s['name']} ({s['reg_no']}) - {s['institution']}")


 # instituation wise details
 # 
print("\n--- INSTITUTION-WISE DETAILS ---")
for inst in institutions:
    print(f"\nInstitution: {inst}")
    for d in ["Day1", "Day2", "Day3"]:
        day_students = [s for s in institutions[inst]["students"] if s["day"] == d]
        print(f"  {d}: {len(day_students)} students")
        for s in day_students:
            print(f"    {s['name']} ({s['reg_no']})")       