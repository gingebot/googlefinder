GoogleFinder
============

OverView
--------

Googlefinder is a package designed to allow quick internet searches via google and return and array of url and snippet results. Currently this package searches google.co.uk only.

Please note use of this package may be against Google's terms of use.

Requirements
------------
* Googlefinder is written for python 2.X
* requests 2.4.3 or newer
* beautifulsoup4 4.3.2 or newer

Installation
------------

Install with pip

```pip install googlefinder```


Or installation can be from source:

```git clone https://github.com/gingebot/googlefinder.git```


```python setup.py install```



Package Specifics / Use
-----------------------

contained within module google is object finder.

On initialisation finder creates a valid session.

Search method takes a list of search terms, it then gets the first 10 search results and filters for only results containing all the search terms. Return data is a list of 2 part tuples of containing result url and result snippet.

Example use
-----------

```>>> from googlefinder.google import finder```

```>>> x = finder()```

```>>> x.Search(['toast','banana'])```

```[(u'/url?q=http://www.bbcgoodfood.com/recipes/1897711/peanut-butter-and-banana-on-toast', u'Toast bread and slice banana. Layer banana on one slice of toast and dust with \ncinnamon. Spread the second slice with peanut butter, then sandwich the two\xa0...'), (u'/url?q=http://www.hovisbakery.co.uk/health-and-recipes/recipes/recipe/classic-banana-on-toast', u'Mash a banana in a bowl and spread onto 2 slices of Hovis Wholemeal toast. ... \nQuick Fix: Slice the banana and eat on the go as a sandwich. Recipes.'), (u'/url?q=http://www.calorieking.com/recipes/Breakfasts/Cereals-Breads-Waffles/Banana-Toast_Y2lkPTE1JnNpZD00MyZyaWQ9MjAx.html', u'Preheat the grill or broiler. Toast bread on both sides. Arrange the banana slices \nevenly on the toast. Dust with cinnamon and artificial sweetener (optional).'), (u'/url?q=http://www.marthastewart.com/315671/banana-french-toast', u'Why wait for the weekend to enjoy French toast when you can whip up this \nirresistible breakfast in practically no time?'), (u'/url?q=http://allrecipes.com/recipe/peanut-butter-and-banana-french-toast/', u'An unique and delicious recipe that my mom used to make. It is so easy that even \nkids can help to make it. Serve it hot with butter or margarine and syrup.'), (u'/url?q=http://onehandedcooks.com.au/recipe/banana-toast-for-babies/', u'25 Mar 2014 ... Banana toast is a wonderful soft finger food for babies and toddlers and helps to \nkeep breakfast interesting with different tastes and textures.'), (u'/url?q=http://www.jamieoliver.com/recipes/fruit-recipes/stuffed-french-toast/', u"Jamie's stuffed French toast recipe is delicious; everyone will love these fried \neggy bread sandwiches with a banana, honey and pecan nut filling.")]``