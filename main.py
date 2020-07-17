#message
#Function that prints our story with user input
def M(animal,borough,action,food):
  
  my_story = """
  Hello There! Welcome to our zoo!
  
  Let us tell you about a {0},
  who once lived in the borough of {1}. 
  It loved to {2} with it's favorite food,
  which is {3}, instead of eating it right away.
  Everyone loved the {0}.
  But he only loved to eat {3}. 
  He never shared his {3} with any other animals.
  All the animals were now angry with the {0}.

  So, the {0} became lonely. 
  Kids share your {3} with your friends

   """.format(animal,borough,action,food)
  
  print(my_story)

a= input("Enter your Favorite Animal: ")
b= input("Enter your Borough: ")
c= input ("Enter an Action: ")
d= input ("Enter your Favourite Food: ")

M(a,b,c,d)

