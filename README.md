﻿new or updated:
===========================
 
server(NEW!!, devserver/wsgi application, docs at stranica.nl/docs),
devserver(a (now simple) devserver that you help devlop sites), 
mail(mail messages and files with python),
maths(a lib with math functions),
py_install(updated)




include:
===========================

    introduction
                                                                                 
    	
    description                                                                                                                                                                    
    	
    home
    
    loading_bars

introduction:
===========================

    to install os_sys you type: pip install os_sys                                                                                  
    to upgrade os_sys you type: pip install --upgrade os_sys                                                                                  
    so lets get start to install os_sys                                                                                  

                                                                                

discription:
===========================
    os_sys is a extra package for python(3)                                                                                  
    it's a extra to have a more easy use of the normal python libs                                                                                  
    plz look sometimes to my packages becuse i am making more own libs(extra is not that own lib)                                                                                  
    if i have more info i while show it here                                                                                   
    plz read the license                                                                                  
    
    



loading_bars:
Easy progress reporting for Python
==================================

|pypi|



Bars
----

There are 7 progress bars to choose from:

- ``Bar``
- ``ChargingBar``
- ``FillingSquaresBar``
- ``FillingCirclesBar``
- ``IncrementalBar``
- ``PixelBar``
- ``ShadyBar``

To use them, just call ``next`` to advance and ``finish`` to finish:

.. code-block:: python

    from os_sys.progress import bar

    bar = Bar('Processing', max=20)
    for i in range(20):
        # Do some work
        bar.next()
    bar.finish()

or use any bar of this class as a context manager:

.. code-block:: python

    from os_sys.progress import bar

    with Bar('Processing', max=20) as bar:
        for i in range(20):
            # Do some work
            bar.next()

The result will be a bar like the following: ::

    Processing |#############                   | 42/100

To simplify the common case where the work is done in an iterator, you can
use the ``iter`` method:

.. code-block:: python

    for i in Bar('Processing').iter(it):
        # Do some work

Progress bars are very customizable, you can change their width, their fill
character, their suffix and more:

.. code-block:: python

    bar = Bar('Loading', fill='@', suffix='%(percent)d%%')

This will produce a bar like the following: ::

    Loading |@@@@@@@@@@@@@                   | 42%

You can use a number of template arguments in ``message`` and ``suffix``:

==========  ================================
Name        Value
==========  ================================
index       current value
max         maximum value
remaining   max - index
progress    index / max
percent     progress * 100
avg         simple moving average time per item (in seconds)
elapsed     elapsed time in seconds
elapsed_td  elapsed as a timedelta (useful for printing as a string)
eta         avg * remaining
eta_td      eta as a timedelta (useful for printing as a string)
==========  ================================

Instead of passing all configuration options on instatiation, you can create
your custom subclass:

.. code-block:: python

    class FancyBar(Bar):
        message = 'Loading'
        fill = '*'
        suffix = '%(percent).1f%% - %(eta)ds'

You can also override any of the arguments or create your own:

.. code-block:: python

    class SlowBar(Bar):
        suffix = '%(remaining_hours)d hours remaining'
        @property
        def remaining_hours(self):
            return self.eta // 3600


Spinners
========

For actions with an unknown number of steps you can use a spinner:

.. code-block:: python

    from os_sys.progress import spinner

    spinner = Spinner('Loading ')
    while state != 'FINISHED':
        # Do some work
        spinner.next()

There are 5 predefined spinners:

- ``Spinner``
- ``PieSpinner``
- ``MoonSpinner``
- ``LineSpinner``
- ``PixelSpinner``

comming - ``working to a big update the 2.0.0 release``

home:
===========================
    
    plz visit my one website there you can post evry program for python that you want:

    https://python-libs-com.webnode.nl/
    
