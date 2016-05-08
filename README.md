## ***VisionViewer***: Images & Video frames filter expert. ##


### What is this repository for? ###

* If you are working with image & video frames effect, this app will make your life much easier. Load images & videos, select your favourite filters and you will have the result in a second. You can edit your results with the intention to get exactly what you need. 
* Also you could get the code that makes your favourite effects. So if you’re a developer and you are working with some new filters, you could have some examples for your work. 
* And if you are working with images, you will see on the screen some nice filters & their result.
* Version: 1.0
### How do I get set up? ###
* If you want to try this software, you need to download first or clone repository.
* Use your favourite Python IDE, i use "PyCharm" to open the project. 
* Go to VisionViewer.py file in the Viewer package & click run.

### Contribution guidelines ###
* If you want to make this app a better app, you could join us and help a lot people. We want to have as many filters as we can. So if you like python or you are a developer it is very easy to make filters. We work with OpenCV 2.4.11, Numpy, Scipy libraries & of course Python 2.7. 
* OpenCV will help you with image effect & Computer vision.
* Numpy: will give you a n-dimension array with excellent functions to work with.
* Scipy: If you need to code difficult math function, you will love this library.
* Python it is very versatile and gives you the opportunity to use a lot of open libraries on internet.

### Resources
* Homepage: <http://visionviewer.org>
* Docs: <http://docs.visionviewer.org/>
* Issue tracking: <https://bitbucket.org/rainer85ah/visionviewer/issues>


### Contributing
Please read before starting work on a pull request:
If your filter work in our project, we are very pleases to improve our app.
We have really nice tutorials and examples about programming filter images. Check it out!
Together we are stronger. Simple right.

### Examples:
![VisionViewer Examples.jpg](https://bitbucket.org/repo/B5jE66/images/3078382406-VisionViewer%20Examples.jpg)

```
#!python
def canny(self):
        """ The Canny method apply the canny algorithms to the image received on __init__
        :return: an image with the edges of the original photo. With some setting 
        by default or a "private" method to do it with different values.
        """
        if self.lower == 0 and self.upper == 0:
            blur = cv2.GaussianBlur(self.gray_image, (3, 3), 0)
            self.edge_image = cv2.Canny(blur, self.low_threshold, self.max_threshold)
            return self.edge_image
        else:
            return self.__canny2()
```
```
#!python
def __canny2(self):
        """
        :return: an image with the edges. If the user select some setting, 
        we call this "private" method to do the same process with the new values.
        """
        blur = cv2.GaussianBlur(self.gray_image, (3, 3), 0)
        self.edge_image = cv2.Canny(blur, self.lower, self.upper)
        return self.edge_image
```


### Summary of guidelines:
* One pull request per issue;
* Choose the right base branch;
* Always it´s good to have your documentation. Remember we are a team;
* Git will help you to upload your work;