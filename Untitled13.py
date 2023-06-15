#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import pandas as pd


# In[2]:


img_path = 'colorpic.jpg'
csv_path = 'colors.csv'


# In[3]:


dataFrame = pd.read_csv(r"C:\Users\USER\Desktop\CD\colors.csv")
print("Our DataFrame....",dataFrame)


# In[5]:


index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
dataFrame = pd.read_csv(r"C:\Users\USER\Desktop\CD\colors.csv", names=index, header=None)


# In[6]:


print("Our DataFrame....",dataFrame)


# In[7]:


print(len(dataFrame))


# In[8]:


img = cv2.imread(r"C:\Users\USER\Desktop\CD\colorpic.jpg")
img = cv2.resize(img, (800,600))


# In[9]:


clicked = False
r = g = b = xpos = ypos = 0


# In[ ]:


def get_color_name(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, 'R'])) + abs(G - int(csv.loc[i, 'G'])) + abs(B - int(csv.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = dataFrame.loc[i, 'color_name']
    return cname


# In[ ]:


def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LEFTBUTTONBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[ ]:


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)


# In[ ]:


while True:
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)
        text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)
        if r+g+b >=600:
            cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)
            
        clicked = False    
            
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destryAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




