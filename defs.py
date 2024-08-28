def jc_set_mapper(pair):
    col1, doc1 = pair[0]
    col2, doc2 = pair[1]
    inter = 0
    union = 0
    for i in range(len(doc1)):
        if doc1[i] != 0 and doc2[i] != 0:
            inter += 1
        if doc1[i] != 0 or doc2[i] != 0:
            union += 1
    sim = inter/union
    return (col1, col2, sim)

def jc_bag_mapper(pair):
    col1, doc1 = pair[0]
    col2, doc2 = pair[1]
    inter = 0
    union = 0
    for i in range(len(doc1)):
        if doc1[i] != 0 or doc2[i] != 0:
            inter += min(doc1[i],doc2[i])
            union = doc1[i] + doc2[i]
    sim = inter/union
    return (col1, col2, sim)

def cs_mapper(pair):
    col1, doc1 = pair[0]
    col2, doc2 = pair[1]
    dot_prod = 0
    doc1_prod = 0
    doc2_prod = 0
    for i in range(len(doc1)):
        dot_prod += doc1[i]*doc2[i]
        doc1_prod += doc1[i]**2
        doc2_prod += doc2[i]**2
    sim = dot_prod / (doc1_prod*doc2_prod)**0.5
    return (col1, col2, sim)
