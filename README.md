# Web scrape We Rate Dogs
Code for scraping the [weratedogs](https://www.instagram.com/weratedogs/?hl=en) instagram account for dog pictures and associated ratings and captions.

## Requirements:
- `instaloader`
- `pandas`

## How to run:


**Step 1: Scrape weratedogs instagram**

We will use [instaloader](https://instaloader.github.io/) to crawl every post from the [weratedogs](https://www.instagram.com/weratedogs/?hl=en) meme pages. 

To install instaloader run:

`pip install instaloader`

In this directory then run the command:

`instaloader profile weratedogs`

This will will give us a folder called `weratedogs` with all of the data from the page.

**Step 2: Filter output and extract ratings**

Each post has a comment stored in the text file. We are only interested in posts that have a rating for a dog. These are all in the format N/10, where N is an integer (there are a couple of exceptions that we will ignore to keep things simple). We will use [regex](https://regex101.com/) to find posts with ratings of this format in. We will add this rating and the original comment to the `doggo_ratings.tsv` file, and copy the first image from the post (incase it is a slideshow) into the folder data.

To run the code, run the command:
`python filter_and_extract.py`

**Step 3: Check data**

Check `doggo_ratings.tsv` to make sure all of the ratings have been extracted correctly and that are the same number of images as there are ratings. Once checked you can now use this dataset for your own purposes!

**Additional steps**

- Can you write code to take into account the ratings that do not follow the N/10 rule? (tip: you may want to print out or save the ratings not recorded in the tsv to see if you can spot them.)
- Can you write code to make use of every image of each dog, rather than just the first one in the post for the dataset?
- What kind of model can you train on this dataset? Can you make use of the text description as well as the rating?