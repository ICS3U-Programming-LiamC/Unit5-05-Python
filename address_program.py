#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 7, 2021
# This program gets an address and then transforms it into all caps
# and the right format


# function that does all the formating
def format_address(addressee_in_func, str_num_in_func,
                   str_name_in_func, postal_in_func, city_in_func,
                   prov_in_func, apt_num_in_func=None):

    # makes everything uppercase
    addressee_in_func = addressee_in_func.upper()
    str_name_in_func = str_name_in_func.upper()
    city_in_func = city_in_func.upper()
    prov_in_func = prov_in_func.upper()
    postal_in_func = postal_in_func.upper()
    # make a new postal code thats empty
    # probably wasnt neccessary
    new_postal_in_func = ""

    # for each in the postal code attatch it to the new postal
    # and put a space after the third character
    if (len(postal_in_func) == 6):
        for each in range(6):
            if each == 3:
                new_postal_in_func = (new_postal_in_func
                                      + " " + postal_in_func[each])
            else:
                new_postal_in_func = (new_postal_in_func
                                      + postal_in_func[each])
    else:
        new_postal_in_func = postal_in_func

    # make the long single stringed variable with all
    # the info in the right format
    if (apt_num_in_func == "" or apt_num_in_func is None):
        text = ("{} \n{} {} \n{} {}  {}"
                .format(addressee_in_func, str_num_in_func,
                        str_name_in_func, city_in_func,
                        prov_in_func, new_postal_in_func))
    else:
        text = ("{} \n{}-{} {} \n{} {}  {}"
                .format(addressee_in_func, apt_num_in_func,
                        str_num_in_func, str_name_in_func, city_in_func,
                        prov_in_func, new_postal_in_func))
    # return it
    return text


# main function
def main():
    # get all the inputs
    addressee = input("Who are you sending this to: ")
    str_num = input("what is the street number: ")
    str_name = input("what is the street name: ")

    apt_or_no = input("Do you have an apartment(y/n): ")
    if ((apt_or_no == 'y') or (apt_or_no == 'y')):
        apt_num = input("what is the apartment number: ")

    city = input("what is the city: ")
    prov = input("what is the province in the format of(ON, QC...): ")
    postal = input("what is the postal code: ")

    # call the address function with all the parameters
    if (apt_or_no != "y" and apt_or_no != "Y"):
        result = format_address(addressee, str_num, str_name,
                                postal, city, prov)
    else:
        result = format_address(addressee, str_num, str_name,
                                postal, city, prov, apt_num)
    # print the result
    print("\n")
    print(result)


if __name__ == "__main__":
    main()
