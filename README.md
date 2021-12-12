# Dark-Horse-Comics-Converter
This script written in Python helps you download and convert your Dark Horse Comics to a CBZ format.

*It uses the following python modules:-*

*os, json, tarfile, zipfile, shutil, requests, googlesearch, bs4, webbrowser*

*Make sure these all are installed/available on your system.*

# Disclaimer

THIS SCRIPT IS NOT MEANT TO PROMOTE OR FACILIATE PIRACY, BUT RATHER TO BE A LEARNING TOOL AND TO BACKUP YOUR OWNED COMICS FOR PERSONAL USAGE. PLEASE TAKE CARE IF THAT IS LEGAL IN YOUR COUNTRY OR NOT. 

**How to use:-** 

1) Open your browser and login to https://digital.darkhorse.com/accounts/login/?next=/
2) Search and open the book you want to download. **REMEMBER this will only work for books you own! Nothing else.** Your books/purchases will be located here https://digital.darkhorse.com/accounts/manage/order_history/ 

Your book page url will look something like this:- 
https://digital.darkhorse.com/books/5baf9f8140344ca1879a74669e3abd42/world-of-the-witcher-hc

3) Click on "Read Now" and then copy the page URL. 
4) Download or clone this repository to your PC.
5) Double-click on "url.py" and paste the url that you copied in the earlier steps. This will open the download page and start downloading your book as "book.tar".
6) Double-click on "full script v2.py" and enter the path of the book you downloaded **without quotes!**

It will now do the following steps automatically:- 
i) Extract the tar file
ii) Rename and convert the files to images in the correct order.
iii) Zip it into a CBZ file.

7) Finish. 

Now you can go the folder where you downloaded the "book.tar" file and see your comic there. You can safely delete the book.tar file now if ya want.


**For the record:-**

This is WEB-DL, not WEBRip or Scan.


**Q) Why is this downloaded comic smaller in size than a comic uploaded by Digital Empire or someone from there group?**

A) This is a mid-quality WEB-DL by Dark Horse Digital themselves. The comics uploaded by Digital Empire is not a WEB-DL, but actually scans of actual comics. So they have higher resolution scans in their uploaded comics. Personally, I prefer the darkhorse comics' color than the scanned ones, but the scanned ones are of higher quality than these as they are HQ print scans.
