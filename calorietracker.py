class CalorieTracker:
    def __init__(self):
       
        self.food_log = []

    def add_food(self, food_name, calories):
        self.food_log.append({"food": food_name, "calories": calories})
        print(f"Added: {food_name} - {calories} calories")

    def view_log(self):
        if not self.food_log:
            print("No food items recorded.")
            return
        print("Food Log:")
        for entry in self.food_log:
            print(f"{entry['food']} - {entry['calories']} calories")

    def total_calories(self):
        total = sum(entry["calories"] for entry in self.food_log)
        print(f"Total calories consumed: {total} calories")

def main():
    tracker = CalorieTracker()
    
    while True:
        print("\n--- Calorie Tracker ---")
        print("1. Add Food")
        print("2. View Log")
        print("3. Total Calories")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            food_name = input("Enter food name: ")
            try:
                calories = int(input("Enter calories: "))
                tracker.add_food(food_name, calories)
            except ValueError:
                print("Please enter a valid calorie amount.")
        elif choice == '2':
            tracker.view_log()
        elif choice == '3':
            tracker.total_calories()
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
