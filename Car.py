name = ["Martin","Hanne","Bob","Jennifer","Henrik","Oda","Karle","Lillan","Marit","Eple"]
location = ["Elverum","Elverum","Oslo","Oslo","Lier","Lier","Lier","Elverum","Oslo","Lier"]
age = [18,24,35,45,32,12,19,50,50,34]

bronnoysund_dictionary = list(zip(location,name, age))
#this is kind of the info as I expect to be able to harvest from a database

elverum_dictionary = bronnoysund_dictionary
list(zip(elverum_dictionary(location("Elverum"),name,age)))

print(elverum_dictionary)