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

class C:

    def func1(self):
        x = 1
        y = x * 2 + 199
        z = self.why(x, y)
        return z

    def func2(arg0, arg1):
        return arg0 + arg1

    def func3(self):
        a, b = 0, 0
        c = 2 * a + 1
        a = c + 3
        return a, b

    def fn_with_inner_fn(self):
        self.func1()
        self.func2(100)

    def repeated_identifier(self):
        x = 0
        x = x + 2 + 3 + 66
        return x
