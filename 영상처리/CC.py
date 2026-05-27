import cv2
import numpy as np


def extract_char_components_cc(
    plate_img,
    min_area=5,
    min_h_ratio=0.15,
    min_w_ratio=0.005,
    max_h_ratio=0.95,
    max_w_ratio=0.5,
    debug=False
):
    """
    Connected Component 기반 번호판 문자 후보 추출 함수
    """

    h, w = plate_img.shape[:2]

    # 1. Grayscale 변환
    if plate_img.ndim == 3:
        gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    else:
        gray = plate_img.copy()

    # 2. 노이즈 완화
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    binary_candidates = []

    # 3. THRESH_BINARY / THRESH_BINARY_INV 둘 다 시도
    for thresh_type in [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV]:
        binary = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresh_type,
            31,
            15
        )

        # 4. 작은 노이즈 제거
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            binary,
            connectivity=8
        )

        components = []

        for label_id in range(1, num_labels):
            x = stats[label_id, cv2.CC_STAT_LEFT]
            y = stats[label_id, cv2.CC_STAT_TOP]
            bw = stats[label_id, cv2.CC_STAT_WIDTH]
            bh = stats[label_id, cv2.CC_STAT_HEIGHT]
            area = stats[label_id, cv2.CC_STAT_AREA]

            h_ratio = bh / h
            w_ratio = bw / w
            aspect_ratio = bw / max(bh, 1)

            # 5. 약한 문자 후보 필터링
            if area < min_area:
                continue
            if h_ratio < min_h_ratio or h_ratio > max_h_ratio:
                continue
            if w_ratio < min_w_ratio or w_ratio > max_w_ratio:
                continue

            components.append({
                "label_id": label_id,
                "bbox": [x, y, x + bw, y + bh],
                "area": int(area),
                "h_ratio": float(h_ratio),
                "w_ratio": float(w_ratio),
                "aspect_ratio": float(aspect_ratio),
                "centroid": centroids[label_id].tolist(),
            })

        # x 좌표 기준 정렬
        components = sorted(components, key=lambda c: c["bbox"][0])

        binary_candidates.append({
            "thresh_type": thresh_type,
            "binary": binary,
            "components": components,
            "num_components": len(components)
        })

    # 6. 더 많은 문자 후보가 나온 이진화 결과 선택
    best = max(binary_candidates, key=lambda x: x["num_components"])

    components = best["components"]
    binary = best["binary"]

    if debug:
        vis = plate_img.copy()
        if vis.ndim == 2:
            vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

        for comp in components:
            x1, y1, x2, y2 = comp["bbox"]
            cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)

        return components, binary, vis, best["thresh_type"]

    return components
