#モジュールを使うために使用する記述

import random

number  = random.randint(1, 6)

print("サイコロの目は:", number)

#--------------------------------#

#モジュールの中から適切なメソッドを使うために使用する記述

from random import randint

number = randint(1, 6)

print("サイコロの目は:", number)

#--------------------------------#

#モジュールを別名で使うために使用する記述

import random as r

number = r.randint(1, 6)

print("サイコロの目は:", number)