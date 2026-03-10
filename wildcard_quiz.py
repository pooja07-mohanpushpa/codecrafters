# Wildcard Entry Quiz System

def check_eligibility(score):
    passing_score = 70
    
    if score >= passing_score:
        print("Access granted to the requested lesson.")
    else:
        print("Please complete previous lessons first.")


# Example quiz score
user_score = int(input("Enter quiz score: "))

check_eligibility(user_score)
