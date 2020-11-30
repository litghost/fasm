#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2020  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from warnings import warn

# Parsers available
available = []

try:
    from fasm.parser.antlr import \
        parse_fasm_filename, parse_fasm_string, implementation
    available.append('antlr')
except ImportError as e:
    warn('Importing fasm.parse_fasm: {}'.format(e), RuntimeWarning)
    warn('Falling back on slower textX parser implementation', RuntimeWarning)
    from fasm.parser.textx import \
        parse_fasm_filename, parse_fasm_string, implementation

# The textx parser is available as a fallback.
available.append('textx')
