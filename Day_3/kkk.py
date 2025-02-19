#Solution_1
#strip: remove spaces
#get:
#join
def print_specific_values(data):
    keys_input = input("Enter the keys you want to display (separated by commas): ")
    keys = [key.strip() for key in keys_input.split(',')]

    values = [str(data.get(key)) for key in keys]
    print(values)

data = {'ahmed': 190, 'omnia': 173, 'fatma': 189, 'alaa': 187}
print_specific_values(data)

##############################################
#Solution_2
#fromkeys
data = {'ahmed': 190, 'omnia': 173, 'fatma': 189, 'alaa': 187}
keys =('ahmed', 'omnia')

dataa = data.fromkeys(keys)
print(dataa)