import math
# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase

def earn_points(price):
    whole_dollars = int(price)
    points = whole_dollars * 3
    return points

# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
def tier_label(points):
    if points < 100:
        return "Bronze"
    elif points >= 100 and points < 500:
        return "Silver"
    else:
        return "Gold"

# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
purchases = [12.50, 34.20, 299.99]
total_points = 0
for purchase in purchases:
    total_points += earn_points(purchase)

# 4. After the loop, call tier_label(total_points)
tier = tier_label(total_points)
total_dollars = 0 
for cost in purchases:
    total_dollars += cost
print("Loyalty Summary")
print(f"Total dollars spent: {total_dollars}")
print(f"Total points earned: {total_points}")
print(f"Final tier: {tier}")
# # 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
