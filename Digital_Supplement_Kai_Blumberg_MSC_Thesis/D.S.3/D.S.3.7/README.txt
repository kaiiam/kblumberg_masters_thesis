D.S.3.7: Delivering polar-focused knowledge products

to calculate network statistics from the envoPolar subset. This folder contains two folders:

degree_calculation: to calculate means and medians for the out degree, shortest path length, in degree

subclasses_and_subclasses_queried_directly_from_envo_polar_subset: where we extract the information to build a network from and analyze using cytoscape. this is done by using query_for_class.py to get all the classes in the envoPolar network, query_for_property.py to get all relations in the envoPolar network and finally using query_for_classes_linked_by_input_classes_and_input_properties.py to get the linkages between all classes via all relations within the network, the results of this file can be passed to cytoscape as to build a network. 
