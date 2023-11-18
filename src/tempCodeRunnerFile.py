article_tag = soup.find_all(name="h3", class_="css-1kv6qi")

article_texts = []
article_links = []
article_authors = []

for article in article_tag:
    article_text = article.getText()
    article_link = article.get("href")
    article_author = soup.find(name="div", class_="css-1i4y2t3").getText()
    article_texts.append(article_text)
    article_links.append(article_link)
    article_authors.append(article_author)
    
print(f'Article Texts: {article_texts} \n Article Links: {article_links}\n Authors')
