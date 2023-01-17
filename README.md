# User-Operation-State-Model-Generator

## About
This is a sample of the tool we create in the research of "Automatic Generation of An Android User Operation State Model for Digital Forensics Analysis". We use this tool to construct state models based on Android event log for digital forensics investigators.

## Installation
Clone this project with:

```git clone https://github.com/HongheZ/User-Operation-State-Model-Generator.git```

## Usage
You can just click the User_Operation_State_Model_Generator.exe to execute the tool. 

Or use the command lines below:
```User_Operation_State_Model_Generator```
![image](https://github.com/HongheZ/ImageFile/blob/main/User-Operation-State-Model-Generator/Command_Screenshot.png)

In this sample, we use the espresso log file as an example. When you execute the exe file, please make sure the two files are in the same directory.

After the tool is successfully executed, three new files will be generated under the current folder: 

UserBehaviorDotFile.dot.pdf(The result state model), UserBehaviorDotFile.dot and statemodel.json.

![image](https://github.com/HongheZ/ImageFile/blob/main/User-Operation-State-Model-Generator/New_File_Generated.png)

## Contribution
Honghe Zhou

Lin Deng

Weifeng Xu

Josh Dehlinger

Suranjan Chakraborty
