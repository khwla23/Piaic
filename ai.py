def calculate_taxes(percent):
    def actual_tax(salary):
       return salary * percent
    return actual_tax


actual_tax_fn = calculate_taxes(0.30)
print(actual_tax_fn)
print(actual_tax_fn(100000))