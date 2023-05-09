========
Ragnarok
========


.. image:: https://img.shields.io/pypi/v/ragnarok.svg
        :target: https://pypi.python.org/pypi/ragnarok

.. image:: https://img.shields.io/travis/ZenulAbidin/ragnarok.svg
        :target: https://travis-ci.com/ZenulAbidin/ragnarok

.. image:: https://readthedocs.org/projects/ragnarok/badge/?version=latest
        :target: https://ragnarok.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/ZenulAbidin/ragnarok/shield.svg
     :target: https://pyup.io/repos/github/ZenulAbidin/ragnarok/
     :alt: Updates



On-chain + Lightning desktop wallet with a bundled full node.


* Free software: GNU General Public License v3
* Documentation: https://ragnarok.readthedocs.io.


Features
--------

* It supports legacy addresses, native and nested segwit addresses, and taproot addresses
* It creates wallets from BIP39 seed phrases.
* Wallet passwords use Scrypt to delay the decryption algorithm to a fixed amount of time, for security.
* Anti-clipboard hijacking area under transaction windows prints addresses that have been inserted into
  the clipboard.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
