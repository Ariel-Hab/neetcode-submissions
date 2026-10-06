class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(key= lambda x: x[0])
        new_car = cars.pop()
        front_fleet =(target-new_car[0])/new_car[1]
        fleets = 1
        while cars:
            new_car = cars.pop()
            new_fleet = (target-new_car[0])/new_car[1]
            if(new_fleet > front_fleet): #va a demorar mas, por lo que va a llegar despues
                front_fleet = new_fleet
                fleets += 1
        return fleets
                    

            