from lib.map_concept import MapConcept
import os
test =MapConcept()
#print(os.path.abspath(__file__))
a = os.path.join(os.path.dirname(__file__))
#print(a) 
print(test.get_disease_concept_id("糖尿病"))
