# Engineering Success

## Research

​		We began the project by extensively searching the literature, and we also consulted researchers and professors in related fields. During our conversation with professors, they frequently complained it repeated and time-consuming to screen manually for an enzyme when there is no available suitable one in the database to catalyze the target reaction. They regularly do such work simply based on experience or maybe just by random attempt. 
​		Based on this problem, we conducted further research. We found that several existing software aims to solve these problems. For example, XTMS applies inverse synthesis to search for the metabolic pathways that produce the target compound; and PathPred, proved useful in multistep response prediction. Yet, they do have several defects. For example, XTMS, based on a limited E. coli database, could not identify the precursor material; and using PathPred, it is still inevitable that intermediate reactions will be disconnected. Naturally, an idea occurred to our mind that we may be able to do something to make the research process easier.

## Design

### Preliminary design

​		Our preliminary design was as follows:

- Frontend
  - Users input a reaction, mark the participation substructure and select the corresponding reaction type

- Backend 

  - Receive request from frontend
  - Conduct primary selection by screening the enzymes able to catalyze the reactions that contain the substracture marked in given reactions
  - Pass the enzymes to the similarity-computing module
  - Compute reaction similarity and sort the primarily selected enzymes based on it
  - Backend returns the top 30 enzymes according to the sort results

  Here is a flowchart of our preliminary backend design.

<img src="C:\Users\Tanjf\Desktop\Preliminary_Flowchart.svg" style="zoom:80%;" />



### Iterations

​		We invited our instrcutor to test our software and he advised that we should take cofactors, organism and kinetics into consideration. He also reminded us of auxiliary reactions that recycled cofactors, which may help reduce the reaction cost. 

​		Owing to these precious suggestions, we made  the following changes:

- Option expanded for users

  Cofactor and organism options were added to the frontend interface and taken into account during the enzyme primary selection in backend for more granular searches. Besides, we implented the elastic search of organism option with soundex.

- More information

  To be more relevant to the actual situation, basic return contained extra information about the optimum temprature and pH of the selected enzymes.

-  Furthur return of the auxiliary reaction. 

  Apart from the basic return, we added a furthur return, which gave the relevant kinetic constants to inform researchers could of the suggessted amount ratio of enzyme and substrate for higher efficiency. 

<img src="C:\Users\Tanjf\Desktop\Flowchart.svg" style="zoom:80%;" />

### Advantages

Learning from other existing similar software like PathPred, Ketcher and so on, we notice the importance of user-friendliness. So we choose to design our web software from multiple perspectives. 

From users' point of view, we have optimized the way to use the software. Compared to using the command line to access the software, our web software provides a GUI artboard. Based on Ketcher, we design a user-customized interface supporting users to use our software according to their own preferences. We allow users to draw chemical structures, import .mol file to generate chemical structures.

And from a feedback perspective, our software return to users a complete set of informations about enzyme with intuitive and understandable informations. What's more, our software also return Brenda database links to our predicted enzymes which supports users to explore further informations.

Besides, from the point of view of software implementation, our software supports fuzzy search for the sake of some wrong informations users input. Simultaneously, to increase the speed of enzyme searching, we adopt a heuristic search algorithm to balance the accuracy and speed of searching processes.

It is worth mentioning that our software is free of environment dependence. Our software is running on the web browser and users don't need to download a sophisticated software in their local Windows, Linux or Macos computer. It is easy to accessible to our web software as long as you can access the Internet.

## Build

### Data Collecting

​		We collect enzyme, cofactor, kinetic parameters data from public database Brenda. In order to facilitate use and query, we extract the desired information from the collected data, rebuild it into a new database, and integrate it into our web software.

### Database Building

​		We mainly maintain 3 kinds of databases: reaction DBs, enzyme DBs and kinetic info DBs. Reaction DBs contain information of reactions, mostly used to in prescreening process, to improve MEI's performance. Enzyme DBs include the basic info of each enzyme number, such as organisms, enzyme name and so on. Kinetic info DBs have precise pH, Km, Kcat and temperature info of each enzyme. We obtain these data from open-access databases, such as Brenda and ExplorEnz. A lot of optimization has been done when buliding our self-construct database. In our database, we store the reactions and moledules in SMILES format, instead of the name or chemical formula in the source database. This is to expand the representation power of text info. In support of fuzzy search, we introduce SOUNDEX algorithm, and save an extra soundex column for each column representing a name, so that MEI is robust of the case when user has a typo in the query. 

### Model Selection

#### Enzyme Kinetics

In biochemistry, Michaelis–Menten kinetics is one of the best-known models of enzyme kinetics. The model takes the form of an equation describing the rate of enzymatic reactions by relating reaction rate.

![](C:\Users\蓝\Desktop\equation.svg)

This equation is called the Michaelis–Menten equation, a mathematical model of the reaction. The model is used in a variety of biochemical situations other than enzyme-substrate interaction, including antigen–antibody binding, DNA–DNA hybridization, and protein–protein interaction. It can be used to characterise a generic biochemical reaction, in the same way that the Langmuir equation can be used to model generic adsorption of biomolecular species.

