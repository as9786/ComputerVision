# VSR : A Unified Framework for Document Layout Analysis combining Vision, Semantics and Relations

## 초록
- DLA를 위해서 vision, semantics and relations 활용
- NLP-based model은 layout modeling을 하는데 있어서 불충분한 기능들
- CV-based model은 부족한 modality fusion and relation modeling
- VSR은 NLP, CV 둘 다 지원
- 2-stream network를 이용해, modality-specific visual and semantic feature를 추출하고 이를 적절히 융합해 상호보완 정보를 최대한 활용
- Component 후보들을 감안해 GNN을 기반으로 하는 relation module을 삽입. Component 간의 관계를 모형화하고 최종 결과물 출력

