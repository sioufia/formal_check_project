# Formal Check Project

By Alexandre Sioufi and Mathieu Seris

This repository corresponds to the project of "Vérification Formelle" (Formal Check) at CentraleSupélec, in the 3rd year.
The main goal is to study different criterias for the WHILE language : compute coverage criteria and generate data set
that validate the criteria for a specific program.

# STRUCTURE OF THE PROJECT:

- ./control_graph.py : the construction of Control Graph from a WHILE program. It contains 3 classes : 
    - Graph class built from Vertice and Edge classes
    - Vertice class
    - Edge class

- ./boolean_exp.py : it contains the class representing the boolean expression (equality, inequality, etc)

- ./command_exp.py : it contains the class representing the command expression (assignement, loop, skip)

- ./test_generation.py : the automatic generation of data set that validate a critera for a specific WHILE programm. 
Currently it finds the data set for a programm with only one variable.
To take into account multiple variables, we could use the package constraint from python.

- ./constraint_programming.py : a solver made by Professor Dürr during the class of Optimization

- Control_Graphs : containing control graphs of different WHILE program (both class representation for symbolic execution and source code)
    - ./Control_Graphs/CG_Project_Example.py : example program of the project
    - ./Control_Graphs/CG_PGCD.py
    - ./Control_Graphs/CG_Dumb.py
    - ./Control_Graphs/CD_Dumb_loop_simple.py
    - ./Control_Graphs/Source_Project_Example.txt
    - ./Control_Graphs/Source_PGCD.txt
    - ./Control_Graphs/Source_Dumb.txt
    - ./Control_Graphs/Source_Dumb_loop_simple.txt
    
- test_folder : containing the different criterias from 1 to 8. For each one, we tried to find data set and program that
validate the criterias.
    - ./test_folder/all_assigned_1.py : 1st criteria
    - ./test_folder/all_decisions_2.py : 2nd criteria
    - ./test_folder/all_4_paths_3.py : 3rd criteria
    - ./test_folder/all_i_loop_4.py : 4th criteria
    - ./test_folder/all_definitions_5.py : 5th criteria
    - ./test_folder/all_usage_6.py : 6th criteria
    - ./test_folder/all_DU_paths_7.py : 7th criteria
    - ./test_folder/all_conditions_8.py : 8th criteria

# STEPS TO RUN THE CRITERIAS:
    1/ Go to the folder ./test_folder
    2/ Launch the file corresponding to the criteria
    you want : python <name_of_file>
    For each file there are :
        - 1 passed test (with a control graph and a dataset)
        - 1 failed test (with a control graph and a dataset)
        - 1 generation of dataset for the criteria (only for criterias 
        1,2,3 and 8)
