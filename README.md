# AutomatingPhysics
Scripts to automate my physics class.

**NOTE**: These scripts are designed to work with the specified url. In this case my course's website. It will not work with any other website unless modified.

## image_downloader.py
This script downloads all assigned problems (images), then creates
a folder according to the chapter to which the problem belongs and saves each image accordingly. 

## presentations.py
In conjunction with a cron job presentations.py checks wether a new class presentation has been uploaded. If so, it will download the newly added. Additionally, it will check which presentations you already have and download any missing ones.
