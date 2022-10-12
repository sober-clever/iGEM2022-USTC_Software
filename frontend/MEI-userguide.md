# MEI User Guide

中文版用户指南[请点击此处](MEI-userguideCN.html)

## 1. Introduction

### 1.1. Purpose

This user guide is written for medical and biological perosonnel to use MEI, clarifing how to find a proper enzyme aiming at a specfic biological-chemical reaction, explaining the usage of the system for users and providing references and help when essential.

Intended readers: Staff or research fellow in biological/medical corporations or organizations, developing and testing perosonnel of the MEI.

### 1.2. Background

- Project Name: MEI(Modefied Enzyme Interface)
- Precenters: All participants in iGEM-2022 Team:USTC-Software.
- Developers: iGEM-2022 Team:USTC-Software.
- Product users: All users that needs to find a proper enzyme for a designated biological-chemical reaction, iGEM participants, project precenters, developers and users.

## 2. Usage

### 2.1. Inputting chemical structure

The chemical structure editor of MEI is based on a free and open-source editor: [Ketcher](https://github.com/ggasoftware/ketcher). On the basis of it, our team have made a series of development and adjustment to adapt with Project-MEI. On behalf of iGEM-2022 Team: USTC-Software, we would like to express our sincerest thanks and respect to the open-source workers for their work.

- Main module: Chemical Draw\
The alteration struct-editor by iGEM-2022 Team:USTC-Software is shown in the following figure.\
![](img/UG-0.png)\
The Editor enables inputting a wide variety of atoms and bonds, including C-C single,double,triple bonds, single up/down bonds, aromatic bonds etc. Meanwhile, it enables one-click input for some complex structures(Benzene, Cyclopentadiene for example) and some commonly used biochemical protection groups like Boc and MOM.\
The user could choose the bonds and structure they want to input, then move the mouse to the sketching area, adding them with a click or click-move. Some structures (Cyclopentadiene for exmaple) is collapsed in a button, which needs to click the bottom-right area of the button. Then choose the template group after the dropdown list displayed.
- Rendering SMILES and `.mol` on sketching area\
    The user could click the button with a file-folder icon, which is shown in the left of the following figure, paste the SMILES and mol string into the input section, and click the OK-button. The editor will render the chemical the user inputs.
- Read chemicals on sketching area as `.mol` and SMILES\
    The user could click the button with a download icon, which is shown in the right of the following figure and choose the output format. The editor will read chemicals on the sketching area as given format, what needs to do is copy it.\
    ![](img/UG-1.png)
- Customized groups input and Custom cache\
    The user could click the button with a human-like icon after drawn the group. The chemical will be stored in the first section of the cache, which is shown in the following figure.\
    ![](img/UG-2.png)\
    The former groups' and chemicals' offsets will be added 1. When 4 sections are fulled, the editor will automatically delete the chemical in section 4 when adding a new chemical, which is the earlist chemical joined in the queue.\
    This cache used `localStorage`, it is smiliar with cookie, but has more space than cookie. However, `localStorage` is often used to store the data that don't needs to interact with backend.

### 2.2. The Capture of the main reaction groups
The MEI depends on tracking the *change* of the groups involved in the reaction to search for proper enzyme. And the change needs the user to emphasize.
- Choose a part of the chemical\
    The user could choose the Selection tool on the left-top of the editor and choose the groups by dragging the mouse. The selected part will be covered with a green circle, as is shown below.\
    ![](img/UG-3.png)\
    Meanwhile, some buttons on the top of the editor will be enabled. The user can copy, delete or capture this selected-part.\
    Besides, the user can select a single atom or bond by clicking it when selected the selection button.
- Capture and Uncapture ATOMS\
    When a part of the chemical is selected, the user could click the button with a tick icon to capture the selected atoms. The captured atoms will be covered with a blue circle. The circle won't disappear by deselecting the selection button, but it will play a role as a reminder, as is shown below. The difference of the captured atoms will finally have an effect on the results.\
    ![](img/UG-4.png)\
    The uncapture button is at the right of the capture button, click it after selecting the captured atoms will uncapture them.
    >Attention: The editor will capture atoms on both ends of a selected bond.

### 2.3. Switch, Select and Input
This section is on the left of the editor, structure is shown below.\
![](img/UG-5.png)\
- *Switching* Reactant and Product\
    The user could switch inputs for reactants and products by selecting the two radio buttons on the left side of the editor. MEI will store the chemical and captured atoms when switching.
- *Select* cofactors\
    The user could select needed cofactors up to 6 classes. It is an optional and multi-select section. MEI will return some kinetic factors, best pH, best temperature, for example, if one or more cofactors are selected.
- *Select* reaction type\
    The user could *and may* select one reaction on the dropdown list under the cofactor buttons.
- *Input* enzyme organism\
    The user could input the organism of an enzyme in the input box under the selection-box for reaction type. MEI will narrow down the selection for the organism type. And according to the specific situation to give the auxiliary reaction options probabilistically.

### 2.4 Search and Return
After captured atoms in reactant and product and selected type, the user could click the search button to find the nearest enzyme. Information returned will be displayed in the following format:
- EC number
- Name
- Cofactor
- Prediction Accuracy (A constant between 0 and 1, the bigger, the better.)
- Kinetic Parameters consists of optimal pH, Temperature, and given reference.
- Nearest Reaction, the reaction this enzyme is able to catalyze and closest to the target reaction, usually in the form of "Reactant -> Product".
- Description links to this enzyme from 4 major enzyme databases(BRENDA, Uniprot, PDB, PubMed).
- Additionally, if an auxiliary reaction exists, MEI will give an interface for the user to input more reaction information.

It will be rendered as cards or lists. The former is more intuitive and the latter gives more information. The user could change the rendering method by switching the button over the result section.

It is worth mentioning that our team have used [RDKit-JS](https://github.com/rdkit/rdkit-js), an open-source tool for our chemical rendering. On behalf of iGEM-2022 Team: USTC-Software, we would like to express our sincerest thanks and respect again to the open-source workers for their work.

### 2.5 Auxiliary Reaction
Some enzymes have auxiliary reactions when catalyzing chemical reactions. Then the auxiliary reaction button in the page will become executable. The user could click it and the auxiliary reaction interface would display, as is shown below.\
![](img/UG-6.png)\
The user could select cofactor, optimal pH and temperature and then begins the second search. MEI will return 4 kinetic constants: km1, km2, kcat1, kcat2. And they will be given as a range of values with the format of "[max,min]", as is shown below.
>Attention! If the range is [0,100000], then the reaction constant does not exist.
![](img/UG-7.png)

## 3. Installation and Initialization

There is no need for installation of MEI. Simply open the corresponding web client to operate.