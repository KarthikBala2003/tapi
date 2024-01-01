class CommonLib:
    
    """ ******************** setter getter for inbound folder and file ******************** """
    
    def set_inbound_folder(self,folder_location):
        self.__inbound_folder_location = folder_location

    def get_inbound_folder(self):
        return self.__inbound_folder_location
    
    def set_inbound_file(self,file_name):
        self.__inbound_file_name = file_name

    def get_inbound_file(self):
        return self.__inbound_file_name
    
    def set_api_key(self,aws_key):
        self.__aws_key = aws_key

    def get_api_key(self):
        return self.__aws_key
    