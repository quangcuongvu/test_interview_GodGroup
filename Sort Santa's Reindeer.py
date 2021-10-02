list_name=["Dasher Tonoyan", 
  "Dancer Moore", 
  "Prancer Chua", 
  "Vixen Hall", 
  "Comet Karavani",        
  "Cupid Foroutan", 
  "Donder Jonker", 
  "Blitzen Claus"]

def lastname(name):
    name = name.split()
    return name[1]

    
def sort_reindeer(reindeer_names):
    reindeer_names.sort(key=lastname)
    return reindeer_names

 
print(sort_reindeer(list_name))