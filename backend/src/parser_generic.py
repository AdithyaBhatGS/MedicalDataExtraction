import abc

# Making the class MedicalParser abstract

class MedicalParser(metaclass=abc.ABCMeta):
    def __init__(self,text):
        self.text=text
    
    # applying decorator that makes parse an abstract method so that all the child classes should override this method

    @abc.abstractmethod
    def parse(self):
        pass