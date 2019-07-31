.. Lines starting with two dots are special commands. But if no command can be found, the line is considered as a comment

=========================================================
Main titles are written using equals signs over and under
=========================================================

Note that there must be as many equals signs as title characters.

Title are underlined with equals signs too
==========================================

Subtitles with dashes
---------------------

You can  put text in *italic* or in **bold**, you can "mark" text as code with double backquote ``print()``.

Lists are as simple as in Markdown:

- First item
- Second item
    - Sub item

or

* First item
* Second item
    * Sub item

Tables are really easy to write:

=========== ========
Country     Capital
=========== ========
France      Paris
Japan       Tokyo
=========== ========

More complex tables can be done easily (merged columns and/or rows) but I suggest you to read the complete doc for this :)

There are multiple ways to make links:

- By adding an underscore after a word : Github_ and by adding the target URL after the text (this way has the advantage to not insert unnecessary URLs inside readable text).
- By typing a full comprehensible URL : https://github.com/ (will be automatically converted to a link)
- By making a more Markdown-like link: `Github <https://github.com/>`_ .

.. _Github https://github.com/

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

| These lines are
| broken exactly like in
| the source file.

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

