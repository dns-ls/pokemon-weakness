# model.py
# Maximillian Tinati
# December 15, 2013
"""This module contains the model for the Pokemon type calculation app."""
from thetypes import *


#Useful constant: list containing all pokemon types as separate strings in lowercase.
TYPE_LIST = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting',
             'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost',
             'dragon', 'dark', 'steel', 'fairy']

TYPE_ATTACKS = ['normalAtk', 'fireAtk', 'waterAtk', 'electricAtk', 'grassAtk',
                'iceAtk', 'fightingAtk', 'poisonAtk', 'groundAtk', 'flyingAtk',
                'psychicAtk', 'bugAtk', 'rockAtk', 'ghostAtk', 'dragonAtk',
                'darkAtk', 'steelAtk', 'fairyAtk']

def valid_type(thetype):
    """Returns: True if <thetype> is a string representing a valid Pokemon type;
    False otherwise."""
    assert isinstance(thetype, str)
    
    thetype = thetype.lower()   #default string to a standard case for easy checking
    assert thetype in TYPE_LIST


def typeChecker(thetype):
        """Returns: a <Type> object corresponding to the specified Pokemon type
        <thetype>.
        
        Precondition:  <thetype> is a str and a valid Pokemon type."""
        assert isinstance(thetype, str)
        
        thetype = thetype.lower()
        
        if thetype == 'normal':
            return Normal()
        elif thetype == 'fire':
            return Fire()
        elif thetype == 'water':
            return Water()
        elif thetype == 'electric':
            return Electric()
        elif thetype == 'grass':
            return Grass()
        elif thetype == 'ice':
            return Ice()
        elif thetype == 'fighting':
            return Fighting()
        elif thetype == 'poison':
            return Poison()
        elif thetype == 'ground':
            return Ground()
        elif thetype == 'flying':
            return Flying()
        elif thetype == 'psychic':
            return Psychic()
        elif thetype == 'bug':
            return Bug()
        elif thetype == 'rock':
            return Rock()
        elif thetype == 'ghost':
            return Ghost()
        elif thetype == 'dragon':
            return Dragon()
        elif thetype == 'dark':
            return Dark()
        elif thetype == 'steel':
            return Steel()
        elif thetype == 'fairy':
            return Fairy()


def singleWeakness(type1, type2 = None):
    """Prints: a string corresponding to the weaknesses of the given type
    combination.  Values are PRINTED, not returned.
    
    Each line is a different type, and all type attacks are listed.
    
    Precondition: type1 and type2 are str representing valid Pokemon types."""
    #Asserting type1 and type2 are valid Pokemon types
    valid_type(type1)
    if type2 != None:
        valid_type(type2)
    
    pokemon = SingleModel(type1, type2)  #construct the summed type model for the 1-2 types
    

    #poketype is str of the format "Type1 / Type2" for easy displaying of data
    poketype = type1.upper()
    if type2 != None:
        poketype = poketype + " / " + type2.upper()


    print(poketype)
    print("Normal:  " + str(pokemon.sumType.normalAtk))
    print("Feuer:   " + str(pokemon.sumType.fireAtk))
    print("Wasser:  " + str(pokemon.sumType.waterAtk))
    print("Elektro: " + str(pokemon.sumType.electricAtk))
    print("Pflanze: " + str(pokemon.sumType.grassAtk))
    print("Eis:     " + str(pokemon.sumType.iceAtk))
    print("Kampf:   " + str(pokemon.sumType.fightingAtk))
    print("Gift:    " + str(pokemon.sumType.poisonAtk))
    print("Boden:   " + str(pokemon.sumType.groundAtk))
    print("Flug:    " + str(pokemon.sumType.flyingAtk))
    print("Psycho:  " + str(pokemon.sumType.psychicAtk))
    print("Käfer:   " + str(pokemon.sumType.bugAtk))
    print("Gestein: " + str(pokemon.sumType.rockAtk))
    print("Geist:   " + str(pokemon.sumType.ghostAtk))
    print("Drache:  " + str(pokemon.sumType.dragonAtk))
    print("Unlicht: " + str(pokemon.sumType.darkAtk))
    print("Stahl:   " + str(pokemon.sumType.steelAtk))
    print("Fee:     " + str(pokemon.sumType.fairyAtk))

