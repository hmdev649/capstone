I'm building a recommendation system that suggests specifically relevant articles to readers who ask questions in the comments section of Hodinkee, a media website that covers the world of watches. My approach is not specific to the knowledge domain, so this solution can be applied to online communities that geek out over everything from watches and wine to tech gadgets and online gaming.

I discovered a love for mechanical watches and horology about three years ago when I became a regular reader of Hodinkee, one of the premier media companies covering the art of horology and all things watches. Over its decade-long existence it has garnered and grown a passionate and engaged audience, and created a rich trove of high quality horological journalism.
As new readers come to the site, or casual readers return, often the comments will contain questions that have previously been written about in depth on the site. Having a way to refer these users to those articles could help improve the user experience, grow engagement and time spent across the entire corpus of articles, and hopefully lead to a higher conversion rate for the commercial side of the business.

This project builds a recommendation system that answers these questions in the comments by referring readers to Hodinkee articles that answer their questions with a high degree of confidence. The general principle should be easily carried over to other, similar online communities with highly engaged audiences.

## Data Understanding
The Hodinkee site publishes more than 15 articles a week, and its complete corpus is currently approaching 7,000 articles. These include everything from short posts describing a new product launch to 10,000 word essays diving deep into horological arcana. The comments on each article can vary in number from under ten to hundreds over time. 

In just the three years that the site has had its own implementation of a commenting system there have been nearly 150,000 comments posted on articles published since that time (older articles have a Disqus comments system implementation). Please see the Hodinkee Online Community presentation in the reports folder for a more detailed high-level overview.

## Data Preparation
The data for this project is not included in the public facing repo, and neither is the code for scraping it, primarily because the data is proprietary (the total dataset was also almost 2 GB in size). Please contact me if you'd like to discuss these steps in more detail. The project notebooks presume the data is available in csv files in the ~/src/data folder:

| comments	| articles	| tags |
| --- | --- | --- |
| article_num	| article_id	| tag_id |
| comment_id	| article_cat	| tag0 |
| commenter_name	| article_title	| tag1 |
| comment_published	| article_author	| tag2 |
| comment_text	| article_published	| tag3 |
| comment_likes	| article_modified	| tag4 |
| comment_flag	| comm_count	| ... |
| parent_id	| word_count	| tag22 |

Question-comments are heuristically filtered from the full list of comments, with the heuristics described in the FSM notebooks.

## Modeling
The article recommendation is primarily based on the cosine similarity score between the comment text and the article title. A TF-IDF vectorizer is fit on the comments text and used to transform the comments text as well as the article titles. Matrix scores above a very high threshold are returned (along with the comment/title associated metadata) for evaluation.

## Evaluation
A match is graded on the following scale, manually:
1. Perfect
2. Thematically Relevant
3. Related But Different
4. Irrelevant
