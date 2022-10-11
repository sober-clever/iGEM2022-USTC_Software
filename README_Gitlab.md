# Team USTC-Software 2022 Software Tool

If you team competes in the [**Software & AI** track](https://competition.igem.org/participation/tracks) or wants to
apply for the [**Best Software Tool** Award](https://competition.igem.org/judging/awards), you **MUST** host all the
code of your team's software tool in this repository, `main` branch. By the **Wiki Freeze**, a
[release](https://docs.gitlab.com/ee/user/project/releases/) will be automatically created as the judging artifact of
this software tool. You will be able to keep working on your software after the Grand Jamboree.

> If your team does not have any software tool, you can totally ignore this repository. If left unchanged, this
> repository will be automatically deleted by the end of the season.

## Description

to be continued

## Installation

to be continued

## Usage

### Draw a molecule

MEI chemical structure editor is based on open-source sofware [Ketcher](https://lifescience.opensource.epam.com/ketcher/).

[image: UG-0.png]

Using the tool palette you can:

- Draw and edit the moledule by clicking on and dragging atoms, bonds, and other structures;

- Delete any element by clicking on it with Erase tool;

- Some structures (such as aromatic rings) are integrated in one button. Click on the lower right part of button to see the full list.

- Rendering a moledule from SMILES or `*.mol` file:
  
  click on the folder button (the left one of the following figure), input the SMILES or `*.mol` string and press OK.

- Save the drawn molecule as SMILES or `*.mol` file:
  
  click on the download button (the right one of the following figure) and choose the output format, the editor will show the specified format of the current molecule.
  
  [image: UG-1.png]

- Customize group and input cache
  
  After drawing a group, you can click the "person" button, the group would be saved into the 1st buffer, and the former saved groups will move to the latter place, the fourth is automatically trashed.
  
  [image: UG-2.png]

### Mark the main group

Search algorithm of MEI is mainly based on tracking the change of the main group **from substrate to product**.

- Choose the group to track
  
  click on the Lasso button, then just drag and choose items. The choosed structures would be highlighted by green. In this step, `copy`, `delete`, `mark` and some others' several tools are availble.
  
  [image: UG-3.png]

- Note: if press `mark` when chooing a bond, the atoms at its two sides would be marked.

### Mark or unmark marking a atom

- Click on the `correct` button on the top, the marked atoms will become highlighted by blue, and won't be cancelled when leaving the Lasso button.

- Cancelling a mark by clicking on the `delete` button on the top when some atoms are in the marked state.

[image: UG-4.png]

### Switching from reactant to product, Input cofactor, reaction type and organistm of enzyme

This part is at the left side of the sketching area.

[image: UG-5.png]

- Switching
  
  When switching from reactant to product or vice versa, the curren workspace would be temporarily saved.

- Specifying cofactor
  
  You can specify some cofactors for your query. This is optional and you can specify one or more options. If any cofactor is specified, some kinetic info such as temperature, pH and so on may be returned.

- Choosing a reaction type
  
  You should choose **one** reaction type.

- Input the organism of enzyme
  
  This is optional. If specified, MEI would have a smaller search space. This would improve MEI's performance. Some auxiliray reactions may be returned.

### Result

You can start a search query after you have marked the reactant and product and specified the reaction type. MEI will searchthe optimal enzyme may satisfy your query. Each result contains the following info:

- EC number of the enzyme

- Name of the enzyme

- Cofactor the enzyme needs

- Confidence level

- Kinetic info, often contains optimal temperature, optimal pH and reference.

- Nearest reaction: the nearest reaction to target reaction this enzyme can catalyze.

- Link: further information of this enzyme

- Auxiliray reaction: If there are some auxiliray reactions (i.e. some reactions that may increase the utilization of cofactor so that the cost will be lowered)

Result can be displayed as cards or list. While the card is more intuitive, the list gives more information. You can change the rendering methodby switching the button over the result section.

### Auxiliary Reaction

The user could select cofactor, optimal pH and temperature and then 
begins the second search. MEI will return 4 kinetic constants: km1, km2,
 kcat1, kcat2. And they will be given as a range of values with the 
format of "[max,min]", as is shown below.

[image: UG-6.png]

## Contributing

to be continnued

## Authors and acknowledgment

Show your appreciation to those who have contributed to the project.
