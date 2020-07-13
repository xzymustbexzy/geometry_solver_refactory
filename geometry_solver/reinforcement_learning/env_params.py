from geometry_solver.entity import Angle, Line, Point, Triangle
from geometry_solver.relationship import (Collineation, CommonVertexAngle,
        IsEquilateralTriangle, IsIsoscelesTriangle, IsRightTriangle,
        NAngleSector, NLineSector, OppositeVerticalAngle, Parallel,
        Perpendicular, SimilarTriangle, SupplementaryAngle, 
        ValueEquivalence, ValueProportion)
from geometry_solver.theorem import valid_theorem


ENTITY_ATTRIBUTES = {
    Point: [],
    Line: ['length'],
    Angle: ['angle'],
    Triangle: ['area', 'circumference']
}

RELATIONSHIP_ATTRIBUTES = {
    Collineation: [],
    CommonVertexAngle: [],
    IsEquilateralTriangle: [],
    IsIsoscelesTriangle: [],
    IsRightTriangle: [],
    NAngleSector: ['ratio'],
    NLineSector: ['ratio'],
    OppositeVerticalAngle: [],
    Parallel: [],
    Perpendicular: [],
    SimilarTriangle: ['ratio'],
    SupplementaryAngle: [],
    ValueEquivalence: []
}

ALL_ENTITY_TYPE = list(ENTITY_ATTRIBUTES.keys())
ALL_RELATIONSHIP_TYPE = list(RELATIONSHIP_ATTRIBUTES.keys())

MAX_ENTITIES = 64
MAX_RELATIONSHIPS = 128

ENTITY_TYPE_NUM = len(ALL_ENTITY_TYPE)
RELATIONSHIP_TYPE_NUM = len(ALL_RELATIONSHIP_TYPE)

ENTITY_ATTRIBUTE_NUM = max([len(attrs) for attrs in ENTITY_ATTRIBUTES.values()])
RELATIONSHIP_ATTRIBUTE_NUM = max([len(attrs) for attrs in RELATIONSHIP_ATTRIBUTES.values()])

THEOREM_NUM = len(valid_theorem)
