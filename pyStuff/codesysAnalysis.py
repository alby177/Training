import requests, os, bs4

# Save the home page URL
url = 'https://forum.codesys.com/index.php'

# Create a new folder where to save all the files
os.makedirs('codesysForum', exist_ok = True)

# Open the home page url
res = requests.get(url, headers={'user-agent' : 'Mozilla/5.0'})

# Check for errors
res.raise_for_status()

# Parse home forum webpage
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Create a list containing all the code string of the forumlink class among the a tags of the home page
forumElems = soup.select('a.forumlink')

# Create lists used to store page links and titles
forumPages = []
forumTitles = []
i = 0

# From the home page code strings save the link and the titles of every topic
for i in range(len(forumElems)):
    forumPages.append(forumElems[i].get('href')[1:])
    forumTitles.append(forumElems[i].getText())

# Starts from -1 in order to start the titles from the 0 entry of the list
indice = -1

# Examine all the home page topics
for i in forumPages:

    indice += 1

    # User message with which home page topic is opening
    print("Opening topic page {}....".format(i))

    # Create a new folder for each topic
    os.makedirs('codesysForum/{}'.format(forumTitles[indice]), exist_ok = True)

    # Save the link of the topic to be examined
    urlTopic = 'https://forum.codesys.com' + i

    # Examine all the pages inside a certain topic of the home page
    while True:

        # User message with which specific topic is opened
        print("Opening page {}....".format(urlTopic))

        # Open the page of te current topic
        resTopic = requests.get(urlTopic, headers={'user-agent' : 'Mozilla/5.0'})

        # Check for errors
        resTopic.raise_for_status()

        # Parse the topic page
        soupTopic = bs4.BeautifulSoup(resTopic.text, 'html.parser')

        # Select all the topicTitle class object amng the a tags
        topicElems = soupTopic.select('a.topictitle')

        # Create a list where to store the topic pages links
        topicPages = []

        # Save all the discussions of the current topic
        i2 = 0
        for i2 in range(len(topicElems) - 1):
            topicPages.append(topicElems[i2].get('href')[1:])

        # Examine all the discussion of the current topic
        for i3 in topicPages:
            urlPage = 'https://forum.codesys.com' + i3

            # Create the string which will be saved in the file
            str = ''

            # Examine all the pages of the current discussion
            while True:

                # Output which page is being downloaded
                print("Dowloading page {}...".format(urlPage))

                # Connect to the current page
                resPage = requests.get(urlPage)

                try:

                    # Check for errors
                    resPage.raise_for_status()

                # If there is a error in the page, exit the cycle
                except requests.exceptions.HTTPError:
                    break

                # Parse the current discussion page
                soupPage = bs4.BeautifulSoup(resPage.text, 'html.parser')

                # Select the postbody class among div tag
                pageElems = soupPage.select('div.postbody') # Seleziona la classe postbody tra i tag div

                # Check if there are some contents
                if pageElems == []:

                    print('Nothing to save!')

                else:

                    # Save into the string str all the users posts
                    for i4 in pageElems:
                        str = str + i4.getText() + '\n\n'
                try:

                    # Look for the string "next" among the a tags, which leads to the next page
                    nextPage = soupPage.find("a", string="Next")

                    # Extract the link of the next page from the nextPage object
                    NPLink = nextPage['href']

                    # Save the next page link
                    urlPage = 'https://forum.codesys.com' + NPLink[1:]

                # If the button "Next" is not there, exit the cycle
                except TypeError:
                    break

            # Look for the class titles among the a tags and save the text part
            topicName2 = soupPage.find("a", class_="titles").getText()

            # Check for invalid character for a file name
            if topicName2.find(':') != -1:
                topicName = topicName2.replace(':','_')
            elif topicName2.find('/') != -1:
                topicName = topicName2.replace('/','_')
            elif topicName2.find('?') != -1:
                topicName = topicName2.replace('?','_')
            else:
                topicName = topicName2

            # Create the file inside the current topic path
            forumFile = open(os.path.join('codesysForum/{}'.format(forumTitles[indice]), topicName + '.txt'), 'w')

            # Write the text in the file
            forumFile.write(str)

            # Close the file
            forumFile.close()

        try:

            # Look for the string "next" among the a tags, which leads to the next topic page here
            nextPageTopic = soupTopic.find("a", string="Next")

            # Extract the link of the next topic page from the nextPageTopic object
            NPTopic = nextPageTopic['href']

            # Save the url of the next topic page
            urlTopic = 'https://forum.codesys.com' + NPTopic[1:]

        # If the button "Next" is not there, exit the cycle
        except TypeError:
            break
