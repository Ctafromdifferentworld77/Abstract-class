class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
        
class Sri_Lanka():
    def capital(self):
        print("Colombo is the capital of Sri Lanka.")
    def language(self):
        print("Sinhala is the most widely spoken language of Sri la.")
        
obj_ind = India()
obj_Sri_Lanka = Sri_Lanka()
# Conmon Interface
for country in (obj_ind, obj_Sri_Lanka):
    country. capital()
    country. language
