import os

class NewModel:
    """
    This is a new model

    Parameters
    ----------
    new_parameter : str
        A new parameter
    
    Attributes
    ----------
    new_parameter : str
        A new parameter
    
    Methods
    -------
    new_function(even_newer_parameter: str = None)
        A new function

    Examples
    --------
    >>> new_model = NewModel()
    >>> new_model.new_parameter
    'new_parameter'
    >>> new_model.new_function()
  
    """

    def __init__(self, new_parameter: str = None):
        """ 
        Class constructor

        Parameters
        ----------
        new_parameter : str, optional
            _description_, by default None
        """

        self.new_parameter = new_parameter

    def new_function(self, even_newer_parameter: str = None):
        """
        A new function

        Parameters
        ----------
        even_newer_parameter : str, optional
            _description_, by default None
        """
        pass