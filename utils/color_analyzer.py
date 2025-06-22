from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_main_colors(image: Image.Image, n_colors=3):
    """
    PIL.Image 객체에서 주요 색상 추출

    Parameters:
        image: PIL.Image.Image 객체
        n_colors: 추출할 색상 수

    Returns:
        주요 RGB 색상 리스트 (예: ["RGB(255, 240, 230)", ...])
    """
    image = image.convert('RGB')
    image = image.resize((200, 200))  # 성능 최적화

    img_np = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(img_np)
    colors = kmeans.cluster_centers_.astype(int)

    return [f"RGB({r},{g},{b})" for r, g, b in colors]
