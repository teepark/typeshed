# Stubs for itertools

# Based on https://docs.python.org/2/library/itertools.html

from typing import (Iterator, TypeVar, Iterable, overload, Any, Callable, Tuple,
                    Union, Sequence, Generic)

_T = TypeVar('_T')
_S = TypeVar('_S')

def count(start: int = ...,
          step: int = ...) -> Iterator[int]: ... # more general types?
def cycle(iterable: Iterable[_T]) -> Iterator[_T]: ...

def repeat(object: _T, times: int = ...) -> Iterator[_T]: ...

def accumulate(iterable: Iterable[_T]) -> Iterator[_T]: ...

class chain(Iterator[_T], Generic[_T]):
    def __init__(self, *iterables: Iterable[_T]) -> None: ...
    @staticmethod
    def from_iterable(iterable: Iterable[Iterable[_T]]) -> Iterator[_T]: ...

def compress(data: Iterable[_T], selectors: Iterable[Any]) -> Iterator[_T]: ...
def dropwhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def ifilter(predicate: Callable[[_T], Any],
            iterable: Iterable[_T]) -> Iterator[_T]: ...
def ifilterfalse(predicate: Callable[[_T], Any],
                 iterable: Iterable[_T]) -> Iterator[_T]: ...

@overload
def groupby(iterable: Iterable[_T]) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
@overload
def groupby(iterable: Iterable[_T],
            key: Callable[[_T], _S]) -> Iterator[Tuple[_S, Iterator[_T]]]: ...

@overload
def islice(iterable: Iterable[_T], stop: int) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], start: int, stop: int,
           step: int = ...) -> Iterator[_T]: ...

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')

@overload
def imap(func: Callable[[_T1], _S], iter1: Iterable[_T1]) -> Iterable[_S]: ...
@overload
def imap(func: Callable[[_T1, _T2], _S],
        iter1: Iterable[_T1],
        iter2: Iterable[_T2]) -> Iterable[_S]: ...  # TODO more than two iterables

def starmap(func: Any, iterable: Iterable[Any]) -> Iterator[Any]: ...
def takewhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def tee(iterable: Iterable[Any], n: int = ...) -> Iterator[Any]: ...

@overload
def izip(iter1: Iterable[_T1]) -> Iterable[Tuple[_T1]]: ...
@overload
def izip(iter1: Iterable[_T1],
         iter2: Iterable[_T2]) -> Iterable[Tuple[_T1, _T2]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2],
         iter3: Iterable[_T3]) -> Iterable[Tuple[_T1, _T2, _T3]]: ...
@overload
def izip(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3],
         iter4: Iterable[_T4]) -> Iterable[Tuple[_T1, _T2,
                                           _T3, _T4]]: ...  # TODO more than four iterables
def izip_longest(*p: Iterable[Any],
                 fillvalue: Any = ...) -> Iterator[Any]: ...

# TODO: Return type should be Iterator[Tuple[..]], but unknown tuple shape.
#       Iterator[Sequence[_T]] loses this type information.
def product(*p: Iterable[_T], repeat: int = ...) -> Iterator[Sequence[_T]]: ...

def permutations(iterable: Iterable[_T],
                 r: int = ...) -> Iterator[Sequence[_T]]: ...
def combinations(iterable: Iterable[_T],
                 r: int) -> Iterable[Sequence[_T]]: ...
def combinations_with_replacement(iterable: Iterable[_T],
                                  r: int) -> Iterable[Sequence[_T]]: ...
