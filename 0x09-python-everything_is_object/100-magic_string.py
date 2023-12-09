#!/usr/bin/python3
def magic_string(def_set=["Best School"]):
    def_set.append(", " + def_set[0][:])
    return "".join(def_set[:-1])
