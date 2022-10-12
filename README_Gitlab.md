# Team USTC-Software 2022 Software Tool

## Description

This project receives the reactant and generation structure, and the specified group, by preliminarily screening the enzymes of the substrate and generation containing the corresponding group in the database, and then comparing the enzyme-catalyzed reaction with the reactions given by the user to find the enzymes that can catalyze the reaction given by the user or have catalytic potential, and output it in a user-friendly form.

## Installation

### Web Server

#### OS

- Ubuntu 20.04

#### Python

Python packages required:

- Python version 3.8.10
- Django == 4.1
- djangorestframework == 3.14.0
- PyMySQL == 1.0.2
- ray == 1.11.0
- rdkit == 2022.3.4
- rpyc == 5.1.0
- django-cors-headers == 3.13.0

#### MySQL

Download the [dump of our database](https://github.com/sober-clever/iGEM2022-USTC_Software/blob/main/DumpDB.sql) from Github.

```shell
$ mysql
$ source /path/to/InitDB.sql
$ mysql -u iGEM -p "IGEM_PAssword"
$ source /path/to/DumpDB.sql
```

#### Nginx

Install nginx:

```shell
sudo apt install nginx
```

Enter nginx directory:

```shell
cd /etc/nginx
```

The `nginx.conf` and `uwsgi.ini` is in the `nginx` directory.

Copy the `nginx.conf` and `uwsgi.ini` into the directory.(You need to change the path of the backend   project in `uwsgi,ini` to the actual path of the backend project on your server)

Run the command:

```shell
uwsgi --ini uwsgi.ini    
```

Then:

```shell
sudo systemctl start nginx
```

### Calculation Server

#### OS

- Ubuntu 20.04

#### Python

Python packages required:

- Python version 3.8.10
- rpyc == 5.2.3
- rpy2 == 3.5.4
- ray == 2.0.0

#### R

R packages required:

- R version 3.6.3
- rJava
- RxnSim

#### Java

openjdk version "1.8.0_342"

## Usage

### Draw a molecule

MEI chemical structure editor is based on open-source sofware [Ketcher](https://lifescience.opensource.epam.com/ketcher/).

![](https://static.igem.wiki/teams/4240/wiki/img/ug-0.png)

Using the tool palette you can:

- Draw and edit the moledule by clicking on and dragging atoms, bonds, and other structures;

- Delete any element by clicking on it with Erase tool;

- Some structures (such as aromatic rings) are integrated in one button. Click on the lower right part of button to see the full list.

- Rendering a moledule from SMILES or `*.mol` file:
  
  click on the folder button (the left one of the following figure), input the SMILES or `*.mol` string and press OK.

- Save the drawn molecule as SMILES or `*.mol` file:click on the download button (the right one of the following figure) and choose the output format, the editor will show the specified format of the current molecule.)
  
  ![](https://static.igem.wiki/teams/4240/wiki/img/ug-1.png)

  
  
  
  
- Customize group and input cache
  
  After drawing a group, you can click the "person" button, the group would be saved into the 1st buffer, and the former saved groups will move to the latter place, the fourth is automatically trashed.
  
  ![](https://static.igem.wiki/teams/4240/wiki/img/ug-2.png)

### Mark the main group

Search algorithm of MEI is mainly based on tracking the change of the main group **from substrate to product**.

- Choose the group to track
  
  click on the Lasso button, then just drag and choose items. The choosed structures would be highlighted by green. In this step, `copy`, `delete`, `mark` and some others' several tools are availble.
  
  ![](https://static.igem.wiki/teams/4240/wiki/img/ug-3.png)

- Note: if press `mark` when chooing a bond, the atoms at its two sides would be marked.

### Mark or unmark marking a atom

- Click on the `correct` button on the top, the marked atoms will become highlighted by blue, and won't be cancelled when leaving the Lasso button.

- Cancelling a mark by clicking on the `delete` button on the top when some atoms are in the marked state.

![](https://static.igem.wiki/teams/4240/wiki/img/ug-4.png)

### Switching from reactant to product, Input cofactor, reaction type and organistm of enzyme

This part is at the left side of the sketching area.

![](https://static.igem.wiki/teams/4240/wiki/img/ug-5.png)

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

![](https://static.igem.wiki/teams/4240/wiki/img/ug-6.png)

## Contributing

Feel free to contact us, post an issue or merge request if you have any idea!

## Authors and acknowledgment

Brenda and ExplorEnz, who provide us plenty of data.

RxnSim, which enables us to compute reaction similarity.

Ray, which helps us speed up software.

The Western Library of USTC, who gives us one year’s access to Room 214, where we get accomplished most of our work.

Anhui Lianchuang Biological Medicine Co.,Ltd, who showed us around the company and made a lot of practical suggestions.

The University of Science and Technology of China Initiative Foundation, which had been giving us sponsorship and firm support all these years.

The School of Life Sciences, USTC, for their academic support and inspiring advice on our project.

The University of Science and Technology of China Education Foundation, for their selfless financial help.

The frontend and backend group of USTC-Software, who mainly built the software.