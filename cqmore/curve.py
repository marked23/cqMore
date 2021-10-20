from math import sin, cos, tau

from .cq_typing import Point2D

def circle(t: float, radius: float) -> Point2D:
    theta = t * tau
    return (radius * cos(theta), radius * sin(theta))


def helix(t, radius, slope):
    theta = t * tau
    return (radius * cos(theta), radius * sin(theta), radius * slope * t)


def torusKnot(t, p, q):
    phi = t * tau
    r = cos(q * phi) + 2
    p_phi = p * phi
    return (r * cos(p_phi), r * sin(p_phi), -sin(q * phi))


def parametricEquation(f, **params):
    return lambda t: f(t, **params)