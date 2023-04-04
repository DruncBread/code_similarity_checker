# Copyright (C) 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test components for testing program graphs."""


# pylint: disable=missing-docstring
# pylint: disable=pointless-statement,undefined-variable
# pylint: disable=unused-variable,unused-argument
# pylint: disable=bare-except,lost-exception,unreachable
# pylint: disable=global-variable-undefined


def caawld():
  x = 1
  y = x*2+199
  z = why(x, y)
  return z


def why(arg0, arg1):
  return arg0 + arg1


def assignments():
  a, b = 0, 0
  c = 2 * a + 1
  d = b - c + 2
  a = c + 3
  return a, b


def fn_with_inner_fn():
  x=y=22
  x=y-22



def repeated_identifier():
  x = 0
  x = x+2+3+66
  x = 31654
  return x
