# ValueObject [![Build Status](https://app.travis-ci.com/dwt/valueobject.svg?branch=master&status=created)](https://app.travis-ci.com/github/dwt/valueobject)

License: ISC - See LICENSE file

`ValueObject` is a `dict`-like object that exposes keys as attributes.
You can use it like a regular dictionary (in fact, it is a subclass
and does not override its `__init__`). You can use attribute or item
access to get or set values.

    >>> from valueobject import ValueObject
    >>> vo = ValueObject(key=1)
    >>> vo['key']
    1
    >>> vo.key
    1
    >>> vo['key'] += 1
    >>> vo.key += 1
    >>> vo['key']
    3
    >>> vo.key
    3

## Usability notes:

 - If you need to access a key that is not a valid Python identifier
   (for example, it includes spaces), use regular dict access.
 - All regular `object`, `dict` and `ValueObject` methods will be
   returned on attribute access. A key such as `copy` needs to be
   accessed via item access syntax (e.g. `valueobject['copy']`).

## Changelog

- 1.0.3: Minor build fixes, to make the setup.py file python3 safe. While the rest of the library was python3 safe all along, that file was not… 😬