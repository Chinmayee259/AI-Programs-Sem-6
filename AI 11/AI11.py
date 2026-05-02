# AI 11. Implement any one of the following Expert System 
# I.Hospitals and medical facilities 
# II.Employee performance evaluation	
# III.Stock market trading

def medical_expert_system():
    print("Welcome to Medical Expert System 🏥")
    print("Answer the following questions with yes/no\n")

    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    pain = input("Do you have body pain? ").lower()
    injury = input("Do you have any injury? ").lower()

    print("\n--- Diagnosis ---")

    if fever == "yes" and cough == "yes":
        print("You may have a viral infection or flu.")
        print("Suggestion: Consult a physician and take rest.")

    elif fever == "yes" and pain == "yes":
        print("You may have dengue or viral fever.")
        print("Suggestion: Get blood test done immediately.")

    elif injury == "yes":
        print("You may need immediate medical attention.")
        print("Suggestion: Visit nearest hospital or emergency ward.")

    elif cough == "yes":
        print("You may have a throat infection.")
        print("Suggestion: Take warm fluids and consult doctor if needed.")

    else:
        print("You seem fine.")
        print("Suggestion: Maintain healthy lifestyle.")

# Run system
medical_expert_system()


# Welcome to Medical Expert System 🏥
# Answer the following questions with yes/no

# Do you have fever?  yes
# Do you have cough? yes
# Do you have body pain?  no 
# Do you have any injury? no

# --- Diagnosis ---
# You may have a throat infection.
# Suggestion: Take warm fluids and consult doctor if needed.