import numpy as np

kb_vectors = {
    "kb_001": np.array([0.1, 0.2, 0.3]),
    "kb_002": np.array([0.0, 0.9, 0.1]),
    "kb_003": np.array([0.5, 0.1, 0.7])
}


new_vector=np.array([0.11,0.19,0.31])


def cosine_similarity(vec1,vec2):
    dot=np.dot(vec1,vec2)
    norm1=np.linalg.norm(vec1)
    norm2=np.linalg.norm(vec2)
    return dot/(norm1 * norm2)


threshold=0.85


lengthvec=len(kb_vectors)

print(lengthvec)

for kb,kb_vector in kb_vectors.items():
    sim=cosine_similarity(new_vector,kb_vector)
    # print(f"similarity with {kb}: {sim}")
    if sim > 0.85:
        print(f"similarity found {kb}")



