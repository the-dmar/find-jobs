<div align="center">
    <h1>Job Finder</h1>
    <p>A python script I use to look for jobs</p>
    <br>
</div>

## Summary

This bot opens jobs using mouse and keyboard input, checks whether they meet certain criteria, and saves them if they do.

## How it works

The program clicks on each job ad, selects all of the text within that ad, and copies it. I then get data from the clipboard, and check for certain terms using a regular expression. If the ad does not include certain terms, the bot saves it for me, then moves on to the next ad. If there are no more ads on screen- page down is pressed, and the program repeats the process again. If the "next page" element is present- it will press that and start over, otherwise it presses page down and repeats the process.
