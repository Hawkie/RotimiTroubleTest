from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, Type, TypeVar, Union

from src.instructions import instructions
from src.instruments import instruments
from src.curves import curves

T = TypeVar("T", bound=instruments.Instrument)
U = TypeVar("U", bound=instructions.Instructions)


class CurveFactory(ABC, Generic[T, U]):
    @staticmethod
    @abstractmethod
    def create_curve(
        instruments: Sequence[T],
        instructions: U,
    ) -> curves.Curve:
        pass


class RPISwapCurveFactory(
    CurveFactory[
        instruments.RPISwapCurveInstrument, instructions.RPISwapCurveInstructions
    ]
):
    @staticmethod
    def create_curve(
        instruments: Sequence[instruments.RPISwapCurveInstrument],
        instructions: instructions.RPISwapCurveInstructions,
    ) -> curves.RPISwapCurve:
        return curves.RPISwapCurve(instruments, instructions)


class IRSwapCurveFactory(
    CurveFactory[
        instruments.IRSwapCurveInstrument, instructions.IRSwapCurveInstructions
    ]
):
    @staticmethod
    def create_curve(
        instruments: Sequence[instruments.IRSwapCurveInstrument],
        instructions: instructions.IRSwapCurveInstructions,
    ) -> curves.IRSwapCurve:
        return curves.IRSwapCurve(instruments, instructions)


# add more concrete factories for different curve types
# each curve type has a specific factory, instrument type, and instructions.


# Create the dictionary
_factories: dict[
    curves.CurveType, Any
] = {  # TODO: use proper type hint for dict value type
    curves.CurveType.RPISWAPINFLATION: RPISwapCurveFactory,
    curves.CurveType.IRS: IRSwapCurveFactory,
    # Add more entries for other subclasses
}


def create_factory(curve_type: curves.CurveType) -> Type[CurveFactory[T, U]]:
    factory: Type[CurveFactory[T, U]] | None = _factories.get(curve_type)

    if factory:
        return factory
    else:
        raise ValueError("{curve_type} is not a recognised curve type.")


def main() -> None:
    pass
