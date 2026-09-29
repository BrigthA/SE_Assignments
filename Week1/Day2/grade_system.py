
while True:
    mark_input = input("\nEnter your mark (between 0 and 100, or q to quit): ").strip() #strip() removes any leading or trailing whitespace from the input
    if mark_input.lower() == "q":
        break

    try:
        mark = int(mark_input)
        if mark < 0 or mark > 100:
            raise ValueError("\nMark must be between 0 and 100")
    except ValueError as e:
        print(e)
        continue

    if mark >= 90:
        print(f"\nMark : {mark} -> Your grade is A") # print(f"Mark : {mark}") uses an f-string to format the output, which allows you to include variables directly in the string.
    elif mark >= 80:
        print(f"\nMark : {mark} -> Your grade is B")
    elif mark >= 70:
        print(f"\nMark : {mark} -> Your grade is C")
    elif mark >= 60:
        print(f"\nMark : {mark} -> Your grade is D")
    else:
        print(f"\nMark : {mark} -> Your grade is E")