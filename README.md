# Image Similarity Checker

Euclidean Distance represents the distance between any two points in an n-dimensional space. Since we are representing our images as image vectors they are nothing but a point in an n-dimensional space and we are going to use the euclidean distance to find the distance between them.

Histogram is a graphical display of numerical values. We are going to use the image vector for all three images and then find the euclidean distance between them. Based on the values returned the image with a lesser distance is more similar than the other.

### Code Explanation
The code is written in as a command line argument format, with the arguments as given in the snip.

![image](https://user-images.githubusercontent.com/50414959/126056150-62c1a520-8ee2-4f8e-8292-8c38e5a49b1b.png)


#### Steps done in the code
1. We first read the filename of the target image and the folder through command line arguments, and then pass the filename of the target image to the functions that resize the image, read it and get it's histogram values.
2. We then collect the filenames of the each image in the folder and then store it in an array.
3. We then being comaparision by taking one image from the folder at a time and comapare it with the target image by passing it into a funtion named Score_generator
4. Inside the Score_generator function we get the histogram values of the image that we are comparing and then check the Euclidean distance to generate the dissimilarity score.
5. The individual scores are stored in an array and once all the scores are obtained we collect the image that has the least score.
6. We then return the image that has given us the least score as the image most similar to the target image.

#### Directory Structure to be followed
```
Image Similarity
    │   Image Similarity.py
    │   test.jpg  (Target Image)
    │
    └───Images (Folder where the images being checked are kept)
```


### Sample Input and Output

#### Target Image
![image](https://user-images.githubusercontent.com/50414959/126056077-b7d4157a-2e60-4a07-ab49-2c7bcc8780c1.png)


#### Returned Image
![image](https://user-images.githubusercontent.com/50414959/126056081-cdcad981-c29e-491c-84a9-ec1370890760.png)
