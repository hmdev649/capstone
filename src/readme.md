The data for this project is not included in the public facing repo, and neither is the code for scraping it, primarily because the data is proprietary (the total dataset was also almost 2 GB in size). Instead, what I've briefly described below is the process by which the final dataset was created.

	1. Filter articles list from the sitemap
	2. Load each article page and save offline 
	3. Parse each article page for data and save in database:
		a. Article metadata (author, category, date published, etc)
		b. Article tags
		c. Article comments (commenter name, text, time published, number of likes, parent comment, etc)
	4. Extract list of unique commenter names from comments list
	5. Load each commenter user profile and save offline
	6. Parse each commenter profile and save in database:
		a. Member metadata (location, website, member since, etc)
		b. Member favorite brands
		c. Member watch collection (year, manufacturer, model, etc)
	7. Export database tables to csv for easy reading in Jupyter notebooks
	8. Read in csv files (this step is visible in the notebooks)

Please contact me if you'd like to discuss these steps in more detail. A brief overview of the online community is available in the reports folder, and a list of the main Python libraries used for extraction and analysis is listed below:

	1. Pandas
	2. numpy
	3. beautifulsoup4
	4. sqlite
	5. matplotlib
	6. statsmodels
	7. datetime
	8. colour


