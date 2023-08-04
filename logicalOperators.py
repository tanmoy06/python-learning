# if applicant has high income AND good credit thn he is Eligible for Loan
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

# NOT operator
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")