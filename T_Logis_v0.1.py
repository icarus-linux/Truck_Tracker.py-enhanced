# Imports


# Greetings or message templates
greetMessage = "---- welcome to truck tracker v0.1 ----"

print(greetMessage)


# Questions

driverInfo = input("What is the drivers name: ")
truckIDInfo = input("What is the truck ID: ")
routeInfo = input("What is the route beign taken (eg. x to y): ")
minTempInfo = input("What is the minimum temp that the truck may reach: ")
maxTempInfo = input("What is the max temp that the truck may reach: ")
startTime = input("What time did the route start(This includes date): ")
finishTime = input("What time did the route finish(this includes date): ")



# Print the results

print(
    driverInfo,
    truckIDInfo,
    routeInfo,
    minTempInfo,
    maxTempInfo,
    startTime,
    finishTime,
    sep="\n"
)

# Choose destination

file_path = input("Please enter the file path where you want to save the file: ")


# Writes to file with info

with open("TRI.txt", "w") as file:
    file.write(f"Driver name: {driverInfo}\n")
    file.write(f"Truck ID: {truckIDInfo}\n")
    file.write(f"Route: {routeInfo}\n")
    file.write(f"Minimum temperature: {minTempInfo}\n")
    file.write(f"Maximum temperature: {maxTempInfo}\n")
    file.write(f"Start time: {startTime}\n")
    file.write(f"Finish time: {finishTime}\n")

print("Information saved to TRI.txt")




