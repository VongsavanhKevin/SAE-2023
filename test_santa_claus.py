from santa_claus import*



def test_dictionary_cities():
    assert dictionary_cities(["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]) == {'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    assert dictionary_cities(["Lyon", 4.85, 45.75,"Paris",2.33, 48.86,"Marseille", 5.40, 43.30,"Lille", 3.06, 50.63]) == {'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662}, 'Marseille': {'Lyon': 275.87965367431525, 'Paris': 661.8616554466852, 'Lille': 834.0220261600157}, 'Lille': {'Lyon': 558.5472363339595, 'Paris': 203.67224282542662, 'Marseille': 834.0220261600157}}
    assert dictionary_cities(["Marseille", 5.40, 43.30,"Lyon", 4.85, 45.75,"Lille", 3.06, 50.63,"Paris",2.33, 48.86]) == {'Marseille': {'Lyon': 275.87965367431525, 'Lille': 834.0220261600157, 'Paris': 661.8616554466852}, 'Lyon': {'Marseille': 275.87965367431525, 'Lille': 558.5472363339595, 'Paris': 394.5056834297657}, 'Lille': {'Marseille': 834.0220261600157, 'Lyon': 558.5472363339595, 'Paris': 203.67224282542662}, 'Paris': {'Marseille': 661.8616554466852, 'Lyon': 394.5056834297657, 'Lille': 203.67224282542662}}
    print('Test unitaire : ok')


def test_distaces_cities():
    assert distances_cities('Paris', 'Louvres', dico) == -1
    assert distances_cities('Marseille', 'Paris', dico) == 661.8616554466852 
    assert distances_cities('Lyon', 'Paris', dico) == 394.5056834297657
    assert distances_cities('Villetaneuse', 'Louvres', dico) == -1
    assert distances_cities('Villetaneuse', 'Lille', dico) == -1
    print("test unitaire : ok")


def test_distaces_cities():
    assert tour_length(["Marseille", "Lyon", "Paris", "Lille"], dico) == 1708.0796060895232
    assert tour_length(["Marseille", "Lyon", "Lille", "Paris"], dico) == 1699.9607882803707
    assert tour_length(["Marseille", "Lille", "Lyon", "Paris"], dico) == 2448.9366013704102
    assert tour_length(["Paris", "Lille", "Lyon", "Marseille"], dico) == 1699.9607882803707
    assert tour_length(["Lille", "Marseille", "Paris", "Lyon"], dico) == 2448.9366013704102
    print("test unitaire : ok")


def test_closest_city():
    assert closest_city('Paris',["Marseille", "Lyon","Lille"],dico) == 2
    assert closest_city('Lille',["Lyon", "Paris","Marseille"],dico) == 1
    assert closest_city('Paris',["Marseille", "Lyon","Lille"],dico) == 2 
    assert closest_city('Marseille',["Lyon", "Paris","Lille"],dico) == 0
    assert closest_city('Lyon',["Lille", "Paris","Marseille"],dico) == 2
    print("test unitaire : ok")

def test_tour_from_closest_city():
    assert tour_from_closest_city('Marseille',dico) == ['Marseille', 'Lyon', 'Paris', 'Lille']
    assert tour_from_closest_city('Lyon',dico) == ['Lyon', 'Marseille', 'Paris', 'Lille']
    assert tour_from_closest_city('Paris',dico) == ['Paris', 'Lille', 'Lyon', 'Marseille']
    assert tour_from_closest_city('Lille',dico) == ['Lille', 'Paris', 'Lyon', 'Marseille']
    print("test unitaire : ok")

def test_tour_from_closest_city():
    assert best_tour_from_closest_city(dico) == ['Lille', 'Paris', 'Lyon', 'Marseille']
    print("test unitaire : ok")

def test_reverse_part_tour():
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],2,5) == ['Agen', 'Belfort', 'Fréjus', 'Épinay', 'Dijon', 'Cahors', 'Grenoble', 'Hyères']
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],0,6) == ['Grenoble', 'Fréjus', 'Épinay', 'Dijon', 'Cahors', 'Belfort', 'Agen', 'Hyères']
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],5,6) == ['Agen', 'Belfort', 'Cahors', 'Dijon', 'Épinay', 'Grenoble', 'Fréjus', 'Hyères']
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],3,6) == ['Agen', 'Belfort', 'Cahors', 'Grenoble', 'Fréjus', 'Épinay', 'Dijon', 'Hyères']
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],3,4) == ['Agen', 'Belfort', 'Cahors', 'Épinay', 'Dijon', 'Fréjus', 'Grenoble', 'Hyères']
    print("test unitaire : ok")

def test_inversion_length_diff():
    assert inversion_length_diff(dico,["Marseille", "Lyon", "Paris", "Lille"],1,2) == -740.8569952808871
    assert inversion_length_diff(dico,["Paris", "Marseille", "Lyon","Lille" ],1,3) == -2.2737367544323206e-13
    assert inversion_length_diff(dico,["Paris", "Marseille", "Lyon","Lille" ],1,2) == -8.118817809152688
    assert inversion_length_diff(dico,["Lille", "Paris", "Marseille","Lyon" ],1,2) == -748.9758130900395
    assert inversion_length_diff(dico,["Lille", "Marseille", "Lyon","Paris" ],0,3) == 0
    print("Test unitaire : ok")


def test_better_inversion():
    assert better_inversion(["Marseille", "Paris", "Lyon", "Lille"],dico) 
    assert not better_inversion(['Marseille', 'Lyon', 'Paris', 'Lille'],dico)
    assert not better_inversion(["Lille", "Paris", "Marseille","Lyon"],dico)
    assert better_inversion(["Lille", "Marseille", "Paris","Lyon"],dico)
    assert not better_inversion(['Lille', 'Paris', 'Marseille', 'Lyon'],dico)
    print("Test unitaire : ok")


def test_best_obtained_with_inversions():
    assert best_obtained_with_inversions(["Marseille", "Paris", "Lyon", "Lille"],dico) == 2
    assert best_obtained_with_inversions(["Paris", "Lyon", "Marseille", "Lille"],dico) == 1
    print("Test unitaire : ok")