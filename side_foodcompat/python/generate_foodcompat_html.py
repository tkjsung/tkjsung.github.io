# generate_foodcompat_html.py
# Purpose: Generate Food Compatibility HTML site
# Side Note: This file is used for Food Compatibility Project
# Date: May 5, 2023

import os
import sys
import time
import pandas as pd

website_ver = "1.0.1"
food_zh = []
food_compat_mark = []
food_zh_reason = []

class createNewFolder:
    def __init__(self):
        self.proj_path = os.getcwd()
        self.date_format:str
        self.today_list:list
        self.new_folder_name:str
        self.folder_type:str = "html"

    # 1a. Get the date and time for folder naming and automatically generated text file.
    def get_datetime(self):
        now = time.localtime()
        self.today_list = [now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec]

    # 1b. Create folder to put all the files in
    def create_folder(self):
        # global date_format
        self.date_format = f"{self.today_list[0]}-{self.today_list[1]:02d}-{self.today_list[2]:02d} @ {self.today_list[3]:02d}.{self.today_list[4]:02d}.{self.today_list[5]:02d}"
        self.new_folder_name = f"{self.proj_path}/{self.folder_type}/{self.date_format}"
        os.mkdir(self.new_folder_name)
        print(f"Folder created: \"{self.date_format}\" (at {self.proj_path}/{self.folder_type})")

    # 1c. Create text file that tells me when the CSV file was generated
    def create_textfile(self):
        filepath_today = f"{self.new_folder_name}/{self.date_format}.txt"
        txt_content = f"{self.today_list[0]}-{self.today_list[1]:02d}-{self.today_list[2]:02d} @ {self.today_list[3]:02d}:{self.today_list[4]:02d}:{self.today_list[5]:02d}"
        with open(filepath_today, 'w+') as f:
            f.write(f"This folder is created on {txt_content}.\n")
            f.write(f"This text file is automatically generated by Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}.")
    
    # Automatically run all functions within this class, then output back to appropriate place as needed.
    def auto_run(self):
        self.get_datetime()
        self.create_folder()
        self.create_textfile()


# TODO: Continue working on this function in the future
# TODO: In the future, read a template of a HTML page. Then, simply replace the lines using Python
def generate_zh_website(write_filepath:str):
    write_filepath = write_filepath + "/food_compat_prod.html"
    print(f"{write_filepath}")
    
    f = open(write_filepath, 'w+')
    # with open(write_filepath, 'w+') as f:
    f.write("<!DOCTYPE html>\n")
    f.write('<html lang="en" dir="ltr">\n')

    # HTML Head Content
    f.write("<head>\n")
    f.write('<meta charset="utf-8" />\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
    f.write('<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"\n>')
    f.write("<title>食物相剋 / Food Compatibility | Ke-Jun (Tom) Sung's Website</title>\n")
    f.write('<link rel="stylesheet" href="/side_foodcompat/css/food_compat.css">\n')
    f.write('<link rel="shortcut icon" type="image/x-icon" href="/favicon_io/favicon.ico">\n')
    f.write('<link rel="apple-touch-icon" type="image/png" href="/favicon_io/apple-touch-icon.png">\n')

    # Google Analytics
    f.write("<script>\n")
    f.write("(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n")
    f.write('(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n')
    f.write('m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n')
    f.write("})(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n")            
    f.write("ga('create', '{{ site.google_analytics }}', 'auto');\n")
    f.write("ga('send', 'pageview');\n")
    f.write('</script>\n')
    f.write('<script async src="https://www.googletagmanager.com/gtag/js?id=G-PH3B1H4D6B"></script>\n')
    f.write('<script>\n')
    f.write('window.dataLayer = window.dataLayer || [];\n')
    f.write("function gtag(){dataLayer.push(arguments);}\n")
    f.write("gtag('js', new Date());\n")
    f.write("gtag('config', 'G-PH3B1H4D6B');\n")
    f.write('</script>\n')
    f.write("</head>\n")

    # HTML Body Content
    f.write('<body onload="page_loaded()">\n')
    f.write('<h1>食物相剋 / Food Compatibility</h1>\n')
    f.write('<p>Note: Currently only supports Chinese (Traditional) food items. English support to come in a future update.</p>\n')
    f.write('<p><button class="collapseAll" id="collAll">Collapse All</button></p>\n')
    f.write("<div>\n")
    f.write('<input type="text" id="compat_searchbox" placeholder="Search for food items ..." title="Type in a food item" onkeypress="check_enter_key(event)">\n')
    f.write('<input type="button" id="compat_searchbutton" value="Search" name="Search" onclick="compat_search()">\n')
    f.write('</div><br>\n')
    f.write('<p id="text_results">Results:</p>')

    # HTDML Body: Food Compatibility Food Content
    for index in range(0, len(food_zh)):
        f.write(f'<button class="collapsible">{food_zh[index]}</button>\n')
        f.write('<div class="content">\n')
        f.write(f"{food_zh_reason[index]}\n")
        f.write('</div>\n')

    # HTML Body: Footnote
    f.write('<p class="footnote">\n')
    f.write(f'v{website_ver} \n')
    f.write('(<a href="/side_foodcompat/md/food_compat_changelog">Changelog</a>)</p>\n')
    f.write('<p class="footnote">\n')
    f.write('Copyright &copy; <script>document.write(/\d{4}/.exec(Date())[0])</script> Ke-Jun (Tom) Sung. All rights reserved.</p>\n')

    # HTML Body: Import JavaScript
    f.write('<script src="/side_foodcompat/js/collapse_expand.js"></script>\n')
    f.write('<script src="/side_foodcompat/js/filter_search.js"></script>\n')

    f.write("</body>\n</html>")
    f.close()
    

def data_import():
    global food_zh, food_zh_reason, food_compat_mark
    df = pd.read_csv(os.path.join(os.getcwd(),'data/FoodCompatibility.csv'))
    for index in range(0, df.item_zh.size):
        food_compat_mark.append(df.compatibility[index])

        tmp = df.item_zh[index].split(";")
        tmp_str = ''
        for i2, item2 in enumerate(tmp):
            if i2 == len(tmp)-1:
                tmp_str += f'{item2}'
            else:
                tmp_str += f'{item2} & '

        if food_compat_mark[index] == "good":
            tmp_str += " &#9989"
            food_zh_reason.append(f"GOOD &#x2705: {df.reason[index]}")
        else:
            tmp_str += " &#10062"
            food_zh_reason.append(f"BAD &#x274C: {df.reason[index]}")

        food_zh.append(tmp_str)


if __name__ == '__main__':
    # Create new folder to place file into:
    cf = createNewFolder()
    # cf.folder_type = "html"
    cf.auto_run()

    # Import data
    data_import()

    # Generate Website (ZH)
    generate_zh_website(f"{cf.new_folder_name}")
