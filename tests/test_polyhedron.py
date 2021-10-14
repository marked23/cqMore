import unittest
import sys
sys.path.append('..')

from cqmore.polyhedron import gridSurface, uvSphere, hull
from cqmore.cq_typing import FaceIndices
from typing import cast

class TestPolyhedron(unittest.TestCase):
    def test_uvSphere(self):
        sphere = uvSphere(10, 3)
        self.assertListEqual(
            [(0, 1, 7), (0, 7, 6), (1, 2, 8), (1, 8, 7), (2, 3, 9), (2, 9, 8), (3, 4, 10), (3, 10, 9), (4, 5, 11), (4, 11, 10), (5, 0, 6), (5, 6, 11), (12, 1, 0), (12, 2, 1), (12, 3, 2), (12, 4, 3), (12, 5, 4), (12, 0, 5), (13, 6, 7), (13, 7, 8), (13, 8, 9), (13, 9, 10), (13, 10, 11), (13, 11, 6)],
            cast(list[FaceIndices], sphere.faces)
        )

    def test_gridSurfae(self):
        points = [
            [(0, 1, 0), (10, 0, 0), (20, 0, 0)],
            [(0, 10, 0), (10, 10, 1), (21, 10, 0)],
            [(0, 20, 0), (10, 21, 0), (20, 20, 0)]
        ]

        sf = gridSurface(points, 1)

        self.assertEqual(18, len(cast(list, sf.points)))
        self.assertEqual(32, len(cast(list, sf.faces)))

    def test_hull(self):
        points = (
            (50, 50, 50),
            (50, 50, 0),
            (-50, 50, 0),
            (-50, -50, 0),
            (50, -50, 0),
            (0, 0, 50),
            (0, 0, -50)
        )

        convex_hull = hull(points)

        self.assertEqual(10, len(cast(list, convex_hull.faces)))
        self.assertEqual(7, len(cast(list, convex_hull.points)))

if __name__ == '__main__':
    unittest.main()
