.. lfs_sofortueberweisung.de documentation master file, created by
   sphinx-quickstart on Sun Mar  4 08:57:53 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

lfs_sofortueberweisung
======================

What is it?
-----------

lfs_sofortueberweisung is the integration of the payment processor
`sofortüberweisung`_ for `LFS`_.

Installation
------------

#. Register at https://www.payment-network.com/sue_de to get a user and project
   id.

#. Within ``buildout.cfg`` add ``lfs_sofortuebweisung`` to eggs within the
   ``django`` section::

    eggs =
        django-lfs == 0.7.0b1
        gunicorn
        lfs_sofortueberweisung

#. Run the installer::

    $ bin/buildout -Nv

#. Within ``settings.py`` add ``lfs_sofortuebweisung`` to ``LFS_PAYMENT_METHOD_PROCESSORS``::

    LFS_PAYMENT_METHOD_PROCESSORS = [
        ["lfs_sofortueberweisung.models.SofortUeberweisungPaymentMethodProcessor", "sofortueberweisung.de"],
    ]

#. Within ``settings.py`` add lfs_sofortuebweisung specific settings::

    SOFORTUEBERWEISUNG_USERID = your_user_id
    SOFORTUEBERWEISUNG_PROJECT_ID = your_project_id

#. Restart your instance

#. Within the LFS Management go to ``Shop/Payment Methods`` and add a new
   payment processor.

#. Select ``sofortueberweisung.de`` for the ``Module`` field.

See also
--------

* `LFS Settings <http://docs.getlfs.com/en/latest/developer/settings.html>`_

.. _`sofortüberweisung.de`: https://www.payment-network.com/sue_de
.. _`LFS`: http://pypi.python.org/pypi/django-lfs
