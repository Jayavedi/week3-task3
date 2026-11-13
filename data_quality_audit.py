import pandas as pd

data = {
    "name": [
        "Arun", "Priya", "Kumar", "Divya",
        "Rahul", "Sneha", "Vijay", "Meena",
        "Ajay", "Kavya", "Ravi", "Anitha",
        "Suresh", "Deepa", "Manoj", "Lakshmi",
        "Arun", "Priya", "Karthik", "Nisha",
        "Gokul", "Swetha", "Hari", "Pooja",
        "Surya", "Ram", "Geetha", "Bala",
        "Sanjay", "Keerthi", "Mohan", "Divya"],

    "email": [
        "arun@gmail.com", None, "kumar@gmail.com",
        "divya@gmail.com", None, "sneha@gmail.com",
        "vijay@gmail.com", None, "ajay@gmail.com",
        "kavya@gmail.com", None, "anitha@gmail.com",
        "suresh@gmail.com", None, "manoj@gmail.com",
        "lakshmi@gmail.com", "arun@gmail.com", None,
        "karthik@gmail.com", "nisha@gmail.com",
        None, "swetha@gmail.com", "hari@gmail.com",
        None, "surya@gmail.com", "ram@gmail.com",
        None, "bala@gmail.com", "sanjay@gmail.com",
        None, "mohan@gmail.com", "divya@gmail.com"],

    "city": [
        "Chennai", "chennai", "CHENNAI ", "Madurai",
        "madurai", "CHENNAI", "Coimbatore", "coimbatore",
        "Salem", " SALEM ", "Chennai", "Trichy",
        "TRICHY", "Madurai", "Chennai", "salem",
        "Chennai", "chennai", "Coimbatore", "CHENNAI",
        "Madurai", "Salem", "Trichy", "Chennai",
        "coimbatore", "MADURAI", "Salem", "Chennai",
        "Trichy", "Madurai", "CHENNAI", "chennai"],

    "age": [
        25, 30, 35, -5, 28, 250, 40, 32,
        22, 29, 31, 45, 38, 26, 33, 27,
        25, 30, 36, 24, 42, 29, 34, 31,
        28, 39, 41, 23, 37, 26, 32, 35],

    "phone": [
        "9876543210", "987654321", "9876543210",
        "12345", "9876543210", "9876543210",
        "9876543210", "98765", "9876543210",
        "9876543210", "9876543210", "12345678901",
        "9876543210", "9876543210", "98765",
        "9876543210", "9876543210", "987654321",
        "9876543210", "9876543210", "12345",
        "9876543210", "9876543210", "9876543210",
        "9876543210", "9876543210", "9876543210",
        "9876543210", "9876543210", "9876543210",
        "9876543210", "9876543210"]}

df = pd.DataFrame(data)


print("\nMISSING VALUES")

print(df.isna().sum())


print("\nMISSING PERCENTAGE")

missing_percentage = (df.isna().sum() / len(df)) * 100

print(missing_percentage.round(2))



print("\nDUPLICATE CUSTOMERS")

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)

print(df[df.duplicated()])



print("\nINVALID AGES")

invalid_age = (df["age"] < 0) | (df["age"] > 120)

invalid_age_count = invalid_age.sum()

print("Invalid age count:", invalid_age_count)


print(df[invalid_age])



print("\nBEFORE CITY CLEANING")

print(df["city"].unique())


df["city"] = df["city"].str.strip().str.title()

print("\nAFTER CITY CLEANING")

print(df["city"].unique())



print("\nBEFORE REMOVING DUPLICATES")

print("Total rows:", len(df))


df = df.drop_duplicates(subset=["name"], keep="first")

print("\nAFTER REMOVING DUPLICATES")

print("Total rows:", len(df))

# STEP 13: Fix Invalid Ages

print("\nBEFORE FIXING INVALID AGES")

print(df[df["age"] < 0])
print(df[df["age"] > 120])


invalid_age = (df["age"] < 0) | (df["age"] > 120)


df.loc[invalid_age, "age"] = pd.NA

print("\nAFTER FIXING INVALID AGES")

print("Invalid ages fixed:", invalid_age.sum())

print(df[df["age"].isna()])



print("\nPHONE NUMBER VALIDATION")

df["phone_valid"] = (
    df["phone"]
    .astype(str)
    .str.fullmatch(r"\d{10}"))

print(df[["name", "phone", "phone_valid"]])

print("\nINVALID PHONE NUMBERS")

print("Invalid phone count:", (~df["phone_valid"]).sum())

print(df[df["phone_valid"] == False])



df.to_csv("customers_clean.csv", index=False)

print("\nCLEANED DATA SAVED SUCCESSFULLY!")

print("File name: customers_clean.csv")



print("\nBEFORE AND AFTER SUMMARY")

print("Rows before:", 32)
print("Rows after:", len(df))

print("Duplicates removed:", 3)
print("Invalid ages fixed:", 2)

print("Missing emails:", df["email"].isna().sum())

print("Invalid phone numbers:", (~df["phone_valid"]).sum())



print("\nDATA QUALITY REPORT")

print("1. The original dataset contained 32 customer records.")

print("2. Missing email addresses were identified and flagged.")

print("3. Three duplicate customer records were removed.")

print("4. Two invalid age values were replaced with missing values.")

print("5. City names were standardised and six invalid phone numbers were flagged.")