# Schedule Lynx

![alt text](https://github.com/PurpleRabbit75/Schedule-Lynx/blob/main/Miscellaneous-Developer-Stuff/Schedule-Lynx-icon.png?raw=true)

## Quick Summary

Schedule Lynx is a cross-platform project designed to help groups of 2-12 people compare their weekly schedules. It is especially helpful for college students, but can be used by anyone anywhere.

## Installation

If you do not have Python 3 installed already on your system, you will need to install it first. See python.org for help on how to do this. Once it is installed, you may proceed with these instructions.

To install Schedule Lynx, download it in any way you wish. You can click the green `<> Code` button above and download it as a zip, or git clone the repository if you're more comfortable with that. If you download it as a zip, unzip it. 


Congrats! Schedule Lynx is now installed! The remaining dependencies etc. will automatically install the first time you run the program.

## Inputs and Outputs

Schedule Lynx takes in a pile of .json files and spits out a .jpg file. You specify which files come from and go to which directories by editing `config.json`. There are more details on this in the next section.

## Standard Operating Proceedure

### Adding Schedule JSON Files
To create a new schedule, you will need to edit the files in the `data` folder. In this folder, place at least two `person.json` files. You can create a `person.json` file by copying the `person_template.json` file and editing it to match the schedule of any given person. (NB! People new to JSON usually miss the commas. Pay attention to them!)

The first entry in a `person.json` file must be their name. 
Every subsequent entry in the `person.json` file represents an event recurring at least once a week.
All subsequent entries must follow this pattern:

```
[[18, 30], [22, 0], "MTWRF", "Night Class"]
```
The first pair of numbers specifies the starting hour and starting minute of the recurring event that this entry records. In this case, the event starts at 18:30--equivalent to 6:30 PM. 

The second pair of numbers specifies the hour and minute that the event ends. In this case, the event ends at 22:00--equivalent to 10 PM. 

The third entry is the "day string". Add letters or subtract them from this string to specify which days of the week this particular event occurs on. In this case, the event occurs on Monday (M), Tuesday (T), Wednesday (W), Thursday (R), and Friday (F). An event that occurs only on Wednesdays might look like:
```
[[11, 45], [13, 5], "W", "Lunch"]
```

The fourth entry is a comment field. You can put anything you want there, and as of now, nothing will happen.

Note that events on Saturday or Sunday are not currently supported.

### Adjusting Config Files

 You may later choose to adjust the `config.json` and `colors.json` files as you see fit. More about them will be explained in the technical appendix. 

 ### Running the Program

 To launch the program, simply run the `main.py` file. The simple way to do this is to open Terminal, navigate to the Schedule-Lynx directory, and run `python3 main.py`. You can also run it from within an IDE like IDLE or VS Code.
 You will see a number of status updates printing to your terminal. Then, it will say 
`PROGRAM HAS TERMINATED`

 There should now be a new schedule.jpg file in the Schedule-Lynx folder!

  Included in the Github is _also_ an .exe file. The function of this file is to run the file located in the same directory as the .exe that is named `main.py`. The source code for this is available in the `Miscellaneous-Developer-Stuff` directory.

 # Technical Appendix

If you are reading this, I assume that you know what you're doing around .py and .json files, have some experience with coding, etc. 

## API Documentation

### config.json

- font_size: default value = 13: represents the global font size of all the text in the image. Must be an integer
- start_time: default value = [7, 0]: represents the earliest time value shown in the image. The format is [hours, minutes], where minutes go from 0 to 59 and hours go from 0 to 23. This, for example, is 7 AM. Errors may occur if event times are written in the `person.json` files outside of of the max and min times listed here.
- end_time: default value = [22, 0]: represents the latest time value shown in the image. See previous for more details.
- spacer_pixels: default value = 30: The number of whitespace pixels at the very top of the image. Must be integer. 
- schedule_column_width: default value = 400: The width (in pixels) of each column which contains the colored schedule bars. Must be integer.
- time_column_width: default value = 73: The width (in pixels) of each column which contains the time increments. Must be integer. Each discrete time column has a 1-pixel black border on each side, so the default of 73 is 75 pixels - 2 border pixels.
- row_height: default value = 15: The height in pixels of each row. It's good to keep this at 15 pixels, because the rows are spaced 15 minutes apart in time, so 1 pixel maps to 1 minute. Must be integer.
- data_directory: default value = "data": The directory containing your `person.json` files. You can make this anywhere you like--but don't include any other files in that directory that don't perfectly follow the `person.json` format or errors will ensue. (Eg. it is not advisable to make this path your Downloads folder)
- output_path: default value = "schedule.jpg": Wherever this path points is where the output image will be saved. Make sure to keep the .jpg extension on the end, though--there are no checks on that, and I have no idea what the Pillow library might do with other formats. If you _really_ want to mess with this, the relevant "save file" code is at the end of `main.py`.

### colors.json

`colors.json` consists of a bunch of key-value pairs, formatted like this:
```
 "Crimson": [220, 20, 60]
 ```
The key is irrelevant to the code except as documentation. You can make it whatever you like.
The value must be a valid RGB triple--that is, each number must be an integer between 0 and 255, inclusive. `[0, 0, 0]` is black and `[255, 255, 255]` is white. In this app, all the defaults are CSS Colors (aka HTML colors or Web colors), but they don't _have_ to be. 

These particular colors were selected by an artistic friend of mine for purely aesthetic reasons. In an older draft of the code, I had the colors of each person's block coded into their personal file. This, however, resulted in utter chaos and _really_ bad looking outputs, so I went ahead and standardized it.

If you're interested in messing with `colors.json`, note that which colors map to which person are decided by the order of the colors in this file. Swapping these around or changing the colors will change what color goes to whom. The order of the _people_ on the chart is actually decided by the filenames of the `person.json` files and your own filesystem. On my computer, filenames higher in the alphabet get read first, so I could change the order of the names on the output image by making my data directory tree look like this:
```
/data
  ├── aPerson2.json
  ├── bPerson3.json  
  └── cPerson1.json  
```

The number of entries in `colors.json` determines the number of `person.json` files that the software can process. If you increase the former, you may increase the latter past 12. (If you do so, I also recommend increasing `schedule_column_width` in `config.json`)

## Miscellaneous Notes:


- This system is agnostic to the difference between \ and / when it comes to filepaths, but \ must be escaped in both JSON and Python.