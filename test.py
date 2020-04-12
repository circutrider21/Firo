from Firo import FiroDB

car = FiroDB.Start("Hey.db")

car.set("memo", "Hello")

print(car.get("memo"))
