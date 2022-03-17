from bs4 import BeautifulSoup
import urllib3


def  get_page(the_url):

    http_pool = urllib3.connection_from_url(the_url)
    r = http_pool.urlopen('GET', the_url)
    return r


def get_linked_in_photo(l_url):

    page = get_page(l_url)

    soup = BeautifulSoup(page.data)
    img_element = soup.find_all("img", {"class": "artdeco-entity-image"})

    print(img_element)


if __name__ == "__main__":
    get_linked_in_photo("https://www.linkedin.com/in/nicoleanasenes")



"""

<img class="artdeco-entity-image artdeco-entity-image--circle-8 top-card-layout__entity-image top-card__profile-image top-card__profile-image--real-image onload lazy-loaded" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static-exp1.licdn.com/sc/h/244xhbkr7g40x6bsu4gi6q4ry" alt="Nicole Anasenes" src="https://media-exp1.licdn.com/dms/image/C4D03AQGmWPJUOptyjQ/profile-displayphoto-shrink_200_200/0/1532181809794?e=1652918400&amp;v=beta&amp;t=SAsyPc35pGHGXUdgTD5hc2Do8KQ-U4aaDbh8iql3_J8">
"""





