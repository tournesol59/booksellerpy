from enum import Enum
#enum needed for class syntax
class Categ(Enum):
    OUVRAGE=1
    PROCEEDING=2
    MANUEL=3
    ENCYCLOPEDIA=4
	
#the real class 
class eBook:
    def __init__(self, _data):
      #initialize
        self.title = _data['title']
        self.author = _data['author']
        self.categ = _data['category']
        self.course_id = _data['course_id']
	  #then 'heading' could be added
	  
	  