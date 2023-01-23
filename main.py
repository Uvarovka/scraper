import pickle
from arbitr import parse_arbitr
from wanted import parse_wanted
from disqualified import parse_disqualified

def read_arbitr():
    with open("parse_arbitr.pickle", "rb") as handle:
        arbiter_array = pickle.load(handle)
    return arbiter_array

def read_wanted():
    with open("parse_wanted.pickle", "rb") as handle:
        wanted_array = pickle.load(handle)
    return wanted_array

def read_disqualified():
    with open("parse_disqualified.pickle", "rb") as handle:
        disqualified_array = pickle.load(handle)
    return disqualified_array    
