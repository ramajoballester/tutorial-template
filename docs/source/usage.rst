Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

.. Creating recipes
.. ----------------

.. To retrieve a list of random ingredients,
.. you can use the ``lumache.api.get_random_ingredients()`` function:

.. .. autofunction:: lumache.api.get_random_ingredients

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.api.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.api.InvalidKindError

.. For example:

.. >>> import lumache
.. >>> lumache.api.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

