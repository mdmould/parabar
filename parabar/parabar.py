from tqdm.auto import tqdm
from pathos.pools import ProcessPool


def map(func, iterables, *args, ncpus = 1, tqdm_kwargs = {}, **kwargs):
    
    if type(iterables) is not zip:
        iterables = zip(iterables)
        
    total = tqdm_kwargs.pop('total', None)
    
    if total is None:
        iterables = list(iterables)
        total = len(iterables)
        
    with ProcessPool(ncpus) as pool:
        
        return list(
            tqdm(
                pool.imap(
                    lambda iterable: func(*iterable, *args, **kwargs),
                    iterables,
                    ),
                total=total,
                **tqdm_kwargs,
                ),
            )
