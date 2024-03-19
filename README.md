# DeepMinds
Repo for senior design 1


## Members

- [Matthew Munoz](https://www.github.com/MattMunoz) - Team Leader
- [Matthew Nieves](https://www.github.com/Nieves350) - System Savvy
- [Jinfeng Ouyang](https://www.github.com/ellis51) - Quality Assurance
- [Tajwar Rahman](https://www.github.com/thetajwar2003) - Tech Smith

## Introduction Slides
DeepMinds member introduction [slides](https://docs.google.com/presentation/d/1a_4PFULTmjSpIxwWGtVhbDTeNvAeE5SiUZxqbOzDJ4o/)

## Project Ideas
- Recipe App
  - Fullstack app where users can write blogs, view recipes, and upload their own recipes
  - We can implement a few models such as a recommendation system, creating a recipe from images the user uploads, abd allowing the user to ask for a specific recipe (with dietary restrictions for example)
  - [Full description](https://github.com/thetajwar2003/khuda-lagche)

## Sources
| Source | Summary |
| ------------- | ------------- |
| [Dataset](https://www.kaggle.com/datasets/dansbecker/food-101) | Food-101 Dataset |
| [Techniques for Recommender Systems](https://iopscience.iop.org/article/10.1088/1757-899X/1085/1/012011)  | This paper addresses the different techniques in use when bulding Recommendation Systems(RS). It includes Collaborative and Content-Based filttereing as well as their advantages and dissadvantages. Addtitinally, the Collaborative filterting can be split into both Memory and Model base. For this project it is presumed that Collaborative filtering would be ideal due to its ubiquitousness, easier implementation and rating being received explicitly from the user as the app will be designed to do. A prefereance between memory and model has not been determined at this time. |
| [Recommendation sytems using ML](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702439)  | This paper further illustrates the power and techniques used in Collaborative filtering using item similarity computation. It proposes the use of ML algorithms, such as Clustering, to aid in identifying hidden patters from similar users. It also proposes use of item similarity computations using either Pearson Corrolation or Cosine Vector Similarity.  |
| [Recommender Systems — A Complete Guide to Machine Learning Models](https://towardsdatascience.com/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748) | A serier of leactures to aid in the understanding of the use and application of recommender systems, mostly base on Collaborative filtering. |
| [Recepie Detection](https://medium.com/@imdhawaltank/recipe-detection-of-food-image-using-deep-learning-65eb382aeb38#:~:text=Recipe%20detection%20of%20food%20images%20using%20deep%20learning%20is%20an,in%20various%20image%20recognition%20tasks.) | Am artical that summarizes different echniques and data sets used for image detection and recepie output. It uses Convolutional Nural Networks for the image detectaion and Food-101 dataset consisting of 101 catagories and 101,000 total images. It discusses preprocessing, training and several dificulties in creating this model. |
| [CNN for Food Detection](https://www.researchgate.net/profile/Kiyoharu-Aizawa/publication/266357771_Food_Detection_and_Recognition_Using_Convolutional_Neural_Network/links/542d52930cf29bbc126d2897/Food-Detection-and-Recognition-Using-Convolutional-Neural-Network.pdf) | A paper that oultines the use of CNN for food detection and identifies it a one of the best methods to use when wanting to identify food in images. It determines CNN having an accuray of 93%, which is several percent points higher than the next ;eading method. |
| [Paper on Recipe Generation From Images](https://arxiv.org/pdf/2304.02016.pdf) | This paper compares these monolithic approaches to a lightweight and specialized method based on employing image models to label objects, then serially submitting this resulting object list to a large language model (LLM). |
| [Orignal Recipe Project Done By MIT CSAIL](https://news.mit.edu/2017/artificial-intelligence-suggests-recipes-based-on-food-photos-0720#:~:text=Pic2Recipe%2C%20an%20artificial%20intelligence%20system,a%20similar%20recipe%20to%20it.&text=Dorfman%2FMIT%20CSAIL-,Caption%3A,some%20task%20by%20analyzing%20examples.) | Trained an artificial intelligence system called Pic2Recipe to look at a photo of food and be able to predict the ingredients and suggest similar recipes. |
| [Food Image Classification with Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/8550005) | |
| [Food Classification and Discussions on Different Food Databases](https://ieeexplore.ieee.org/abstract/document/9524498) | |

## References 
- [Dive Into Deep Learning](https://d2l.ai/)
- [Intro to ML](https://openlearninglibrary.mit.edu/login?next=/dashboard)
