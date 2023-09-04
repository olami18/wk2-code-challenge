# wk2-code-challenge

This project focuses on creating a domain model for a restaurant review system similar to yelp. We have three main models: 'Restaurant', 'Customer' and 'Review' which are interconnected to manage restaurant reviews and customer interactions

## Table of contents
. Description 
. Getting started
. Prerequisites
. Installation
. Project structure
. License

## Description
In this project, we stimulate a Yelp-style domain with the following models:

- 'Restaurant': Represents a restaurant which has many reviews.
- 'Customer': Represents a customer, who can write reviews for a restaurant.
- 'Review': Represents a review, which belongs to both a customer and a restaurant

## Getting Started
### Prerequisites

Ensure you have Python 3.10 installed. You'll also need to set up your development environment. You can do this using a tool like Pipenv. To install all project independencies,  run this command
```bash
pipenv install
```
## Installation
Clone this Github repo to your local machine
```bash
git clone https://github.com/olami18/wk2-code-challenge
```
Navigate to the project directory
```bash
cd wk2-code-challenge
```
Set up your virtual environment
```bash
pipenv shell
```
Install the project dependencies
```bash
pipenv install
```

## Project structure
- 'main.py': Contains the main code for the classes and methods.

## License 
This project is licensed under the [MIT] License
(https://choosealicense.com/licenses/mit/)