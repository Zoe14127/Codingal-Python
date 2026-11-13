def total(bill_amount, tip_perc):
    # Calculate final bill after adding tip
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print("Please pay $", total)
    return total
total(150, 20)

def seating(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating(guests - 1)
print(seating.__doc__)

print("Seating arrangements for guest 1 is", seating(1))
print("Seating arrangements for guest 2 is", seating(2))
print("Seating arrangements for guest 3 is", seating(3))
print("Seating arrangements for guest 4 is", seating(5))