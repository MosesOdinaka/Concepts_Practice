---
created: 2024-06-09T16:42:33 (UTC +01:00)
tags: []
source: https://intranet.alxswe.com/projects/1213
author: 
---

# Project: 0x00. Pascal's Triangle | Lagos Intranet

> ## Excerpt
> Score: 45.45% (Checks completed: 45.45%)

---
[

](https://intranet.alxswe.com/)

-   [
    
    Home
    
    ](https://intranet.alxswe.com/)
-   [
    
    My Planning
    
    ](https://intranet.alxswe.com/planning/me)
-   [
    
    Projects
    
    ](https://intranet.alxswe.com/projects/current)
-   [
    
    QA Reviews I can make
    
    ](https://intranet.alxswe.com/corrections/to_review)
-   [
    
    Evaluation quizzes
    
    ](https://intranet.alxswe.com/dashboards/my_current_evaluation_quizzes)

___

-   [
    
    Curriculums
    
    ](https://intranet.alxswe.com/dashboards/my_curriculums)
-   [
    
    Concepts
    
    ](https://intranet.alxswe.com/concepts)
-   [
    
    Conference rooms
    
    ](https://intranet.alxswe.com/dashboards/video_rooms)
-   [
    
    Servers
    
    ](https://intranet.alxswe.com/servers)
-   [
    
    Sandboxes
    
    ](https://intranet.alxswe.com/user_containers/current)
-   [
    
    Tools
    
    ](https://intranet.alxswe.com/dashboards/my_tools)
-   [
    
    Video on demand
    
    ](https://intranet.alxswe.com/dashboards/videos)

___

-   [
    
    Peers
    
    ](https://intranet.alxswe.com/users/peers)

___

-   [
    
    Discord
    
    ](https://discord.com/app)
    
    [
    
    My Profile
    
    ](https://intranet.alxswe.com/users/my_profile)
    

Curriculum

Short Specializations Average: 93.94%

-   [
    
    Short Specializations Average: 93.94%
    
    
    
    ](https://intranet.alxswe.com/curriculums/17/observe)
-   [
    
    SE Foundations Average: 93.15%
    
    
    
    ](https://intranet.alxswe.com/curriculums/1/observe)

# 0x00. Pascal's Triangle

AlgorithmPython

-   Weight: 1
-   Project over - took place from Mar 4, 2024 6:00 AM to Mar 8, 2024 6:00 AM
-   An auto review will be launched at the deadline

#### In a nutshell…

-   **Auto QA review:** 5.0/11 mandatory
-   **Altogether:**  **45.45%**
    -   Mandatory: 45.45%
    -   Optional: no optional tasks

## Resources

-   [What is Pascal’s triangle](https://intranet.alxswe.com/rltoken/F458nFkW9StJum2zPI4khg "What is Pascal's triangle")
-   [Pascal’s Triangle - Numberphile](https://intranet.alxswe.com/rltoken/XXMN2RVCCGcF5l5ZnUIv8Q "Pascal's Triangle - Numberphile")
-   [What are Python Algorithms](https://intranet.alxswe.com/rltoken/q5v0xbgrVxG4Nf-fV-BW2w "What are Python Algorithms")

## Additional Resources

-   [Mock Technical Interview](https://intranet.alxswe.com/rltoken/vKf7Spm4xxFMom3x4Jx52g "Mock Technical Interview")

## Must Know

To successfully complete this project, you should revise the following Python concepts:

1.  **Lists and List Comprehensions**:
    
    -   Understand how to create, access, modify, and iterate over lists.
    -   Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.
2.  **Functions**:
    
    -   Know how to define and call functions.
    -   Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.
3.  **Loops**:
    
    -   Use `for` and `while` loops to iterate through sequences.
    -   Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.
4.  **Conditional Statements**:
    
    -   Apply `if`, `elif`, and `else` conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).
5.  **Recursion (Optional)**:
    
    -   While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
    -   Recognize base cases and recursive cases for a function that generates the triangle’s rows.
6.  **Arithmetic Operations**:
    
    -   Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.
7.  **Indexing and Slicing**:
    
    -   Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.
8.  **Memory Management**:
    
    -   Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.
9.  **Error and Exception Handling (Optional)**:
    
    -   Use try-except blocks as needed to handle potential errors, such as invalid input types or values.
10.  **Efficiency and Optimization**:
    
    -   Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
    -   Evaluate and apply optimizations to improve the performance of the solution.

By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.

## Tasks

### 0\. Pascal's Triangle

mandatory

Score: 45.45% (Checks completed: 45.45%)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

-   Returns an empty list if `n <= 0`
-   You can assume `n` will be always an integer

```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x00-pascal_triangle`
-   File: `0-pascal_triangle.py`

Done?! Check your code

×

#### Correction of "0. Pascal's Triangle"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred QA Review

×

#### 0\. Pascal's Triangle

##### Commit used:

-   **User:** \---
-   **URL:** Click here
-   **ID:** `---`
-   **Author:** \---
-   **Subject:** _\---_
-   **Date:** \---

Copyright © 2024 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

```
**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~
```

#### Headers

```
# Big header
## Medium header
### Small header
#### Tiny header
```

#### Lists

```
* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item
```

#### Links

```
[Text to display](http://www.example.com)
```

#### Quotes

```
&gt; This is a quote.
&gt; It can span multiple lines!
```

#### Images

CSS style available: `width, height, opacity`

```
![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
```

#### Tables

```
| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
```

#### Displaying code

````
`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```
````

window.codySettings = { widget\_id: "9993bc72-2258-452b-a4bf-b2fe1ad5e0d7" }; !function(){var t=window,e=document,a=function(){var t=e.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://trinketsofcody.com/cody-widget.js";var a=e.getElementsByTagName("script")\[0\];a.parentNode.insertBefore(t,a)};"complete"===document.readyState?a():t.attachEvent?t.attachEvent("onload",a):t.addEventListener("load",a,!1)}(); <iframe id="_hjSafeContext_49630960" title="_hjSafeContext" tabindex="-1" aria-hidden="true" src="about:blank" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe><iframe id="nr-ext-rsicon" style="position: absolute; display: none; width: 50px; height: 50px; z-index: 2147483647; border-style: none; background: transparent; top: 441px; left: 265px;"></iframe>window.userpilotSettings={token:"NX-b636a33d"};  for(var dl=window.dataLayer||\[\],user=void 0,i=0;i<dl.length;i++)if(dl\[i\].userId){user=dl\[i\];break}user&&user.batch&&user.curriculum&&(userpilot.identify("savanna-"+user.userId.toString(),{cohortId:user.batch.id,cohortName:user.batch.fullNameWithC,locationId:user.batch.schoolLocation.id,locationName:user.batch.schoolLocation.name,curriculumId:user.curriculum.id,curriculumName:user.curriculum.name}),userpilot.reload());

#cody-wrapper .cody-launcher { position: var(--position) !important; left: var(--left) !important; right: var(--right) !important; bottom: var(--launcher-bottom) !important; border-radius: 9999px !important; border: 0 !important; padding: 0 !important; box-sizing: border-box !important; z-index: 999999 !important; overflow: hidden !important; display: flex !important; align-items: center !important; justify-content: center !important; transition: box-shadow, scale 300ms linear !important; animation: cody-launcher-pulse 4s infinite !important; background-color: var(--background-color) !important; color: var(--text-color) !important; cursor: pointer !important; --icon-margin: 12px; --close-icon-margin: 16px; } #cody-wrapper { --position: fixed; --left: unset; --right: 20px; --launcher-bottom: 20px; --frame-bottom: 90px; --background-color: #FBD647; --text-color: #020617; --shadow-color: 251, 214, 71; } @media screen and (max-width: 512px) { #cody-wrapper { --left: unset; --right: 10px; } } #cody-wrapper .cody-launcher:hover { scale: 1.1 !important; } #cody-wrapper .cody-launcher .cody-close-icon { display: none !important; } #cody-wrapper\[data-launcher-open\] .cody-launcher .cody-icon { display: none !important;; } #cody-wrapper\[data-launcher-open\] .cody-launcher .cody-close-icon { display: block !important;; } #cody-wrapper .cody-iframe { z-index: 99999 !important; transition: visibility .5s, opacity .5s linear !important; background-color: #fff !important; position: fixed !important; left: var(--left) !important; right: var(--right) !important; bottom: var(--frame-bottom) !important; height: 75vh !important; width: 448px !important; border-radius: 10px !important; overflow: hidden !important; box-shadow: 0 2px 4px rgba(0, 18, 26, .08), 0 3px 12px rgba(0, 18, 26, .16), 0 2px 14px 0 rgba(0, 18, 26, .2) !important; border: 0 !important; display: none !important; } @media screen and (max-height: 667px) { #cody-wrapper .cody-iframe { height: calc(100vh - 110px) !important; } } @media screen and (max-width: 448px) { #cody-wrapper .cody-iframe { width: calc(100vw - 20px) !important; } } #cody-wrapper\[data-launcher-open\] .cody-iframe { display: block !important; } @keyframes cody-launcher-pulse { 0%, 100% { box-shadow: 0 0 18px 4px rgba(var(--shadow-color), 0.8); } 50% { box-shadow: 0 0 12px 3px rgba(var(--shadow-color), 0.4); } }
