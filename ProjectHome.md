# Ehtml-py #


# Introduction #

Ehtml(Extend HTML) help you build static web site(page) easy and quickly.

There are a php version of [ehtml](http://sourceforge.net/projects/ehtml/) on [sf](http://sourceforge.net/).
and ehtml-py build on genshi(python).


# System Requirements #

  * apache2
  * python2.5+
  * genshi0.4.4+


# Install #

checkout the ehtml
```
svn checkout http://ehtml-py.googlecode.com/svn/trunk/ ehtml-py-read-only
```
to anywhere you like.
consider the directory as $ehtml-dir$.
change file $ehtml-dir$/ehtml/handler.py 's mode to 755.
```
chmod a+x $ehtml-dir$/ehtml/handler.py
```


open the apache's config file,
add the following 3 lines:

```
AddHandler cgi-script .py
Action ehtml-render $ehtml-dir$/ehtml/handler.py
AddHandler ehtml-render .ehtml
```

to the [Directory](Directory.md) of your site.
if there already has a line like
```
AddHandler cgi-script
```
in config, just add .py to the end of line with a space.

if you got any error,
check the
```
Options
```
to see if there are
ExecCGI
option be added.

if you have any trouble to setup the apache's config file,
go to [about AddHandler](http://httpd.apache.org/docs/2.0/mod/mod_mime.html#addhandler)
or [about Action](http://httpd.apache.org/docs/2.0/mod/mod_actions.html#action)
or [about Options](http://httpd.apache.org/docs/2.0/mod/core.html#options) to get help.

Good luck!