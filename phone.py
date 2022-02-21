import PhoneClass as pc


def main():
    my_phone = pc.Phone("Apple", "X", 1000)

    print("The manufacturer of the phone is: ", my_phone.get_manufact())
    print("The model of the phone is: ", my_phone.get_model())
    print("The retail price of the phone is: ", my_phone.get_retail_price())

    my_phone.set_manufact("Samsung")
    my_phone.set_model("Y")
    my_phone.set_retail_price(500)

    print("The manufacturer of the phone is now: ", my_phone.get_manufact())
    print("The model of the phone is now: ", my_phone.get_model())
    print("The retail price of the phone is now: ", my_phone.get_retail_price())


# Call the main function.
main()
