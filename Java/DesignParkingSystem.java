/** 
Leetcode Problem #1603

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: 
big, medium, and small, with a fixed number of slots for each size.

- Assign parking space available values to the class variables (big,small,medium)
- map the car type input to the space size i.e by checking if car type is either big,medium or small
- if its one of the sizes then also check if there is more than 0 spaces and then decrement that space and return true either return false

Big O time Complexity: Soon
 */

class ParkingSystem {

    int big = 0;
    int small = 0;
    int medium = 0;
    public ParkingSystem(int big, int medium, int small) {
        // this is the spaces available for each size respectively 
        this.big = big;
        this.medium = medium;
        this.small = small;
    }
    
    public boolean addCar(int carType) {
        if (carType == 1 && this.big > 0) {
            this.big--;
            return true;
        }
        else if (carType == 2 && this.medium > 0) {
            this.medium--;
            return true;
        }
        else if (carType == 3 && this.small > 0) {
            this.small--;
            return true;
        }
        else {
            return false;
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */