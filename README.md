# Prerequisite relationship detection

RefD: Calculate RefD based on wiki article content.

Link-based measure, Reference distance: 
We use related concepts to measure the antecedent relationship between two concepts by calculating the degree of difference in how related concepts refer to each other.

Compared with prerequisites, a more common and observable relationship between concepts is the citation relationship, which exists widely in various forms, such as hyperlinks, citations, notes, etc. Although a single citation relationship does not explain the prerequisite relationship , but a large number of references may have different effects. For example, if most of A's relevant concepts point to B, but a few of B's relevant concepts point to A, then B is more likely to be a prerequisite for A.

# Reference：
Liang C, Wu Z, Huang W, et al. Measuring prerequisite relations among concepts[C]
Proceedings of the 2015 conference on empirical methods in natural language processing. 2015: 1668-1674.

# Method
# 1. Definition of RefD.

$RefD(A,B)=\frac{\sum_{{c_i} \in L(A)} r(c_i,B)w(c_i,A)}{\sum_{{c_i} \in L(A)} w(c_i,A)}-\frac{\sum_{{c_i} \in L(B)} r(c_i,A)w(c_i,B)}{\sum_{{c_i} \in L(B)} w(c_i,B)}$

$𝑟(𝑐_𝑖,𝐵)$：Whether the wiki page of concept $𝑐_i$ contains $𝐵$ is 1, otherwise it is 0;

$𝑤(𝑐_𝑖,𝐴)$：The correlation between concept $𝑐_i$ and concept $𝐴$ as the weight;

$𝐿(𝐴)$：A collection of concepts related to the concept $𝐴$;

The value of $𝑅𝑒𝑓𝐷(𝐴,𝐵)$ is between -1 and 1, the closer to 1, the greater the possibility that $B$ is the priority of $A$, and the closer to -1, the greater the possibility of $A$ being the priority of $B$.

# 2. Selection of concept $𝑨$ related concept set $𝑳(A)$.

Sort the correlation coefficient of each concept $𝑐_𝑖$ and other concepts, select the correlation coefficient value $𝑅_𝑖$ with index 10 as the threshold of this concept, and obtain the threshold $𝑅$ by summing the thresholds of all concepts and averaging.


# 3. Calculate the $RefD(A,B)$ value between A and B.

Specify thresholds $\theta$ for judging prerequisites:

$$
𝑅𝑒𝑓𝐷(𝐴,𝐵)=
\begin{align}
(\theta,1],     if \ B \ is \ a \ prerequisite \ of \ A \\
[-\theta,\theta],      𝑖𝑓 \ 𝑛𝑜 \ 𝑝𝑟𝑒𝑟𝑒𝑞𝑢𝑖𝑠𝑖𝑡𝑒 \ 𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛\\
(-1,-\theta),    if \ A \ is \ a \ prerequisite \ of \ B 
\end{align}
$$
