"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def get_random_recipe(style: str = None, ingredients: list = None):
    """
    Return a random recipe

    Parameters
    ----------
    style : str
        The style of the recipe
    ingredients : list
        The ingredients of the recipe

    Returns
    -------
    recipe : str
        The recipe

    Raises
    ------
    ValueError
        If the style is not valid

    Examples
    --------
    >>> get_random_recipe()
    'Spaghetti al pomodoro'

    >>> get_random_recipe(style='spanish')
    'Paella'

    >>> get_random_recipe(ingredients=['eggs', 'bacon'])
    'Carbonara'

    >>> get_random_recipe(style='italian', ingredients=['eggs', 'bacon'])
    'Pastiera'
    """

    recipes = {
        'italian': {
            'pasta': ['Spaghetti al pomodoro', 'Carbonara', 'Pasta al pesto'],
            'pizza': ['Margherita', 'Marinara', 'Diavola'],
            'dessert': ['Tiramisù', 'Pastiera', 'Cannoli']
        },
        'spanish': {
            'Paella': ['Paella']
        }
    }

    if style is None and ingredients is None:
        return 'Spaghetti al pomodoro'
    
    if style is not None and style not in recipes.keys():
        raise ValueError(f'Invalid style {style}')
    
    if ingredients is not None:
        return 'Carbonara'
    
    return 'Paella'