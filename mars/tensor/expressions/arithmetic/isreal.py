#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2018 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

from .... import operands
from ..utils import inject_dtype
from .core import TensorUnaryOp


class TensorIsReal(operands.IsReal, TensorUnaryOp):
    def __init__(self, casting='same_kind', err=None, dtype=None, sparse=False, **kw):
        err = err if err is not None else np.geterr()
        super(TensorIsReal, self).__init__(_casting=casting, _err=err,
                                           _dtype=dtype, _sparse=sparse, **kw)

    @classmethod
    def _is_sparse(cls, x):
        return False


@inject_dtype(np.bool_)
def isreal(x, **kwargs):
    """
    Returns a bool tensor, where True if input element is real.

    If element has complex type with zero complex part, the return value
    for that element is True.

    Parameters
    ----------
    x : array_like
        Input tensor.

    Returns
    -------
    out : Tensor, bool
        Boolean tensor of same shape as `x`.

    See Also
    --------
    iscomplex
    isrealobj : Return True if x is not a complex type.

    Examples
    --------
    >>> import mars.tensor as mt

    >>> mt.isreal([1+1j, 1+0j, 4.5, 3, 2, 2j]).execute()
    array([False,  True,  True,  True,  True, False])

    """
    op = TensorIsReal(**kwargs)
    return op(x)
