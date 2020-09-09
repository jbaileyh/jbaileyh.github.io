---
title: LidaRt
author: Joseph Bailey
date: '2019-08-25'
slug: Lidar, R and Blender
categories: [R, Blender, Lidar]
tags: [r]
draft: no
---

As I may have eluded to in previous work or other areas of the internet. I'm a big fan of Geospatial data. I've used it a lot in my previous jobs and I have a bit of a passion for maps. 

Because of this, I also like to create Ray Traced scenes using freely available data and tools. I'm not sure why, but I find raytracing geographic scenes inredibly satisfying so I often do it to make art for my friends. It's relatively easy to make it personal to them by choosing a place of meaning and it's also fun to add small references to their passions where possible. 

There's a lot of tools out there that make this possible and generally this includes things like:

- R
- QGIS
- Blender
- FME
- Python
- Houdini

I've use these before but as I'm an R user I use R for data manipulation and preparation and sometimes QGIS for checking things and visualising large data sets. In this case I've been using the [Environment Agency's Lidar data resources](https://data.gov.uk/dataset/f0db0249-f17b-4036-9e65-309148c97ce4/national-lidar-programme) and preprocessing it in R to make the greyscale imagery that is needed for raytracing. 

![Elevation Encoded Image](waltham_circle.png)

Once I've got the base image, I can import it into Blender and the world is one's oyster so to speak. By varying the style and elevation of the light it's possible to create pleasing cityscapes that have high levels of detail thanks to the Lidar data (some of which is available at 25cm resolution!). 

![Ray Traced](final_small.png)

It's even possible to encode things like colour by height of the buildings to enable all kinds of unusual combinations. 

![Rainbow Ray Traced](final_rainbow_small.png)

This workflow took a while to get set up. Now i've done it however, it's reasonably simple to go from Lidar -> Rendered image by using R, Python in Blender and plain old Blender. If you're looking to learn more i'd recommend checking out [Rayshader](https://www.rayshader.com/) in R and [Daniel Huffman's blog](https://somethingaboutmaps.wordpress.com/2017/11/16/creating-shaded-relief-in-blender/). 



