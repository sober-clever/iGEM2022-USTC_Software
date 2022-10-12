# Proof of Concept

​		Enzyme promiscuity is the ability of the enzyme to specifically catalyze certain reactions left to catalyze many other reactions. In some cases, promiscuity is associated with conformational diversity; that is, the conformational changes that have occurred in evolution allow the same enzyme to adapt to different substrates. This provides theretical support for the idea that the same enzyme may catalyze similar reactions.  Besides, the algorithms of extracting feature vectors to compute reaction similarity described in the RxnSim paper showed us  how to conduct similarity computing and comparing.

​		Apart from our theoretical support, we conducted various validation. We invited USTC Team and NNU Team to use our website. The enzymes they used in practice were successfully selected. We also asked reaserchers Anhui Lianchuang Biological Medicine Co., LTD for their data information and input them on our website. The results turned out to be optimistic as well.

# Engineering Success

​	In the earlier stage we extensively searched literature and consulted researchers. During our communications, we were told it was time-comsuming to manully screen an enzyme when there's no available suitable one in the enzyme database. Thus we conducted furthur research on this problem and decided to develop a user-friendly website to help select enzymes based on reaction similarity comparing.

​	We firstly came up with a simple design which received given reactions and returned selected enzymes according the similarity computing results. However, in the internal test, it was found inefficient and unstable. 

​		Then our iterations began. The web module and computing module were separated and a distrbuting computing framework was utilized to speed up. Thanks to our instructor's advice and collaborators' feedbacks, more information like kinetics and more functions like auxiliary reaction search were added to our interface, which contributed to user-friendliness.  