#Created a program that lets users enter their locations and discover nearby attractions.

# Stores cities and their countries.
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# Stores a traveler's full name, destination, and interests. 
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
    """
    Get a destination's index.
    
    Parameters
    ----------
    destination: string
                 The destination.
    
    Returns
    -------
    destination_index: int
                       The destination's index.
    """
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    """
    Get a traveler's location.
    
    Parameters
    ----------
    traveler: list
              The traveler's name, location, and interests.
    
    Returns
    -------
    traveler_destination_index: int
                                The index of the traveler's location.
    """
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Stores attractions for each destination.
attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
    """
    Add an attraction to a destination.
  
    Parameters
    ----------
    destination: string
                 The destination.
    attraction: list
                The attraction and its tag or tags.
    """
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    """
    Find attractions for a specified destination and specified interests.
   
    Parameters
    ----------
    destination: string
                 The destination
    interests: string
               The traveler's interests.
  
    Returns
    -------
    attractions_with_interest: list
                               Attractions that match the traveler's interests.
    """
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
      possible_attraction = attraction
      attraction_tags = attraction[1]
      for interest in interests:
       if interest in attraction_tags:
          attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    """
    Find attractions based on a traveler's location and interests.
  
    Parameters
    ----------
    traveler: list
              A traveler's name, destination, and interests.
            
    Returns
    -------
    interests_string: string
                      A sentence that informs travelers of a destination's attractions that match their interests.
    """
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi, " + traveler[0] + ". We think you'll like these places around " + traveler[1] + ": " + str(traveler_attractions) + "."
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
