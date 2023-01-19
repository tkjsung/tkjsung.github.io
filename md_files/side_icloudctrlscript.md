---
layout: default
title: Side Project - iCloud Control Script
---

# Side Project: iCloud Control Script

* * *

## Side Project Work Repository

Written in Swift in Xcode 14.2 for macOS 13.1.

Link: <a href="https://github.com/tkjsung/iCloud-Control-Script" target="_blank">https://github.com/tkjsung/iCloud-Control-Script</a>

## About the Side Project

The project was inspired by Robbert Brandsma's (Obbut) GitHub project iCloud Control (available here: [https://github.com/Obbut/iCloud-Control](https://github.com/Obbut/iCloud-Control)). The developer of said project deemed it unnecessary to continue developing the Finder extension as Apple has implemented the download/remove local file feature in macOS Catalina (macOS 10.15), which at the time is built for Intel-based Macs. In other words, the Finder extension runs Intel x86 instruction code. In the future, though, Apple will remove support for x86 applications, which will render the iCloud Control extension unusable. To ensure I personally can continue to use a form of iCloud Control, I created this script.

Apple's solution is not ideal for removing local iCloud files. If an iCloud folder has a non-zero amount of downloaded files, it is not possible to remove local copies of the iCloud files by using the secondary options (right click). One would need to click the "Download Now" button to download the entire folder before the "Remove Download" button would appear. Alternatively, downloads can be removed by visiting each file manually, which is tedious. This script solves this problem; local iCloud files can be removed without downloading the entire folder or manually removing individual files.

As I have no expertise in macOS app development and I am personally not from a software background, I did not know how to modify and build the iCloud Control Finder extension for Universal/Apple Silicon. Therefore, I opted to piece together a command line tool, which is called iCloud Control Script. This script's only functionality is removing local copies of iCloud files, which is the function I used the most.

<br><br>

[Back to Home Page](/md_files/home)
