def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    try:
        import re
        #from lxml import etree
        with open(filename) as f:
            data = f.read()
        urls = re.findall('<a.+href=[\'|\"](.+)[\'|\"].*?>(.+)</a>', data)
        dictionary = {}
        for url in urls:
            if url[1] not in dictionary.keys():
                dictionary[url[1]] = [url[0]]
            elif url[0] not in dictionary[url[1]]:
                result[url[1]].append(m[0])
        return dictionary
    except IOError, e:
        print "Sorry, that is not a valid file"

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    #This approach is much better because it deals with corner cases more elegantly
    from lxml import etree
    try:
        urls = etree.parse(filename, etree.HTMLParser()).xpath("//a")
        dictionary = {}
        for url in urls:
            if url.text not in dictionary.keys():
                dictionary[url.text] = [url.get("href")]
            elif url.get("href") not in dictionary[url.text]:
                dictionary[url.text].append(url.get("href"))
        return dictionary

    except IOError:
        print "Sorry, that is not a valid file"

