from CarsList import cars

def list_cars():
    for car in cars:
        model = car["models"]
        print(model)
        #print(f'{car["brand"]}\nModels: {car["models"]}\nSlogans: {car["slogans"]} \n')

def query_car():
    query_brand = input("Enter the brand of the car you want to search for: ")
    
    found_cars = [car for car in cars if query_brand.lower() in car["brand"].lower()]
    
    if found_cars:
        print(f"Found {len(found_cars)} matching cars:")
        print(found_cars)
        #for car in found_cars:
            #print(f"\nCar: {car['brand']}\nModels: {', '.join(car['models'])}\nSlogans: {car['slogans']}\nPrep Time: {car['prep_time']} minutes\n")
    else:
        print("No matching cars found.")

def find_cars_by_models(available_models):
    matching_cars = []
    for car in cars: 
        model  = car['models']
        if (model in available_models):
            matching_cars.append(car)
    return matching_cars

def main():
    print("Welcome to the car Book CLI Application!")
    
    while True:
        print("\nChoose an option:")
        print("1. List cars")
        print("2. Query cars")
        print("3. Search by models")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            list_cars()
        elif choice == "2":
            query_car()
        elif choice == "3":
            available_models = input("Enter the models you have (comma-separated): ").split(',')
            available_models = [model.strip() for model in available_models]
            print(available_models)
            matching_cars = find_cars_by_models(available_models)
            
            if matching_cars:
                print("You can make the following cars:")
                for car in matching_cars:
                    print(car['brand'])
            else:
                print("No cars found with the given models.")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()