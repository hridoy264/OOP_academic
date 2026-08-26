# error vs exceptions

# error --> Compile time er error
#       --> syntax, Indentation

# Exceptions --> Run time error
#           --> Indexing, key, value, zero division


try: # je code e exception thakte pare

    with open("name.txt", "r") as f:
        print(f.read())
    print(10/10)
    # x = int("abc")
    a = [1, 2, 3]
    # print(a[100])
    # x = abc

except ZeroDivisionError:
    print("Error: Division by Zero is not possible")
except ValueError:
    print("Invalid value!")
except FileNotFoundError:
    print("File Not Found")
except IndexError:
    print("Wrong index")
except Exception as e:
    print("Some error occured!!", e)
else:
    print("Code executed succesfully!")
finally:
    print("eta print hobei")

# custom error baniyechi
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are allowed")
    print("Valid File")

# check_file('data.csv') 

# custom error handling
try:
   check_file('data.csv')
except Exception as e:
    print(e)