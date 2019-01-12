# Mastodon Domain Block List Generator

Creates a simple HTML table for pasting into an instance's about page.

## Instructions

## Create a source file

Copy and paste the list of blocked domains from the admin into a plain text file. Don't include the headers. (Sorry I didn't figure out a way to automate this part.) You can leave in the "reject media files" and "undo" fields, though. This will filter them out.

Name the file ```domainblocks.txt``` (or edit the code accordingly).

## Create the HTML:

``` python3 domainblocklist.py ```
