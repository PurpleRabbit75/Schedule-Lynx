# Schedule Lynx

![alt text](https://github.com/PurpleRabbit75/Schedule-Lynx/blob/main/Miscellaneous-Developer-Stuff/Schedule-Lynx-icon.png?raw=true)

## Quick Summary

Schedule Lynx is a cross-platform project designed to help groups of 2-12 people compare their weekly schedules. It is especially helpful for college students, but can be used by anyone anywhere.

## Installation

If you do not have Python 3 installed already on your system, you will need to install it first. See python.org for help on how to do this. Once it is installed, you may proceed with these instructions.

To install Schedule Lynx, download it in any way you wish. You can click the green `<> Code` button above and download it as a zip, or git clone the repository if you're more comfortable with that. If you download it as a zip, unzip it. 


Congrats! Schedule Lynx is now installed! The remaining dependencies etc. will automatically install the first time you run the program.

## Inputs and Outputs

Schedule Lynx takes in a pile of .json files and spits out a .jpg file. You specify which files come from and go to which directories by editing config.json. There are more details on this in the next section.

## Standard Operating Proceedure

### Adding Schedule JSON Files
To create a new schedule, you will need to edit the files in the "data" folder. In this folder, place at least two `person.json` files. You can create a `person.json` file by copying the `person_template.json` file and editing it to match the schedule of any given person. (NB! People new to JSON usually miss the commas. Pay attention to them!)

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

## Miscellaneous Notes:

- You can expand this for an arbitrary number of people by adding more entries to colors.json. 

- This system is agnostic to the difference between \ and / when it comes to filepaths, but \ must be escaped in both JSON and Python.