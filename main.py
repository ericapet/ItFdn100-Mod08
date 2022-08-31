# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Erica Peterson,08/29/22,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
open('products.txt', 'a')
class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
    changelog: (date,name,change)
        2022/01/01, RRoot, Created Class
        2022/08/30, Erica Peterson, Modified code to complete assignment 8
    """
# -- Fields --
    product_name = ""
    product_price = 0
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)
    # -- Properties --
    @property
    def product_name(self):  # getter for product name
        return str(self.__product_name).title()  # Title case
    @product_name.setter
    def product_name(self, value):  # setter for product name
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product name cannot be numerical, please enter name using alphabetical characters only")
    @property
    def product_price(self):  # getter for price
        return float(self.__product_price)  # Numeric characters
    @product_price.setter
    def product_price(self, value):  # setter for price
        self.__product_price = value
    # -- Methods --
    def to_string(self):
        return self.__str__()
    def __str__(self):
        return self.product_name + "," + str(self.product_price)
# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Erica Peterson, 8.31.22,Modified code to complete class
    """
    # -- Methods --
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        with open(file_name, "r") as file:
            for line in file:
                data = line.split(",")
                row = Product(product_name=data[0].strip(),
                              product_price=data[1].strip())
                list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(name, price, list_of_rows):
        row = (str(name).strip(),
               str(price).strip(), "\n")
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        with open(file_name, "w") as file:
            for item in list_of_rows:
                file.write(str(item.product_name) + "," +
                           str(item.product_price) + "\n")
        file.close()
        print("\n\tData saved to products.txt file!")
        return list_of_rows
# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs inputs and outputs, including outputting a menu to the user, gaining their input for menu choice,
     outputting current data in file, and inputting data from the user
    """
    # -- Methods --
    @staticmethod
    def output_menu_tasks():
        """ Display a menu of choice to the user

        :return: nothing
        """
        print("""
    Menu of options
        1) Show current product data in file
        2) Add new product data
        3) Save product data to file
        4) Exit program
        """)
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        return choice
    @staticmethod
    def show_current_data(list_of_products):
        print("Here is what is currently in your products.txt file: ")
        for item in list_of_products:
            print("\t" + str(item.product_name) + ',' + '{0:.2f}'.format(item.product_price))
    @staticmethod
    def add_product():
        name = input("Enter the name of the product: ")
        price = input("Enter the price of the product: ")
        item = Product(product_name=name,
                       product_price=price)
        return item

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName,
                                                        lstOfProductObjects)

while True:
    # Show user a menu of options
    IO.output_menu_tasks()

    # Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':  # show current data
        IO.show_current_data(lstOfProductObjects)
        continue

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':  # add product
        lstOfProductObjects.append(IO.add_product())
        continue

        # let user save current data to file and exit program
    elif choice_str.strip() == '3':
                lstOfProductObjects = \
            FileProcessor.save_data_to_file(strFileName,
                                            lstOfProductObjects)
    elif choice_str.strip() == '4':
        print() # added for aesthetics
        print("Exiting program!")
        input()
        break

