# Proof of Concept

## Theoretical Support

​		Enzyme promiscuity is the ability of the enzyme to specifically catalyze certain reactions left to catalyze many other reactions. In some cases, promiscuity is associated with conformational diversity; that is, the conformational changes that have occurred in evolution allow the same enzyme to adapt to different substrates. This provides theretical support for the idea that the same enzyme may catalyze similar reactions.

​		Our algorithms to  compute reaction similarity are explained in the article[1] introducing RxnSim. The main idea is to extract feature vectors from reactions or molecules and compute based on them. And the article also shows the ROC curve of the algorithm.

## Dry Lab Validation

We have collected a great amount of validation enzyme reaction dataset from online database and apply them to our web software to see how our program performs. We choose different types of reaction, select different types of cofactors and predicting in different organisms.

We choose this reaction:.

## Wet Lab Validation

​		USTC Team offered the pathway they desgned to synthesize Borneol. Those reactions were then input to our website and search for potential enzymes. Certain enzymes selected were exactly the same as those mannually screened by USTC Team. Besides, our website found some enzymes which may contribute for future research.

<img src="C:\Users\Tanjf\Desktop\wet_lab1.png" style="zoom:67%;" />

<img src="C:\Users\Tanjf\Desktop\wet_lab2 .png" alt="wet_lab2 " style="zoom:67%;" />

<img src="C:\Users\Tanjf\Desktop\wet_lab3.png" alt="wet_lab3" style="zoom: 80%;" />

​		We also invited NNU Team to validate our software. They searched for enzymes on our platform and compared the results with the ones the used in practice. It turned out that our platform successfully returned the enzymes they used, which inspired us a lot. 

​		<img src="C:\Users\Tanjf\Desktop\NNU.jpeg" style="zoom:80%;" />

## Biological Corporation Validation

​		We visited Anhui Lianchuang Biological Medicine Co., LTD and discussed with their researchers. They offered us their data information during their production process. The data were then input to our  platform and the results were given back to the corporation. The enzymes we selected were quite similar to the ones they used.



## Refrences

[1] Varun Giri, Tadi Venkata Sivakumar, Kwang Myung Cho, Tae Yong Kim, Anirban Bhaduri. RxnSim: a tool to compare biochemical reactions. *Bioinformatics*, Volume 31, Issue 22, 15 November 2015, Pages 3712–3714, https://doi.org/10.1093/bioinformatics/btv416