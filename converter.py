import os

def convert_obj_to_rows(obj_file):
    verts = []
    faces = []
    
    with open(obj_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                if parts[0] == 'v':
                    verts.append([float(x) for x in parts[1:4]])
                elif parts[0] == 'f':
                    face = []
                    for vert_idx in parts[1:]:
                        vert_idx = int(vert_idx.split('/')[0])
                        face.append(verts[vert_idx-1])
                    faces.append(face)
    
    rows = []
    for face in faces:
        if len(face) == 3:
            rows.append([coord for vert in face for coord in vert])
        else:
            print(f"Warning: Skipping non-triangular face: {face}")
    
    return rows


obj_file = 'cat.obj'
rows = convert_obj_to_rows(obj_file)

with open('model.txt', 'w') as f:
    for row in rows:
        f.write(' '.join(str(x) for x in row) + '\n')
