# -*- coding: utf-8 -*-
"""
Canny Package contain the file CannyBuilder.py, that have implemented the class CannyBuilder.
This class will receive an image in (color/gray) and will return an image with the edges
of the original as result, you will see black image with the edges or shape of the objects on the original image
on it.

The Canny edge detection algorithm can be broken down into 5 steps:
    Step 1: Smooth the image using a Gaussian filter to remove high frequency noise.
    Step 2: Compute the gradient intensity representations of the image.
    Step 3: Apply non-maximum suppression to remove “false” responses to to edge detection.
    Step 4: Apply threshold using a lower and upper boundary on the gradient values.
    Step 5: Track edges using hysteresis by suppressing weak edges that are not connected to strong edges.

The smallest value between threshold1 and threshold2 is used for edge linking.
The largest value is used to find initial segments of strong edges.

The Canny Edge detector was developed by John F. Canny in 1986.
Also known to many as the optimal detector, Canny algorithm aims to satisfy three main criteria:
Low error rate: Meaning a good detection of only existent edges.
Good localization: The distance between edge pixels detected and real edge pixels have to be minimized.
Minimal response: Only one detector response per edge.
"""