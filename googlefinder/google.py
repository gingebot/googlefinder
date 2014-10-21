from bs4 import BeautifulSoup
import requests


class finder(object):
    """
    Google finder returns google search results against a list of search parameters.

    Only the first 10 results are analysed and only results with the search parameters in the results text are returned.

    Return value is a list of 2 item tuples . Item 1 being the result's link url and item 2 being the
    """

    def __init__(self,site='UK'):

        self.header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
        self.session = requests.session()

        if site == 'UK':
            self.baseurl = 'https://www.google.co.uk/search?q='

    def Search(self,SearchArray):
      return self.__ValidateAndReturnResults(self.__ReturnSearchResultsBlock(self.__ReturnSoup(self.__ReturnHtml(self.__FormSearchUrl(SearchArray)))),SearchArray)

    def __FormSearchUrl(self,SearchArray):
        assert isinstance(SearchArray, list), "Submitted Search parameters must be a lists"
        SearchUrl = self.baseurl
        for i in SearchArray:
            SearchUrl += i
            SearchUrl += '+'
        return SearchUrl

    def __ReturnHtml(self,SearchUrl):
        return self.session.get(SearchUrl, headers=self.header).text

    def __ReturnSoup(self,html):
        return BeautifulSoup(html)

    def __ReturnSearchResultsBlock(self,soup):
        """
        Returns Blocks of search results for further processing
        """
        try:
            return soup.find(id='search').findAll('li', attrs={'class':'g'})
        except AttributeError:
            #No search results found, return empty results set instead of failing
            return []
    def __ValidateAndReturnResults(self,ResultsSoup,SearchArray):

        return [self.__ReturnValidSearchData(i) for i in ResultsSoup if self.__ValidatedResult(i, SearchArray)]

    def __ValidatedResult(self,SingleResultSoup,SearchArray):
        """
        Checks a search result contains search values
        """
        #Find the bold items in the soup (search params re highlighted bold
        Bolds = [i.text.lower() for i in SingleResultSoup.findAll('b')]
        valid = True
        for i in SearchArray:
            if i.lower() not in Bolds:
                valid = False

        return valid

    def  __ReturnValidSearchData(self,SingleResulSoup):
        """
        Returns tuple of url and text portion of result
        """
        return (SingleResulSoup.find('a')['href'].split('&')[0], SingleResulSoup.find('span', attrs={'class':'st'}).text)
