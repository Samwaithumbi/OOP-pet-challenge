from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet("Bruno")

    # Display initial status
    my_pet.get_status()

    # Perform actions
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()

    # Teach some tricks
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("Fetch")

    # Show tricks learned
    my_pet.show_tricks()

    # Final status
    my_pet.get_status()

if __name__ == "__main__":
    main()
