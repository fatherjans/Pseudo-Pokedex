import pakuri

class Pakudex:
    def __init__(self, capacity=20):
        # initializes this object to contain exactly capacity objects when completely full
        # pakudex capacity is 20
        self.capacity = capacity
        self.pdex = []

    def get_size(self):
        # returns the number of critters currently being stored in the pakudex
        return len(self.pdex)

    def get_capacity(self):
        # returns the number of critters that the pakudex has the capacity to hold at most
        return self.capacity

    def get_species_array(self):
        # returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
        # if species is not in the pakudex, returns None
        if len(self.pdex) == 0:     # if length of pdex list is zero then there is no pakuri, return None
            return None
        else:
            # for each object in self.pdex, get species name and append to string list
            species_array = []
            for i in self.pdex:
                species_array.append(str(i.get_species()))
            return species_array

    def get_stats(self, species):
        # returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
        pdex_list = self.pdex
        stats = []
        in_pdex = False
        for i in pdex_list:
            # if species is in the pakudex, append each evolved stat to stats
            if species == i.get_species():
                stats.append(int(i.get_attack()))
                stats.append(int(i.get_defense()))
                stats.append(int(i.get_speed()))
                in_pdex = True      # true if there is paku in the list
                break
        if not in_pdex:     # if species is not in pakudex return None
            return None
        else:
            return stats

    def sort_pakuri(self):
        # sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
        self.pdex.sort(key=lambda item: item.get_species())
        pass

    def add_pakuri(self, species):
        # adds species to the pakudex; if successful, return True, and False otherwise
        successful = False
        for i in self.pdex:
            if i.get_species() == species:
                return successful
        if self.get_size() >= self.capacity:
            return successful
        else:
            successful = True
            self.pdex.append(pakuri.Pakuri(species))
            return successful

    def evolve_species(self, species):
        # attempts to evolve species within the pakudex; if successful, return True, and False otherwise
        pdex_list = self.pdex
        in_pdex = False
        for i in pdex_list:
            if species == i.get_species():
                # if species is in pdex list, evolve pakuri and turn variable true
                i.evolve()
                in_pdex = True
                break
        if not in_pdex:
            return False
        else:
            return True
    