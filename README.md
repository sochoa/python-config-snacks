Config Snacks
=============

## Overview

This project is called config "snacks" because its a collection
of small bits that make configuration a bit easier.

## Placeholders

Used for rendering placeholders that exist in strings
within things that behave like dictionaries.

The primary use-case of this module is to use either file-based
or env-based.  This helps developers to drive values in configuration
trees (yaml, json, etc) that behave like dictionaries based on
environment variable values or file contents of known files that
contain values (e.g. /etc/region or some such).

## Assertions

Used for making sure that values are what you expect them to be.