class SingleModel(object):
    """An instance of this class models incoming attack effectiveness against
    A SINGLE defending pokemon, whose type(s) are chosen upon class construction.
    This model calls the appropriate single type classes from thetypes.py, and
    determines the overall effectiveness if the defending pokemon is dual-typed.
    
    Instance attributes:
        types:      a list containing the types of the pokemon to be analyzed
                    [list of 1-2 <Type> objects if any are selected, None otherwise]
        sumType:    a fictional pokemon type containing the effectiveness of
                    incoming attacks to both of the Pokemon's types
                    [a single <Type> object if types specified, None otherwise]"""
    
    def __init__(self, type1 = None, type2 = None):
        """Initializer: constructs an object of type <SingleModel> with all initial
        variable states corresponding to  the inputted Pokemon types.
        
        Precondition: type1 and type2 are strings and valid Pokemon types."""
        #assert valid_type(type1)
        #assert valid_type(type2)
        
        #Create appropriate Type classes if any and append to <types>
        self.types = []
        if type1 is not None:
            typeObj1 = typeChecker(type1)
            self.types.append(typeObj1)
        if type2 is not None:
            typeObj2 = typeChecker(type2)
            self.types.append(typeObj2)
        
        #Initialize sumType att using helper method b/c really long
        self.constructSumType()
    
    def constructSumType(self):
        """Method to handle initialization of the <sumType> attribute.
        Initially, <sumType> is None.  If <types> contains only a single type,
        then <sumType> will contain that particular Type obj.  If <types>
        contains 2 Type objs, then a dual-type Type obj is constructed and stored
        in <sumType>."""
        #Default to None
        self.sumType = None
        
        #If 1 type specified, set the sumType to this type
        if len(self.types) == 1:
            self.sumType = self.types[0]
        
        #If 2 types specified, construct artificial Type w/multiplied effectivenesses
        elif len(self.types) == 2:
            type1 = self.types[0]
            type2 = self.types[1]
            self.sumType = Type()
            
            self.sumType.normalAtk = type1.normalAtk * type2.normalAtk
            self.sumType.fireAtk = type1.fireAtk * type2.fireAtk
            self.sumType.waterAtk = type1.waterAtk * type2.waterAtk
            self.sumType.electricAtk = type1.electricAtk * type2.electricAtk
            self.sumType.grassAtk = type1.grassAtk * type2.grassAtk
            self.sumType.iceAtk = type1.iceAtk * type2.iceAtk
            self.sumType.fightingAtk = type1.fightingAtk * type2.fightingAtk
            self.sumType.poisonAtk = type1.poisonAtk * type2.poisonAtk
            self.sumType.groundAtk = type1.groundAtk * type2.groundAtk
            self.sumType.flyingAtk = type1.flyingAtk * type2.flyingAtk
            self.sumType.psychicAtk = type1.psychicAtk * type2.psychicAtk
            self.sumType.bugAtk = type1.bugAtk * type2.bugAtk
            self.sumType.rockAtk = type1.rockAtk * type2.rockAtk
            self.sumType.ghostAtk = type1.ghostAtk * type2.ghostAtk
            self.sumType.dragonAtk = type1.dragonAtk * type2.dragonAtk
            self.sumType.darkAtk = type1.darkAtk * type2.darkAtk
            self.sumType.steelAtk = type1.steelAtk * type2.steelAtk
            self.sumType.fairyAtk = type1.fairyAtk * type2.fairyAtk

    def type_checker(self, pokemon):
        """Function that determines whether or not the types in <pokemon> are
        valid types.  This function calls <valid_type> to determine type
        validity.  This function also serves to check that raw input and parsing
        were done correctly, by verifying that <pokemon> is a list of 1-2 strings.
        
        Precondition: pokemon is a list of 2 strings."""
        assert isinstance(pokemon, list)
        for i in pokemon:
            assert isinstance(i, str)
        assert len(pokemon) == 1 or len(pokemon) == 2
        
        for i in pokemon:
            valid_type(i)