#### RxnSim

​		RxnSim provides methods to compute chemical similarity between two or more reactions and molecules. Molecular similarity is computed based on structural features. Reaction similarity is a function of similarities of participating molecules. The package provides multiple methods to extract structural features as fingerprints (or feature vectors) and similarity metrics. It additionally provides functionality to mask chemical substructures for weighted similarity computations. It uses rCDK and fingerprint packages for cheminformatics functionality.

#### 

####

### Technical Support

#### Back-end

The back-end web framework we uesd is Django. Django makes it easier to build better web apps more quickly and with less code. We know now that REST APIs are important because they let us interact in an easy way with the database. So we ues the Django REST framework to achieve RESTful style and Django REST framework is a powerful and flexible toolkit for building Web APIs. And we use MySQL for its better performance, high availability, scalability, platform-frendly and friendly-interface. Ray is a general-purpose framework for programming a cluster. Ray enables developers to easily parallelize their Python applications or build new ones, and run them at any scale, from a laptop to a large cluster. Ray provides a highly flexible, yet minimalist and easy to use API. We choose Ray for its excellent performance in parallel computing.

![](C:\Users\蓝\Desktop\dg.png)

![](C:\Users\蓝\Desktop\djang-rest-framework-logo.webp)

![](C:\Users\蓝\Desktop\Database-mysql.svg.png)

![](C:\Users\蓝\Desktop\ray_header_logo.png)

#### Front-end



### Service Deployment

​		Nginx is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause BSD-like license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.

![](C:\Users\蓝\Desktop\library-nginx-logo.png)

​		We deploy our frontend and backend project with Nginx and uwsgi. They enables us to use multiple threads and a message queue, thus improving the concurrency and stablity of MEI. In order to connect Web server with calculation server, we turn to rpc so that the backend API can communicate with Ray clusters on the other server.  

## Test

### Validation



## Learn

### Improvement of Design



### Improvement of Build

- **User-Friendliness**

- **Database Optimization**

  

- **Performance Improvement**

  ​		Due to the big scale of the data primarily selected, it took our preliminary software a long time to compute similarity. Therefore, we first seperated the web module and the calculation module, deploying them on different servers. Then we modified the parameters passed to RxnSim and enabled Cache, which improved the speed by 30%. We also found the low efficiency of one-process programming, which could hardly utilize all the resources of servers. Hence, we used a ditributed-computing framework, ray, to furthur improve our speed. The time needed for the same inputs were then reduced by 50%. In pursuit of a better performance, we improved our server to a high-performance one, thus tremendously improving our speed. After all the optimization in those four aspects, the time needed to compare 5000 reactions was reduced from 90s to only 10s.



- **Message Queue**

​		Our preliminary software were quite weak and only supported one client online at the same time. To improve concurrency, we used uwsgi and modified the execution logic of ray so that we could support more clients visiting our sites simultaneously.









# Project Modeling

## Biological Models

### Enzyme Kinetics

​		In biochemistry, Michaelis–Menten kinetics is one of the best-known models of enzyme kinetics. The model takes the form of an equation describing the rate of enzymatic reactions by relating reaction rate.

​		A key factor affecting the rate of a reaction catalyzed by an enzyme is the concentration of substrate, *[S]*. However, studying the effects of substrate concentration is complicated by the fact that *[S]* changes during the course of an in vitro reaction as substrate is converted to product. One simplifying approach in kinetics experiments is to measure the initial rate (or initial velocity), designated *v*.

![](C:\Users\蓝\Desktop\substrate_concentration.jpg)

​		The curve expressing the relationship between *[S]* and *v* has the same general shape for most enzymes, which can be expressed algebraically by the Michaelis-Menten equation.

![](C:\Users\蓝\Desktop\equation.svg)

​		All these terms called the Michaelis constant—are readily measured experimentally. Some enzymes require no chemical groups for activity other than their amino acid residues. Others require an additional chemical component called a cofactor—either one or more inorganic ions or a complex organic or metalloorganic molecule called a coenzyme.

Some coenzymes are expensive(Nicotinamide adenine dinucleotide), our team designed an auxiliary reaction.

![](C:\Users\蓝\Desktop\auxiliary_reaction.png)

## Computer Models

### RxnSim

​		RxnSim is designed to compute biochemical reaction similarity by comparing molecular signatures of individual molecules involved in the input reactions. The tool can compute similarity between a pair of reactions or list(s) of reactions that are provided as input. It implements fingerprint caching to reduce computation time on large datasets.

​		RxnSim implements four algorithms to compute reaction similarity, namely msim, msim_max, rsim and rsim2.

- *msim* 

  *msim* is based on individual similarities of molecules in two reactions. First, each reactant (product) of a reaction is paired with an equivalent (similar) reactant (product) of the other reaction based on pairwise similarity values using hierarchical grouping. A 0 similarity value is assigned to each unpaired molecule. Reaction similarity is then computed by averaging the similarity values for each pair of equivalent molecule(s) and unpaired molecule(s). Molecule equivalences computed can be reviewed using verbose mode in `rs.compute`.

