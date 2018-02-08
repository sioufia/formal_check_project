This repository corresponds to the project of "Vérification Formelle" (Formal Check) at CentraleSupélec, in the 3rd year.
The main goal is to study different criterias for the WHILE language : compute coverage criteria and generate data set
that validate the criteria for a specific program.

STRUCTURE OF THE PROJECT:
    - control_graph.py : the construction of Control Graph from a WHILE program. It contains 3 classes : 
        - Graph class built from Vertice and Edge classes
        - Vertice class
        - Edge class

    - boolean_exp.py : it contains the class representing the boolean expression (equality, inequality, etc)

    - command_exp.py : it contains the class representing the command expression (assignement, loop, skip)

    - test_generation.py : the automatic generation of data set that validate a critera for a specific WHILE programm

    - constraint_programming.py : a solver made by Professor Dürr during the class of Optimization

    - Control_Graphs : containing control graphs of different WHILE program
        - CG_Project_Example.py : example program of the project
        - CG_PGCD.py
        - CG_Dumb.py
        - CD_Dumb_loop_simple.py
        - Source_Project_Example.txt
        - Source_PGCD.txt
        - Source_Dumb.txt
        - Source_Dumb_loop_simple.txt
    
    - test_folder : containing the different criterias from 1 to 8. For each one, we tried to find data set and program that
    validate the criterias.
        - all_assigned_1.py : 1st criteria
        - all_decisions_2.py : 2nd criteria
        - all_4_paths_3.py : 3rd criteria
        - all_i_loop_4.py : 4th criteria
        - all_definitions_5.py : 5th criteria
        - all_usage_6.py : 6th criteria
        - all_DU_paths_7.py : 7th criteria
        - all_conditions_8.py : 8th criteria
