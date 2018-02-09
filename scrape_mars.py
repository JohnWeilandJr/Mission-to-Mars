
# coding: utf-8

# In[ ]:


# Import Dependencies
from bs4 import BeautifulSoup 
import requests
from splinter import Browser
import pandas as pd


# In[ ]:


# Part 1: NASA Mars News

# Connect to page and create BeautifulSoup object
def scrape():
	url = "https://mars.nasa.gov/news/";
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	print(soup.body.prettify())


	# In[ ]:


	# Examine and loop through results

	result = soup.find('div', class_='content_title')
	news_title = result.a.text

	result = soup.find('div', class_='image_and_description_container')
	news_p = result.a.text
	 
	if news_title and news_p:
	    print("news_title:" , news_title)
	    print("news_p: " , news_p)


	# In[ ]:


	# Part 2: JPL Mars Space Images - Featured Image

	#Connect to URL and parse with BeautifulSoup

	executable_path = {'executable_path': 'C:/Users/jmw53/Downloads/chromedriver/chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[ ]:


	# Extract featured_image_url

	carousel = soup.find('div', class_='carousel_items')
	article = carousel.find('article', class_ = 'carousel_item')
	image = article['style']
	img = image[23:-3]
	featured_image_url = url + img
	print('featured_image_url: '+ featured_image_url)


	# In[ ]:


	#Part 3: Mars Weather

	#Connect to Twitter URL and parse with BeautifulSoup

	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[ ]:


	# Extract weather infromation from Twitter

	tweet_container = soup.find('div', class_ = 'js-tweet-text-container')
	para = tweet_container.find('p', class_ = 'TweetTextSize')
	mars_weather = para.text.strip()
	print(mars_weather)


	# In[ ]:


	# Part 4: Mars Facts

	# Use Pandas to read URL and pull out Mars' Planet Profile

	url = 'https://space-facts.com/mars/'
	facts = pd.read_html(url)
	facts


	# In[ ]:


	# Rename Columns

	df = facts[0]
	df.columns=['Stat', 'Stat Data']
	print(df)


	# In[ ]:


	df.head()


	# In[ ]:


	# Convert data frame to HTML table string

	html_table_string = df.to_html()
	print(html_table) 


	# In[ ]:


	# Save df as HTML

	df.to_html('mars_fact_table.html')


	# In[ ]:


	# Part 4: Mars Hemisperes

	# Use Chrome inspector to inspect each hemisphere's webpage to find image URL then store as a dictionary

	cerberus_img = 'https://astrogeology.usgs.gov/cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png'
	cerberus_title = 'Cerberus Hemisphere'
	schiaparelli_img = 'https://astrogeology.usgs.gov/cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png'
	schiaparelli_title = 'Schiaparelli Hemisphere'
	syrtis_img = 'https://astrogeology.usgs.gov/cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png'
	syrtis_title = 'Syrtis Hemisphere'
	marineris_img = 'https://astrogeology.usgs.gov/cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png'
	marineris_title = 'Valle Marineris Hemisphere'
	    
	hemisphere_image_urls = [ 
	    {'title': cerberus_title, 'img_url': cerberus_img},
	    {'title': schiaparelli_title, 'img_url': schiaparelli_img},
	    {'title': syrtis_title, 'img_url': syrtis_img},
	    {'title': marineris_title, 'img_url': marineris_img}
	]

	print(hemisphere_image_urls)

