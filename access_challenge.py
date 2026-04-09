# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors

#sets fastest for membership checks
revoked = {28, 5, 1, 90, 46, 33}
approved = []
denied = []

while True:
    name = input("Whats your name?")
    if(name.lower() != "done"):
        badge = int(input("What is your badge number?"))
        if badge in revoked:
            denied.append(name)
            print("ACCESS DENIED")
        else:
            approved.append(name)
            print("ACCESS GRANTED")
    else:
        print("Access Summary for ✅ Approved Visitors & ⛔️ Denied Visitors")
        print("-----------------------------------------------------------------")
        print(f"Approved: {sorted(approved)}")
        print(f"Total Approved: {len(approved)}")
        print(f"Denied: {sorted(denied)}")
        print(f"Total Denied: {len(denied)}")
        break
