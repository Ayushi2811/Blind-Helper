# Blind-helper

# _ **1.INTRODUCTION** _

Blind Helper is a hardware cum software project that will be designed keeping in mind the obstacles faced by the blind people.

As we all know that there has not been a fixed solution for the blind to make them independent of others .We have just made few homes for them and we feel that we have done our duties towards them but this is not just what they deserve.They deserve to be self reliant in themselves.

Keeping these above scenario in mind we want to develop an app which will detect object in their pathway and will alert them of the same so that they walk properly without any hazard.

Basically we want to develop an android app by using flutter which will use google map data as its base so that it can detact the traffic nearby or simply the location of the person .

Also we&#39;ll take two thermal cameras in the neckband so that they keep record of the object coming closer to them and after detacting the object the camera will then send this information to the android app which will further make use of the open CV i.e., computer vision and then it will send the further command to the band which will then speak a message as an alert by making use of the google voice.

The person simply just needs to put the phone conating the app in his/her pocket and the app will automatically play in the background .The person doesn&#39;t have to take the trouble to operate it,Its self functionally app.

So if this idea works as per planned we&#39;ll be able to help a lot many blind crowd out there which donot have any permanent solution.

# _ **2.Flow of the project** _

**2.1**

![](RackMultipart20220513-1-88ich1_html_8378f153c719215d.png)

**2.2**

![alt_text](RackMultipart20220513-1-88ich1_html_9d2de5b6edbd8f09.jpg)

**2.3**

![](RackMultipart20220513-1-88ich1_html_c76eacba7055e244.jpg)

**2.4**

![](RackMultipart20220513-1-88ich1_html_67f9c316539410a6.jpg)

**2.5**

![](RackMultipart20220513-1-88ich1_html_3304f9bfb25a5ba5.png)

# _ **3.IMPLEMENTATION** _

**3.1 Design /look of the hardware :**

![](RackMultipart20220513-1-88ich1_html_e5403d13c1a7b35d.jpg) ![](RackMultipart20220513-1-88ich1_html_82b60b7155db3a20.jpg)

**3.2** Mask R-CNN Demo

The Mask R-CNN model addresses one of the most difficult computer vision challenges: image segmentation. Image segmentation is the task of detecting and distinguishing multiple objects within a single image. In particular, Mask R-CNN performs &quot;instance segmentation,&quot; which means that different instances of the same type of object in the input image, for example, car, should be assigned distinct labels.

3.2.1.Input:

![](RackMultipart20220513-1-88ich1_html_763ae8e8f841aa72.png)

3.2.2.Output:

![](RackMultipart20220513-1-88ich1_html_5cab744196afa0c7.png)

**3.3 Teachable Machine view**

Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible to everyone.

1.Gather- and group your examples into classes, or categories, that you want the computer to learn.

**2** Train-Train your model, then instantly test it out to see whether it can correctly classify new examples.

### **3** Export

Export your model for your projects: sites, apps, and more. You can download your model or host it online for free.

![](RackMultipart20220513-1-88ich1_html_a115c4efef9edbf.jpg)

![](RackMultipart20220513-1-88ich1_html_ac6598af049ee7f7.jpg)

![](RackMultipart20220513-1-88ich1_html_f758a161b2a9fcc4.jpg)

![](RackMultipart20220513-1-88ich1_html_d1f50c504329ede8.jpg)

![](RackMultipart20220513-1-88ich1_html_2080136caf0034fc.jpg)

![](RackMultipart20220513-1-88ich1_html_3478dade8022299e.jpg)

![](RackMultipart20220513-1-88ich1_html_bde8b9bee36a5423.jpg)

![](RackMultipart20220513-1-88ich1_html_caaf38decd450722.jpg)

**3.4 Object detection output**

On running the object detection open CV modal on spyder platform and passing the input image in the anaconda command prompt we receive the following output results on the screen.

**3.4.1**

![](RackMultipart20220513-1-88ich1_html_4ecd347792652745.png)

**3.4.2**

![](RackMultipart20220513-1-88ich1_html_e4adb1c0f9f51ad8.jpg)

**3.4.3**

![](RackMultipart20220513-1-88ich1_html_803e0987904bf547.jpg)

# _ **4.Description of audio speaker** _

In this project ,above,we can see that we have implemented the object detection so far so good.We also added voice alarm file to the spyder platform which which convert the text to speech module using gTTS libraries.

A s we cannot provide the audio in the report so it is just a small description that whatever text we give as input on the spyder ,the same audio file is generated or created and it auto plays itself and we hear the sound of whatever the input text we have given in the program and run through anaconda prompt.

So this was all about the text to audio voice alarm.
