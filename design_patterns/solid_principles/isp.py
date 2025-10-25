from abc import abstractmethod

class machine:
    def print(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError

class multi_function_printer(machine):
    def print(self, document):
        pass
    def scan(self, document):
        pass
    def fax(self, document):
        pass

class old_fashioned_printer(machine):
    def print(self, document):
        pass
    # def scan(self, document):
    #     pass
    def scan(self, document):
        raise NotImplementedError("Printer cannot Scan!!")
    
    def fax(self, document):
        pass

## Seperate iterfaces

class printer():
    @abstractmethod
    def print(self, document):
        pass

class scanner():
    @abstractmethod
    def scan(self, document):
        pass

class my_printer(printer):
    def print(self, document):
        print(document)

class photo_copier(printer, scanner):
    def print(self, document):
        return super().print(document)
    def scan(self, document):
        return super().scan(document)