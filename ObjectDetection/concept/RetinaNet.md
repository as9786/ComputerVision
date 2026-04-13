# Focal Loss for Dense Object Detection

## 1. 서론

- Class imbalance occuers due to the diffference in the number of positive and negative samples
- Since most samples are negative, inefficiencies arise during the training
- Before : A two-stage cascade approach was used to filter region proposals end eliminate background samples + Sampling heuristic
- 위 방법들은 한 단계 탐지기에서는 적용이 어려움 
