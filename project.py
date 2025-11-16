class BMW:
    def show(self):
        print("BMW: Smooth luxury ride")
class Ferrari:
    def show(self):
        print("Ferrari: High-speed sports performance")
for car in (BMW(), Ferrari()):
    car.show()
