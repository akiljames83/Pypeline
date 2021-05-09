# pyinstrument-decorator https://pypi.org/project/pyinstrument-decorator/
from __future__ import annotations

import webbrowser
from contextlib import ContextDecorator
from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Generator
from typing import Optional
from typing import TypeVar
from typing import Union

# from atomic_write_path import atomic_write_path
# from functional_itertools import CIterable
try:
    from pyinstrument import Profiler
except ModuleNotFoundError:
    print('Please install pyinstrument to utilize the profiler')
    exit(0)


T = TypeVar("T")
_DEFAULT_PATH = "profile.html"


class WrappedProfiler:
    def __init__(
        self: WrappedProfiler,
        *,
        html: bool = False,
        path: Union[Path, str] = _DEFAULT_PATH,
        overwrite: bool = True,
    ) -> None:
        self._html = html
        self._path = path
        self._overwrite = overwrite

    def __enter__(self: WrappedProfiler) -> WrappedProfiler:
        self._profiler = Profiler()
        self._profiler.__enter__()
        return self

    def __exit__(self: WrappedProfiler, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        self._profiler.__exit__(exc_type, exc_val, exc_tb)
        print(_trim_output_text(self._profiler.output_text(unicode=True, color=True)))
        if self._html:
            path_obj = Path(self._path).with_suffix(".html")
            with open(path_obj, mode="w") as fh:
                fh.write(self._profiler.output_html())
            self.open()
        return False

    def open(self: WrappedProfiler) -> None:  # noqa: A003
        webbrowser.open(str(Path(self._path).resolve()))


def _trim_output_text(text: str) -> str:
    lines = text.split('\n')
    lines = [l for l in lines if not l.startswith("Program:")][1:]
    # lines = (
    #     CIterable(text.splitlines())
    #     .dropwhile(lambda x: not x.startswith("Program:"))[1:]
    #     .dropwhile(lambda x: x == "")
    # )
    return "\n".join(lines)


class ProfileMeta(ContextDecorator, type):
    def __call__(  # noqa: U100
        cls: ContextDecorator,
        func: Optional[Callable[..., T]] = None,
        *,
        html: bool = False,
        path: Union[Path, str] = _DEFAULT_PATH,
        overwrite: bool = True,
    ) -> Union[Generator[WrappedProfiler, None, None], Callable[..., T]]:
        wrapped = WrappedProfiler(html=html, path=path, overwrite=overwrite)
        if func is None:

            @contextmanager
            def core_profiler() -> Generator[WrappedProfiler, None, None]:
                with wrapped as cm:
                    yield cm

            return core_profiler()
        else:

            @wraps(func)
            def profiled_func(*args: Any, **kwargs: Any) -> T:
                with wrapped:
                    return func(*args, **kwargs)

            return profiled_func

    def __enter__(cls: ProfileMeta) -> ProfileMeta:
        cls._wrapped_profiler = WrappedProfiler()
        cls._wrapped_profiler.__enter__()
        return cls

    def __exit__(cls: ProfileMeta, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        cls._wrapped_profiler.__exit__(exc_type, exc_val, exc_tb)
        return False


class profile(ContextDecorator, metaclass=ProfileMeta):
    def __enter__(self: profile) -> profile:
        self._wrapped_profiler = WrappedProfiler()
        self._wrapped_profiler.__enter__()
        return self

    def __exit__(self: profile, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        self._wrapped_profiler.__exit__(exc_type, exc_val, exc_tb)
        return False
