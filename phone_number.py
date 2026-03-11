# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."


number = input("Enter US phone number in any format").strip()

for char in {"-", "(", ")", "."}:
    number = number.replace(char, " ")

split = number.split(" ")
joined = "".join(split)
if len(joined) == 10:
    digits1 = joined[0:3]
    digits2 = joined[3:6]
    digits3 = joined[6:]

    final_num = f"({digits1}) {digits2}-{digits3}"

else:
    print("Please enter exactly 10 digits.")

print(final_num)