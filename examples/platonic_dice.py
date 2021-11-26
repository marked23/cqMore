from typing import cast

from cadquery import Face
from cqmore import Workplane
from cqmore.polyhedron import tetrahedron, hexahedron, octahedron, dodecahedron, icosahedron

number_of_faces = 12 # 4, 6, 8, 12 or 20
radius = 10
font_name = 'Arial Black'
font_size = 5 if number_of_faces < 20 else 3
font_distance = 1
detail = 0
fillet = 0.2

platonic_polyhedra = {
    4: tetrahedron, 
    6: hexahedron, 
    8: octahedron, 
    12: dodecahedron, 
    20: icosahedron
}

dice = (Workplane()
           .polyhedron(
               *platonic_polyhedra[number_of_faces](radius, detail)
           ).fillet(fillet)
       )

faces = dice.faces('%PLANE').vals()
nums = len(faces)
texts = Workplane()
for i in range(nums):
    texts.add(
        Workplane(faces[i])
            .workplane(origin = cast(Face, faces[i]).Center())
            .text(
                str(nums - i), 
                font_size, 
                -font_distance,
                font = font_name
            )
    )

dice = dice.cut(texts)

show_object(dice) # type: ignore