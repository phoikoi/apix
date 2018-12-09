# apix

### A simple Django site example

Features:

* Blog-like article model
* Markdown rendering of text content
* Includes customized fenced-code Markdown plugin, to render `mermaid` diagrams
* Custom bootstrap color theme (slightly warmer and less saturated)

The application is based on Django, of course, but also
[Channels](https://channels.readthedocs.io/en/latest/), allowing the
use of websockets and other goodies.  These aren't implemented yet,
but the pieces are there.

There is also a customized `settings.py`, which uses my own
`config.py` utility module.  This module reads configuration items
from an INI file in the project directory.  The items are specified
in the settings file using the `config` functions, which include:

* `config()` for generic strings
* `config_bool()` for booleans
* `config_int()` for (base-10) integers
* `config_list()` for lists; the return value of the `config_list` function is a Python list.

Each of these functions has the signature
`config_*('section.item', default=None)`. In the `site.ini` file,
each item is listed within an INI section, and this section is the first
half of the positional argument to `config`:

```ini
[section]
item = <config data goes here>
```

If the `site.ini` file is not present when a django admin command is run,
a default file with a few essential values is written to the place where
the settings file expects it.  The default values may not match your site;
in particular, the `db_url` item may very well be incorrect.  The default
file will have a custom-generated `secret_key` item, so that you don't
have to go looking around for how to make one properly.

### Future features

There are packages specified in the `Pipfile` which aren't used yet:

* `django-redis-cache` for caching
* `django-allauth` for allowing login through external providers like Google, etc.
* Others



