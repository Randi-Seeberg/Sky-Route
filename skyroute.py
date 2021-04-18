from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark) 

stations_under_construction = ['Bridgeport', 'King Edward', 'Broadway-City Hall', 'Vancouver City Centre']
stations_uc_dict = {i : stations_under_construction[i] for i in range(len(stations_under_construction))}
stations_uc_string = ""
for num, station in stations_uc_dict.items():
  stations_uc_string += "{0} - {1}\n".format(num, station)

station_list = []
station_list += vc_metro.keys()

station_dict = {i : station_list[i] for i in range(len(station_list))}

station_string = ""
for num, station in station_dict.items():
  station_string += "{0} - {1}\n".format(num, station)

def maintenance_greet():
  print("Hi, this is where you update the list of stations under construction. For maintenance crew only!\n")

def choose_action():  
  action = input("Type 'd' if you want to deactivate a station by adding it to the list of stations under construction. \n\nType 'r' if you want to reactivate a station by removing it from the list of stations under construction.\n")
  if action == 'd' or action == 'r':
    return action
  else:
    print("Sorry, that's neither 'd' nor 'r'. Please try again!\n")
    choose_action()
    
  return action
  
def get_station_to_uc():
  print("Here is a complete list of SkyRoute metro stations:\n" + station_string + "\n")
  station_key = input("Which station do you want to set to 'under construction'? Type in the corresponding number: \n")
  if int(station_key) in station_dict.keys():
    station_to_uc = station_dict[int(station_key)]
  
  else:
    print("Sorry, that number does not correspond to any station on our list. Please try again...")
    return get_station_to_uc()

  return station_to_uc

def get_station_from_uc():
  print("Here is a list of stations currently under construction.\n" + stations_uc_string)
  station_key = input("Type the number corresponding to the station you want to reactivate: \n")
  if int(station_key) in stations_uc_dict.keys():
    station_from_uc = stations_uc_dict[int(station_key)]

  else:
    print("Sorry, that number does not correspond to any station on our list. Please try again...")
    return get_station_from_uc()

  return station_from_uc


def add_station_to_uc():
  station_to_uc = get_station_to_uc()
  confirmed = input("Please confirm that {0} station is under construction. You can enter 'y' for 'yes' or 'n' for 'no'.".format(station_to_uc))
  if confirmed == 'y':
    stations_under_construction.append(station_to_uc)
  elif confirmed == 'n':
    print("Okay, let's try again: \n")
    get_station_to_uc()
  else:
    print("Oops, that's neither 'y' nor 'n'. Let's try again!")
  
  return stations_under_construction

def remove_station_from_uc():
  station_to_reactivate = get_station_from_uc()
  confirmed = input("Please confirm that {0} station is active again. You can enter 'y' for 'yes' or 'n' for 'no'.".format(station_to_reactivate))
  if confirmed == 'y':
    stations_under_construction.remove(station_to_reactivate)
  elif confirmed == 'n':
    print("Okay, let's try again: \n")
    get_station_to_uc()
  else:
    print("Oops, that's neither 'y' nor 'n'. Let's try again!")
  
  return stations_under_construction 

def repeat_or_exit():
  reply = input("Type 'm' if you wish to perform further maintenance actions\nType 'e' if you wish to exit the maintenance platform\n")
  if reply == 'm':
    maintenance_update_list()
  elif reply == 'e':
    return stations_uc_string
  else:
    print("Oops, that's neither 'm', nor 'e'. Let's try again...")

def maintenance_result(stations_under_construction):
  stations_uc_dict = {i : stations_under_construction[i] for i in range(len(stations_under_construction))}
  stations_uc_string = ""
  for num, station in stations_uc_dict.items():
    stations_uc_string += "{0} - {1}\n".format(num, station)
  print("Okay. Here is your list of stations currently under construction: \n")
  print(stations_uc_string)

def maintenance_update_list():
  action = choose_action()
  if action == 'd':
    stations_under_construction = add_station_to_uc()
  elif action == 'r':
    stations_under_construction = remove_station_from_uc()

  repeat_or_exit()
      
  maintenance_result(stations_under_construction)

  return

def skyroute_maintenance():
  maintenance_greet()
  maintenance_update_list()

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)  

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter:")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]

  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()

  return start_point

def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the correspoding letter: ")

  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    
  else:
    print("Sorry, this is not a landmark we have data on. Let's try this again...")
    return get_end()

  return end_point

def skyroute():
  greet()
  new_route()
  goodbye()


def set_start_and_end(start_point, end_point):
  
  if start_point:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    
    if change_point == "b":
      start_point, end_point = get_start(), get_end()

    elif change_point == "o":
      start_point = get_start()

    elif change_point == "d":
      end_point = get_end()

    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
    
  else:
      start_point = get_start()
      end_point = get_end()
      if start_point == end_point:
        print("Sorry, but your entered origin and destination are the same. Please try again!")
        set_start_and_end(start_point, end_point)    
  
  return start_point, end_point

def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)

  shortest_route = get_route(start_point, end_point)

  if shortest_route:
    shortest_route_string = '\n'.join(shortest_route)

    print("The shortest metro route from {0} to {1} is: \n{2}".format(start_point, end_point, shortest_route_string))
  
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance".format(start_point, end_point))

  again = input("Would you like to see another route? Enter y/n: ")
  if again == "y":
    show_landmarks()
    new_route(start_point, end_point)

def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")

  if see_landmarks == "y":
    print(landmark_string)

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  #gets set of metro stations near landmark
  end_stations = vc_landmarks[end_point]

  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      
      metro_system = get_active_stations() if stations_under_construction else vc_metro

      if stations_under_construction:
        possible_route = dfs(metro_system, start_station, end_station)
        if not possible_route:
          return None

      route = bfs(metro_system, start_station, end_station)
    if route:
      routes.append(route) 
  
  shortest_route = min(routes, key=len)
  return shortest_route

def get_active_stations():
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_stations in vc_metro.items():
      if current_station != station_under_construction:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([])

  return updated_metro

def goodbye():
  print("Thanks for using SkyRoute!")

#skyroute()

skyroute_maintenance()



      

  







