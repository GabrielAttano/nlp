class FileReader:
    '''This FileReader class was created with the fake.br-Corpus in mind, so all 
    methods in it were made in such a way that it follows the naming convention 
    used in the corpus. 
    Attempting to use the methods here for other files won't work as intended.'''

    @classmethod
    def read_file(cls, file_name):
        '''Returns a string with the content of the file specified'''

        file = open(file_name, encoding="utf-8")
        text = file.read()
        file.close()
        return text
    
    
