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
  - The ML aspect of the project will be implemented on top of a recepie app. The recepie app will work much in the same way other recepie app works. The full deatils of it can be found [here](https://github.com/thetajwar2003/khuda-lagche)

- Senior Design Project
  - The main aspect of the project will be a recommendation system that creates personalized recommendations for each user of the app. The users will obtain this personalization based on past preferences, whether it's a like or dislike, compared to what other similar users of the app prefer. For example, if two users have similar tastes in recipes and are more closely related we can assume that they will like a similar recipe in the future, so if one of them likes a recipe the other one has not tried we can recommend said recipe to the other user.
  - If time permits, the project will also attempt to implement a function within the app that will allow the user to upload a picture of a dish that they tried and would like to know how to make. The app will then identify the dish in the image and provide a recipe to make that dish. Specifically, if a user uploads a picuture of a margarita pizza, they can upload a picture of the pizza they like and the app will provide a recipe for the dish. 

## Existing Projects
| Source | Summary | Considerations |
| ------------- | ------------- | ------------- |
| [Recepie Recomendation](https://medium.com/web-mining-is688-spring-2021/a-recommendation-engine-for-the-recipes-by-using-collaborative-filtering-in-python-72171b52e7a2) | A recepie recommendation system that uses collaborative filtering to predict what a user will like based on other similar users preferences.  | The large size in the dataset made for having to limit the input of the data due to memory constraints. Additinally, the project had a decent amount of sparcity in the users and the data wihich could result in deterioraed performance. |
| [Recepie Detection](https://medium.com/@imdhawaltank/recipe-detection-of-food-image-using-deep-learning-65eb382aeb38#:~:text=Recipe%20detection%20of%20food%20images%20using%20deep%20learning%20is%20an,in%20various%20image%20recognition%20tasks.) | An artical that summarizes different techniques and data sets used for image detection and recepie output. It uses Convolutional Nural Networks for the image detectaion and Food-101 dataset consisting of 101 catagories and 101,000 total images. It discusses preprocessing, training and several dificulties in creating this model. | The ability to decern the nuances in the different dishes. The look, coloraation, and consistency of a dish can change based on the dish making it hard to determin a dish if it's different from the norm. Additionally, two dishes can look simiar but be very different, a consideration that must be addressed. |

## Sources
| Source | Summary |
| ------------- | ------------- |
| [Techniques for Recommender Systems](https://iopscience.iop.org/article/10.1088/1757-899X/1085/1/012011)  | This paper addresses the different techniques in use when building Recommendation Systems(RS). It includes Collaborative and Content-Based filtering as well as their advantages and disadvantages. Addtitinally, the Collaborative filtering can be split into both Memory and Model base. For this project it is presumed that Collaborative filtering would be ideal due to its ubiquitousness, easier implementation and rating being received explicitly from the user as the app will be designed to do. A preference between memory and model has not been determined at this time. |
| [Recommendation sytems using ML](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702439)  | This paper further illustrates the power and techniques used in Collaborative filtering using item similarity computation. It proposes the use of ML algorithms, such as Clustering, to aid in identifying hidden patters from similar users. It also proposes use of item similarity computations using either Pearson Corrolation or Cosine Vector Similarity.  |
| [Recommender Systems — A Complete Guide to Machine Learning Models](https://towardsdatascience.com/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748) | A serier of leactures to aid in the understanding of the use and application of recommender systems, mostly base on Collaborative filtering. |
| [CNN for Food Detection](https://www.researchgate.net/profile/Kiyoharu-Aizawa/publication/266357771_Food_Detection_and_Recognition_Using_Convolutional_Neural_Network/links/542d52930cf29bbc126d2897/Food-Detection-and-Recognition-Using-Convolutional-Neural-Network.pdf) | A paper that outlines the use of CNN for food detection and identifies it a one of the best methods to use when wanting to identify food in images. It determines CNN having an accuray of 93%, which is several percent points higher than the next ;eading method. |
| [Paper on Recipe Generation From Images](https://arxiv.org/pdf/2304.02016.pdf) | This paper compares these monolithic approaches to a lightweight and specialized method based on employing image models to label objects, then serially submitting this resulting object list to a large language model (LLM). |
| [Orignal Recipe Project Done By MIT CSAIL](https://news.mit.edu/2017/artificial-intelligence-suggests-recipes-based-on-food-photos-0720#:~:text=Pic2Recipe%2C%20an%20artificial%20intelligence%20system,a%20similar%20recipe%20to%20it.&text=Dorfman%2FMIT%20CSAIL-,Caption%3A,some%20task%20by%20analyzing%20examples.) | Trained an artificial intelligence system called Pic2Recipe to look at a photo of food and be able to predict the ingredients and suggest similar recipes. |
| [Food Image Classification with Convolutional Neural Networks](https://ieeexplore.ieee.org/abstract/document/8550005) | The paper covers topics such as dataset selection, image pre-processing techniques, CNN model architecture design, evaluation of model performance, and comparison with existing approaches. In their approach, a CNN is built from scratch for identifying foods and utilizes a pre-trained Inception V3 model, which has been pre-trained on a large-scale dataset like Imagenet. |
| [Image-Based Food Classification and Volume Estimation for Dietary Assessment](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9082900) | Discusses deep learning techniques, such as GoogLeNet with inception modules, for food recognition tasks and comprehensive studies that were conducted on public datasets like UEC-FOOD100, UEC-FOOD256, and Food101. Deep learning method for volume estimation outlined: single RGB image captured, depth map estimation/3D shape completion, 3D model reconstruction, volume estimation (useful for food volume and dietary assessment).  |
| [Crowd Data Sourcing](https://dl.acm.org/doi/abs/10.1145/2737817.2737819?casa_token=ocIch4ZGuFMAAAAA:O8GE71Qk3WiUaBiAGAVARa42ggjRkmP8IN2WaPeZ39qDTn3431sE82BlvXEuqctu0eVex6VGAho) | This paper discusses the idea of building/improving a database through crowd data sourcing (allowing users to contribute to the database). Some topics discussed are: other platforms that make use of crowd sourcing like wikipedia and movie review websites, some challenges that are faced when implementing such features (ex. misuse and reliability), and the foundations for efficiently applying such a method. |

## Datasets
[Food-101 Dataset](https://www.kaggle.com/datasets/dansbecker/food-101) 
## References 
- [Dive Into Deep Learning](https://d2l.ai/)
- [Intro to ML](https://openlearninglibrary.mit.edu/login?next=/dashboard)
