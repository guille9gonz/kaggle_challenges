## **Spaceship Titanic Challenge**
Welcome to the year 2912, where your data science skills are needed to solve a cosmic mystery. We've received a transmission from four lightyears away and things aren't looking good.
The Spaceship Titanic was an interstellar passenger liner launched a month ago. With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.

While rounding Alpha Centauri en route to its first destination—the torrid 55 Cancri E—the unwary Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud. Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!
To help rescue crews and retrieve the lost passengers, you are challenged to predict which passengers were transported by the anomaly using records recovered from the spaceship’s damaged computer system.

### Project structure
**``model``**: Training data analysis and preprocessing. Various models built and trained, and selected the best.  
**``predictions``**: Testing data preprocessing, predictions and submission.  
**``cat_utils.py``**: Functions to handle categorical columns in testing same way as in training.  
**``num_utils.py``**: Functions to handle numerical columns in testing same way as in training.  
**``model2``**: Different preprocessing that increased the score for the test dataset.  

### Results and conclusions:
Several ensemble models were trained and got really a good ``accuracy_score``, from 77.97% to 100%. Finally the Histogram-Based Gradient Boosting model was selected for the submission with a 100% of accuracy in training.  
The Kaggle submission scored **64%**, possibly due to improper test data processing or data leakage during training.  

(**new!**) Created a new notebook with a different treatment of the datasets. Obtained a 80.25% of accuracy in training and **77.99%** in testing
