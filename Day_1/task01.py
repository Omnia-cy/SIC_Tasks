
name = input("Enter your name:")
age =  input("Enter your age:")
fav_movie = input("Enter your favorite movie:")
print (name , " is",str(age),"years old and loves watching",fav_movie)
# lines

name, age, fav_movie = input("Enter your name, age and favorite movie separated by a space: ").split()
print(name, " is", age, "years old, and loves watching",fav_movie)
# by spaces
