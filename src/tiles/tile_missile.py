#!/usr/bin/env python3

"""Missile tile.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    ActionSquare,
    BlankSquare,
    MachineSquare,
)
from .tile import Tile


class MissileTile(Tile):
    """The missile bay launches explosive torpedoes, science probes and boarding craft.

    It must have exterior facing.

    """

    ABBREVIATION: str = 'mi'

    COLOR = colors.RED_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [

        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, MachineSquare, ],
        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, MachineSquare, ],
        [BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   ],
        [BlankSquare,   MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [BlankSquare,   BlankSquare,   ActionSquare,  BlankSquare,   BlankSquare,   ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
