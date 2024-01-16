# End-to-ENd Object Detection with Transformers

## Hungarian algorithm

- 두 집합 사이의 일대일 대응 시 가장 비용이 적게 드는 bipartite matching(이분 매칭)을 찾는 algorithm
- 어떠한 집합 I와 사상 대상인 집합 J가 있으며, $i \in I$를 $j \in J$에 사상하는데 드는 비용을 c(i,j)라고 할 때, $\sigma$ : I -> J로의 일대일 대응 중 가장 적은 비용이 드는 사상에 대한 permutation $\sigma$를 찾는 것
- Permutation : 사상 시 최적의 순서에 대한 식별자
- I, J에 대한 비용을 표현한 행렬에 대하여 동작
