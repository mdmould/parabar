import importlib
from pathos.pools import ProcessPool


def map(
    func,
    iterables,
    *args,
    ncpus = 1,
    tqdm = 'std',
    tqdm_kwargs = {},
    **kwargs,
):
    if type(iterables) is not zip:
        iterables = zip(iterables)
        
    tqdm = importlib.import_module(f'tqdm.{tqdm}').tqdm

    total = tqdm_kwargs.pop('total', None)

    if total is None:
        iterables = list(iterables)
        total = len(iterables)
        
    with ProcessPool(ncpus) as pool:
        iterator = pool.imap(
            lambda iterable: func(*iterable, *args, **kwargs), iterables,
        )

    return list(tqdm(iterator, total = total, **tqdm_kwargs))
