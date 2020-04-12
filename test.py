from Firo import FiroDB

car = FiroDB.Start("Hey.db")

car.set("memo", "Hello")
car.set("hey", "ho")
car.set("stop", "go")

print(car.get("memo"))
print(car.get("hey"))
print(car.get("stop"))
