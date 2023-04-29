---
layout: default
title: Side Project - iCloud Control Script
---

# Side Project: iCloud Control Script

* * *

## Side Project Work Repository

Written in Swift 5 using Xcode 14 for macOS 13.

Link: <a href="https://github.com/tkjsung/iCloud-Control-Script" target="_blank">https://github.com/tkjsung/iCloud-Control-Script</a>

## About the Side Project

### The Problem

iCloud, a service provided by Apple Inc., is a cloud service that allows users to store and sync data (e.g., documents, photos, videos, and backups) across Apple devices. Within this service is an application called iCloud Drive, where users can access their documents/files. iCloud Drive is similar in function to Google Drive (operated by Google) and OneDrive (operated by Microsoft).

On Apple's Mac computers, iCloud Drive files would be downloaded when there is ample amount of local computer storage. As computer storage gets used up, the local copy of the iCloud Drive files would be "offloaded". In other words, the files are deleted from the computer to save space. However, they would still be available on iCloud. Some users do not want macOS to decide when files should be offloaded and wants better control of which files stay on local computer storage. To solve this issue, Apple has implemented the "Download Now" and "Remove Download" options in the secondary options menu ("right-click" or "control-click" on macOS) since macOS Catalina (macOS 10.15).

However, Apple's solution for removing local iCloud files is not perfect. **If an iCloud folder does not have all its contents downloaded and has a non-zero amount of downloaded files, it is not possible to remove local copies of the iCloud files by right-clicking on the folder.** One would need to click the "Download Now" button to download the contents of the entire folder before the "Remove Download" button would appear when right-clicking on the folder. While this can be solved by selecting individual files inside a folder one-by-one, this is tedious and takes a lot of time. Not only is it tedious, it is also not worth the time to do so as macOS may decide to download these files again arbitrarily. As of the latest macOS release, macOS Ventura (macOS 13), this behaviour persists. The script that I have written solves this problem; local iCloud files can be removed without downloading the entire folder or manually removing individual files.

### The Inspiration

The project was inspired by Robbert Brandsma's (Obbut) GitHub project iCloud Control (available here: [https://github.com/Obbut/iCloud-Control](https://github.com/Obbut/iCloud-Control)). The developer of said project deemed it unnecessary to continue developing the Finder extension as Apple has implemented the download/remove local file feature in macOS Catalina (macOS 10.15), which at the time is built for Intel-based Macs. In other words, the Finder extension runs Intel x86 instruction set and works via Rosetta 2 on Apple silicon Mac computers. In the future, though, Apple will remove support for x86 applications and the instruction set, which will render the iCloud Control extension unusable. To ensure I personally can continue to use a form of iCloud Control, I created this script.

### Why This Solution

As I have no expertise in macOS app development and I am not from a software background, I did not know how to modify and build the iCloud Control Finder extension for Universal/Apple silicon. Therefore, I opted to piece together a command line tool, which is called iCloud Control Script. This script's only functionality is removing local copies of iCloud files, which is what I used the most and solves the only short-coming of Apple's implemented solution.

There are other ways to do this, such as using the ``brctl evict`` command in Terminal (which manages CloudDocs daemon. Use ``man brctl`` to learn more about its usage), but I found it to be less reliable in removing local files.

<br><br>

[Back to Home Page](/md_files/home)