- *msim_max*

  reaction similarity is computed in the same way as described for msim except that the unpaired molecules are not used for computing average.

- *rsim*

  *rsim* is based on cumulative features of reactant(s) and product(s) of two reactions. Each reaction is represented by two fingerprints, one each for the reactants and another for products. Reaction similarity is computed by averaging similarity values obtained by comparing reactants fingerprint and products fingerprints.

- *rsim2*

  *rsim2* is based on cumulative features of all molecules in a reaction forming a reaction fingerprint. Reaction similarity is computed based on the reaction fingerprints of two reactions.

​        Performance of these algorithms was measured based on their ability to identify similar reactions. Distributions of reaction similarities (Fig. a) show a median score of ∼0.2 for *msim* and *rsim* algorithms. *msim* shows a prediction accuracy of more than 95% for a cut-off of 0.55 and the area under ROC curve (AUC) was found to be 0.90 (Fig. b). AUCs for *rsim* and *rsim2* were found to be 0.84 and 0.74, respectively. *rsim* and *rsim2* are more useful for analysis of datasets that are known to have common features, such as, catalysis by same enzyme or having same transformation.

​		Comparison of *msim*, *rsim* and *rsim2* algorithms implemented in RxnSim. (**a**) Density plots of reaction similarity scores. (**b**) Receiver operator characteristic (ROC) plot showing effectiveness of three algorithms (AUC order msim>rsim>rsim2) **© The Author 2015. Published by Oxford University Press**

![](C:\Users\蓝\Desktop\roc.jpg)

​		Our project is implemented based on RxnSim. Through the calculation of these alogrithms, we allow the user to input substrates and products to predict the enzymes required for the reaction and return to the user the most similar results along with the kinetic parameters and other parameters under the input conditions.

### Ray

​		Ray implements a dynamic task graph computation model that supports both the task-parallel and the actor programming models, in which the execution of both remote functions and actor methods is automatically triggered by the system when their inputs become available.[2]

![](C:\Users\蓝\Desktop\Ray.svg)

​		We use Ray's parallel model to leverage our multiple cores machines, so that we can speed up computation and searching in our web application. After applying Ray, the execution speed of our web application increased by about sixty percents.

### Soundex

​		Soundex[3] is a phonetic algorithm for indexing names by sound, as pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling. 

![](C:\Users\蓝\Desktop\soundex.png)

In MySQL, Soundex algorithm is the following:

1. Save the first letter. Map all occurrences of a, e, i, o, u, y, h, w. to zero(0)
2. Replace all consonants (include the first letter) with digits as in the Soundex coding guide above.
3. Replace all adjacent same digits with one digit, and then remove all the zero (0) digits
4. If the saved letter's digit is the same as the resulting first digit, remove the digit (keep the letter).
5. Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it

​      So Soundex is the fuzzy searching model we apply in our web application. We use Soundex to match user input from our database. And we establish Soundex index database to optimize the searching time complexity from *O(n)* to *O(log n)*. It has been proven effective in practice.

### RESTful

​		RESTful model is an architectural style for an application program interface (API) that uses HTTP requests to access and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the reading, updating, creating and deleting of operations concerning resources. [4]

![](C:\Users\蓝\Desktop\api-cycle.webp)

​		RESTful model is exceedingly helpful in our public services for its convenience and lightweight. Adopting RESTful model, which is Django REST framework in our web application, facilitates front-end and back-end interaction and improves work efficiency among we teammates. With Django REST framework, we can connected all of our platforms with the same API. This removes duplicity of code and helps to escalate it easily.

# Reference

1. Varun Giri, Tadi Venkata Sivakumar, Kwang Myung Cho, Tae Yong Kim, Anirban Bhaduri, RxnSim: a tool to compare biochemical reactions, *Bioinformatics*, Volume 31, Issue 22, 15 November 2015, Pages 3712–3714, https://doi.org/10.1093/bioinformatics/btv416
2.  Moritz, Philipp et al. “Ray: A Distributed Framework for Emerging AI Applications.”**[arXiv:1712.05889](https://arxiv.org/abs/1712.05889) [cs.DC]**  https://doi.org/10.48550/arXiv.1712.05889
3. [Modern Parallel and Distributed Python: A Quick Tutorial on Ray | by Robert Nishihara | Towards Data Science](https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8)
4. [Soundex - Wikipedia](https://en.wikipedia.org/wiki/Soundex)
4. [What is REST API (RESTful API)? (techtarget.com)](https://www.techtarget.com/searchapparchitecture/definition/RESTful-API)

5. [What Is MySQL And Why It Is Used? (softwaretestinghelp.com)](https://www.softwaretestinghelp.com/what-is-mysql/)
6. Lehninger Principles of Biochemistry.W.H.Freeman.
7. https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics
8. 
