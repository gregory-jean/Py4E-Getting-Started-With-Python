# Accept hours input and convert to float
shrs = input("Enter hours: ")
ihrs = float(shrs)

# Accept rate of pay input and convert to float
srate = input ("Enter rate of pay: ")
irate = float(srate)

# Calculate and display pay amount
pay = ihrs * irate
print("Pay:", pay)