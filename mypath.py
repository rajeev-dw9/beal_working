class Path(object): # Path is a class that contains a list of points and a list of edges that connect those points together 
    @staticmethod # Static method is a method that is not bound to a class instance  
    def db_root_dir(database): # db_root_dir is a static method that returns the path to the database
        if database == 'fundus': # If the database is fundus 
            return '' # The path to the database is returned
            # return '../../../../data/disc_cup_split/'  # file path to the database  
        else: # If the database is not fundus
            print('Database {} not available.'.format(database)) # Print the database is not available
            raise NotImplementedError # Raise an error 
