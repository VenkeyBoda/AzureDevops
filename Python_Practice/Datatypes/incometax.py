"""
incometax.py

this program is calculate the income tax based on the anual income

## Income Tax Slabs in India (Tabular Format) – FY 2025-26 (AY 2026-27)

| Income Range (₹)           | Tax Rate (%) |
|----------------------------|--------------|
| Up to 4,00,000             | 0            |
| 4,00,001 – 8,00,000        | 5            |
| 8,00,001 – 12,00,000       | 10           |
| 12,00,001 – 16,00,000      | 15           |
| 16,00,001 – 20,00,000      | 20           |
| 20,00,001 – 24,00,000      | 25           |
| Above 24,00,000            | 30           |

"""

anual_income = int(input("Enter the anual income: "))

if anual_income <= 400000:
    print("tax is nil")
elif 400001 <= anual_income <= 800000:
    print("tax is 5%")   
elif 800001 <= anual_income <= 1200000:
    print("tax is 10%")
elif 1200001 <= anual_income <= 1600000:
    print("tax is 15%")  
elif 1600001 <= anual_income <= 2000000:
    print("tax is 20%")
elif 2000001 <= anual_income <= 2400000:
    print("tax is 25%") 
elif anual_income <= 2400000:
    print("tax is 30%")         
else:
    print("enter the correct anual income ")
