#importing the random package, able to create psuedo random number for testing purposes
import random
#allows additional operations such as the itemgetter function
import operator
#allows the presentation of plots,graphs etc.. will be used to display agents
import matplotlib.pyplot
#imports the agentframework file which must be in the same directory to work, by importing this we can import the agent class.
import csv
#imports agentframework i in the same directory
import agentframework



#creates a new empty list for what will be the csv environment data
environment = []
agents = []
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

f = open('in.csv', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
     rowlist.append(value)
     environment.append(rowlist)
    
     
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.agent(environment, agents))
    
    
#check agents
for i in range(num_of_agents):
   print(agents[i]) 

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    
#check iterations
for i in range(num_of_agents):
   print(agents[i])        
        

matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()
#Extras!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



















"""To get this code to work in command prompt I had to navigate the correct directory using the cd filename command. The final code 
added in order to get this to work in command prompt was  python /model.py (200,20,30). Worked fine in Jupyter notebook"""


