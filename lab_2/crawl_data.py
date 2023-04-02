from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def get_movie_link(url, n_movies, top_movie):
    driver = webdriver.Chrome('edgedriver.exe')
    driver.get(url)

    # Set initial empty list for each element:
    movie_link = []

    # Grab the block of each individual movie
    if top_movie:
        block = driver.find_elements(By.CLASS_NAME, 'lister-item-header')
    else:
        block = driver.find_elements(By.CLASS_NAME, 'titleColumn')
    # Set up for loop to run through n_movies
    for i in range(0, n_movies):
        flink = block[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
        movie_link.append(flink)
    driver.quit()
    return movie_link


def get_review_link(movie_link):
    review_link = []
    for flink in movie_link:
        driver = webdriver.Chrome('edgedriver.exe')
        driver.get(flink)
        review_flink = driver.find_element(By.XPATH, "//a[text()='User reviews']").get_attribute('href')
        review_link.append(review_flink)
        driver.quit()
    return review_link


def get_reviews(url, n_movies, n_reviews_per_movie, csv_name, top_movie):
    movie_link = get_movie_link(url, n_movies, top_movie)
    review_link = get_review_link(movie_link)
    review_df = pd.DataFrame(columns=['user_name', 'title', 'rating', 'date', 'review'])
    for link in review_link:
        driver = webdriver.Chrome('edgedriver.exe')
        driver.get(link)
        driver.implicitly_wait(
            1)  # tell the webdriver to wait for 1 seconds for the page to load to prevent blocked by anti spam software

        # Set up action to click on 'load more' button
        page = 1  # Set initial variable for while loop
        while page < n_reviews_per_movie / 25:  # 1 page has 25 reviews
            try:
                load_more = driver.find_element(By.ID, 'load-more-trigger')
                load_more.click()
                page += 1
            except:
                break

        review = driver.find_elements(By.CLASS_NAME, 'review-container')
        # Set list for each element:
        title = []
        content = []
        rating = []
        date = []
        # run for loop to get
        for n in range(0,
                       len(review)):  # maybe the movie does not have n_reviews_p_movie reviews, so we just get the max reviews
            try:
                ftitle = review[n].find_element(By.CLASS_NAME, 'title').text
                fcontent = review[n].find_element(By.CLASS_NAME, 'content').get_attribute("textContent").strip()
                frating = review[n].find_element(By.CLASS_NAME, 'rating-other-user-rating').text
                fdate = review[n].find_element(By.CLASS_NAME, 'review-date').text

                # Then add them to the respective list
                title.append(ftitle)
                content.append(fcontent)
                rating.append(frating[:frating.find('/')])
                date.append(fdate)
            except:
                continue
        # Build data dictionary for dataframe
        data = {'title': title,
                'rating': rating,
                'date': date,
                'review': content
                }
        # concat with the root dataframe
        review_df = pd.concat([review_df, pd.DataFrame(data)])
        driver.quit()
    review_df.to_csv(csv_name + '.csv', index=False)
