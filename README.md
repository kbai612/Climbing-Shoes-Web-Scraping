# Climbing-Shoes-Web-Scraping

## Project Description

In this project, I utilized the beautiful soup parser to scrape multiple climbing shoe websites to identify what current shoes in the market were discounted. I then compiled this data into a csv to identify trends on these websites related to brand, price, sale frequency and discount amounts.

## Approach

- I first parsed each website's sale page based on the html formatting and took the main content wrapper of each
- I then parsed the main content wrappers for the specific list elements for each shoe that was on the page that would already have a sale on it
- I looped through the list elements and put them into a dictionary dataframe to then append to the main dataframe. In the process I transformed the column data into the correct formats and added some additional elements such as website, shipping costs and discount %
- Once each website had been parsed I sorted the final dataframe and dsplayed all the shoes on sale at the current time

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have Python 3.x installed on your machine. You can download the latest version of [Python](https://www.python.org/downloads/) here.
</br>
You will also need to have Anaconda on your machine. You can download the latest version of [Anaconda](https://www.anaconda.com/) here.

### Installing

## Running the Program
To run the program, simply execute the following command in your terminal:
```
Web Scraping MEC.ipynb
```
The A* algorithm will begin running to find the optimal path to reconstruct the image. Once the algorithm has finished, the reconstructed image will be displayed.
## Built with:
- Python3 - Programming Language Used
## Results
My implementation of the A* algorithm was successful in reconstructing the original image from the shuffled image.
The program displays the shuffled and reconstructed images side by side and the reconstructed image closely matched the original image.

## Author:
- Kevin Bai
